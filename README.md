# AutoTest for AGEST Vietnam (agest.vn)

AI-driven test automation following the [AI Testing Learning Path](ai_testing_learning_path.pdf): **Python + pytest + Playwright + OpenAI + k6 + Grafana**.

## Stack

- **Functional automation**: Python + pytest + Playwright
- **API testing**: httpx
- **Target site**: https://www.agest.vn

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run Tests

```bash
# All tests
pytest

# Smoke only
pytest -m smoke

# UI only
pytest -m ui

# API only
pytest -m api

# Parallel (pytest-xdist)
pytest -n auto

# Run without UI tests (if Chromium fails in sandbox)
pytest -m "not ui"
```

## Project Structure

```
├── config/           # Settings, env
├── src/
│   ├── pages/        # Playwright page objects (POM)
│   ├── clients/      # API clients
│   ├── models/       # Pydantic schemas
│   └── parsers/      # Requirement parser (Week 1)
├── tests/
│   ├── api/          # API smoke tests
│   ├── ui/           # Playwright UI tests
│   └── unit/         # Parser/model tests
└── k6/               # Performance scripts (Week 8+)
```

## k6 Performance Tests

```bash
# Smoke (2 VUs, 30s)
k6 run k6/agest_smoke.js

# Multi-page (5 VUs, 1m) - home, contact, about, case-studies, services
k6 run k6/agest_multi_page.js

# User journey (3 VUs, 45s) - home → service → contact
k6 run k6/agest_user_journey.js

# Load test (ramp 0→10 VUs, sustain, ramp down)
k6 run k6/agest_load.js

# Override base URL
BASE_URL=https://staging.agest.vn k6 run k6/agest_smoke.js
```

## Requirement Parser (Week 1)

```bash
python -m src.parsers.requirement_parser requirements/sample.txt
```

## Learning Path Alignment

| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Python foundations | ✅ Requirement parser, venv, JSON output |
| 2 | Pytest core | ✅ Markers, fixtures, parametrization |
| 3 | API automation | ✅ httpx client, smoke tests |
| 4 | Playwright basics | ✅ UI smoke, page objects |
| 5 | Framework architecture | ✅ pages/, clients/, config/ layout |
