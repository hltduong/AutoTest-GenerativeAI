@echo off
REM Run k6 with Grafana Cloud Prometheus remote write.
REM Set env vars in .env or export before running:
REM   K6_PROMETHEUS_RW_SERVER_URL
REM   K6_PROMETHEUS_RW_USERNAME
REM   K6_PROMETHEUS_RW_PASSWORD

setlocal
cd /d "%~dp0.."

REM Load .env if present (skips lines starting with #)
if exist .env (
  for /f "usebackq eol=# tokens=1,* delims==" %%a in (".env") do set "%%a=%%b"
)

if "%K6_PROMETHEUS_RW_SERVER_URL%"=="" (
  echo Error: K6_PROMETHEUS_RW_SERVER_URL not set. Add to .env or set before running.
  exit /b 1
)

set "SCRIPT=%~1"
if "%SCRIPT%"=="" set "SCRIPT=k6/agest_smoke.js"

echo Running k6 with Grafana Cloud: %SCRIPT%
k6 run --out experimental-prometheus-rw "%SCRIPT%"
