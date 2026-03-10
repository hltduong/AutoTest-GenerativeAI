# Step-by-Step: Grafana + k6 and Allure Reports

## Part 1: Grafana + k6

Choose one: **Local (Docker)** or **Grafana Cloud**.

---

### Option A: Local Setup (Docker)

#### Step 1: Start Prometheus + Grafana

```bash
# From project root
docker compose -f docker/docker-compose.yml up -d

# Wait ~10 seconds for services to start
```

#### Step 2: Run k6 and Push Metrics

```bash
./scripts/k6_local.sh                    # smoke test
./scripts/k6_local.sh k6/agest_load.js   # load test
```

**Windows:** Use `scripts\k6_local.bat` or `scripts\k6_grafana.bat` instead of the `.sh` scripts.

#### Step 3: Open Grafana and Import Dashboard

1. Open **http://localhost:3000**
2. Login: **admin** / **admin** (change password if prompted)
3. Go to **Dashboards** → **New** → **Import**
4. Enter dashboard ID: **19665** (k6 Prometheus)
5. Select **Prometheus** data source → **Import**

You should see k6 metrics (response times, error rate, VUs).

#### Step 4: Stop

```bash
docker compose -f docker/docker-compose.yml down
```

---

### Option B: Grafana Cloud (Free) + k6

### Step 1: Create Grafana Cloud Account

1. Go to **https://grafana.com/products/cloud/k6/**
2. Click **Start free** or **Sign up**
3. Sign up with email, Google, or GitHub
4. Verify your email if prompted

### Step 2: Create a k6 / Prometheus Stack

1. Log in to **Grafana Cloud** → https://grafana.com/auth/sign-in
2. Go to **My Account** (top right) → **Stacks**
3. Click **Create stack** (or use existing)
4. In the stack, find **Prometheus** (or **Metrics**)
5. Note your **Prometheus Remote Write** endpoint and credentials:
   - URL: `https://prometheus-prod-XX-XX.grafana.net/api/prom/push`
   - Username: usually your stack ID (e.g. `123456`)
   - Password: a generated API token

**Alternative path (k6-specific):**

1. Go to **https://grafana.com/products/cloud/k6/**
2. Follow **Get started with k6 on Grafana Cloud**
3. You’ll get a **Prometheus remote write** URL and credentials

### Step 3: Get Your Credentials

In Grafana Cloud:

1. **My Account** → **Stacks** → select your stack
2. Open **Prometheus** (or **Metrics** / **Details**)
3. Copy:
   - **Remote Write URL** (e.g. `https://prometheus-prod-XX-XX.grafana.net/api/prom/push`)
   - **Username** (your Prometheus instance ID, often numeric)
   - **Password**: Create an **Access Policy** token with `metrics:write` scope:
     - **Security** → **Access Policies** → **Add new token**
     - Or use the **Prometheus** section’s “Generate token” / “Create token” button

### Step 4: Run k6 with Prometheus Remote Write

```bash
# Set env vars (replace with your values)
export K6_PROMETHEUS_RW_SERVER_URL="https://prometheus-prod-XX-XX.grafana.net/api/prom/push"
export K6_PROMETHEUS_RW_USERNAME="YOUR_STACK_ID"
export K6_PROMETHEUS_RW_PASSWORD="YOUR_API_TOKEN"

# Run k6 with Prometheus output
k6 run --out experimental-prometheus-rw k6/agest_smoke.js
```

Or in one line:

```bash
K6_PROMETHEUS_RW_SERVER_URL="https://..." \
K6_PROMETHEUS_RW_USERNAME="123456" \
K6_PROMETHEUS_RW_PASSWORD="glc_xxx" \
k6 run --out experimental-prometheus-rw k6/agest_smoke.js
```

### Step 5: Add k6 Dashboard in Grafana

1. Log in to **Grafana Cloud** → https://grafana.com/auth/sign-in
2. Go to **Dashboards** → **New** → **Import**
3. Enter dashboard ID: **19665** (official k6 Prometheus dashboard)
4. Click **Load**
5. Select your **Prometheus** data source (Grafana Cloud Prometheus)
6. Click **Import**

You should see charts for:
- HTTP request duration (p95, p99)
- HTTP request rate
- Error rate
- VUs (virtual users)
- Checks pass/fail rate

**Note:** Data appears after you run k6 with `--out experimental-prometheus-rw`. Metrics may take 1–2 minutes to show.

### Step 6: Store Credentials and Use Helper Script

Your `.env` is already configured with the Grafana Cloud credentials. Run:

```bash
./scripts/k6_grafana.sh                    # runs agest_smoke.js
./scripts/k6_grafana.sh k6/agest_load.js   # runs load test
# Windows: scripts\k6_grafana.bat [script.js]
```

To set up manually, create `.env` (ensure it's in `.gitignore`):

```
K6_PROMETHEUS_RW_SERVER_URL=https://prometheus-prod-XX-XX.grafana.net/api/prom/push
K6_PROMETHEUS_RW_USERNAME=123456
K6_PROMETHEUS_RW_PASSWORD=glc_xxxxxxxxxxxx
```

Or run manually:
```bash
source .env && k6 run --out experimental-prometheus-rw k6/agest_smoke.js
```

---

## Part 2: Allure Reports for pytest

### Step 1: Install Allure

**macOS (Homebrew):**

```bash
brew install allure
```

**Or download manually:**

1. Go to **https://github.com/allure-framework/allure2/releases**
2. Download the latest `allure-2.x.x.tgz`
3. Extract and add `bin/` to your PATH

**Verify:**

```bash
allure --version
```

### Step 2: Install allure-pytest

```bash
pip install allure-pytest
```

### Step 3: Run pytest with Allure

```bash
# Run tests and generate Allure results
pytest tests/ --alluredir=allure-results

# Open report (starts local server)
allure serve allure-results
```

### Step 4: Add Allure to pyproject.toml (Optional)

Add to `[tool.pytest.ini_options]`:

```ini
addopts = "-v --tb=short --alluredir=allure-results"
```

Then a plain `pytest` will write Allure results.

### Step 5: Generate Static HTML Report

```bash
# Generate report to a folder
allure generate allure-results -o allure-report --clean

# Open the report (opens index.html in browser)
allure open allure-report
```

### Step 6: Attach Playwright Screenshots on Failure

pytest-playwright can capture screenshots. To attach them to Allure, add a conftest hook:

```python
# In tests/conftest.py
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        if hasattr(item, "funcargs") and "page" in item.funcargs:
            page = item.funcargs["page"]
            try:
                screenshot = page.screenshot()
                allure.attach(screenshot, name="failure", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass
```

### Step 7: Add Allure Categories (Optional)

Create `allure-results/categories.json` or configure in `allure.properties`:

```json
[
  {"name": "UI failures", "matchedStatuses": ["failed"], "messageRegex": ".*"},
  {"name": "API failures", "matchedStatuses": ["failed"], "traceRegex": ".*httpx.*"}
]
```

---

## Quick Reference

### Grafana Cloud + k6

```bash
# One-time: set credentials
export K6_PROMETHEUS_RW_SERVER_URL="https://..."
export K6_PROMETHEUS_RW_USERNAME="..."
export K6_PROMETHEUS_RW_PASSWORD="..."

# Run and push to Grafana
k6 run --out experimental-prometheus-rw k6/agest_smoke.js
```

### Allure

```bash
# Run tests
pytest tests/ --alluredir=allure-results

# View report
allure serve allure-results

# Or generate static report
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## Resources

- [Grafana Cloud k6](https://grafana.com/docs/grafana-cloud/testing/k6/)
- [k6 Prometheus remote write](https://grafana.com/docs/k6/latest/results-output/real-time/prometheus-remote-write/)
- [k6 Prometheus dashboard (19665)](https://grafana.com/grafana/dashboards/19665-k6-prometheus/)
- [Allure pytest](https://docs.qameta.io/allure/#_pytest)
- [Allure CLI](https://docs.qameta.io/allure/#_commandline)
