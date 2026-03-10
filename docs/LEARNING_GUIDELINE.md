# Learning Guideline – AutoTest-GenerativeAI

Ideas for extending this project for learning purposes. Pick one area and iterate.

---

## 1. AI / Generative AI (fits project name)

The project is "AI-driven" but has no AI integration yet. Good starting points:

- **AI-generated test cases from requirements** – Extend the requirement parser output with OpenAI/Anthropic to generate pytest test skeletons from user stories.
- **Test data generation** – Use an LLM to generate realistic test data (names, emails, etc.).
- **Failure explanation** – On test failure, send error summary to an LLM and attach a human-readable explanation to the Allure report.

---

## 2. API Testing

- Add more API tests beyond the health check (e.g. services, contact endpoints).
- Add OpenAPI schema validation if a spec exists.
- Add negative tests (404, 500, invalid payloads).

---

## 3. Pytest & Framework

- Add a custom pytest plugin (e.g. custom markers, hooks).
- Add environment-specific config (dev/staging/prod) via `.env`.
- Add more parametrized tests (multiple URLs, locales).
- Add retries for flaky tests (`pytest-rerunfailures`).

---

## 4. CI/CD

- Add a GitHub Actions workflow that runs pytest, k6, and generates Allure reports as artifacts.

---

## 5. Documentation & Learning

- Add inline comments in key files (`requirement_parser.py`, `conftest.py`) explaining design choices.
- Add step-by-step exercises (e.g. "Add a new page object", "Write your first API test").

---

## 6. Visual & Performance

- Add Playwright visual regression (screenshot comparison).
- Add performance assertions in pytest (e.g. response time thresholds).
- Add more k6 scenarios (stress, spike tests).

---

## Quick Start by Goal

| Goal              | First step                                                                 |
|-------------------|----------------------------------------------------------------------------|
| Learn AI testing  | Add `openai` dependency and a small module that generates one test from a requirement. |
| Learn pytest      | Add a custom marker or plugin, or extend the requirement parser.           |
| Learn CI/CD       | Add a basic GitHub Actions workflow that runs `pytest` and `k6`.          |
| Learn API testing | Add 2–3 API tests for real agest.vn endpoints.                             |

---

## Project Structure Reference

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
├── k6/               # Performance scripts
└── docs/             # Setup guides, this guideline
```
