@echo off
REM Run k6 with local Prometheus (Docker).
REM Start stack first: docker compose -f docker/docker-compose.yml up -d

setlocal
cd /d "%~dp0.."

set "PROMETHEUS_URL=%K6_PROMETHEUS_RW_SERVER_URL%"
if "%PROMETHEUS_URL%"=="" set "PROMETHEUS_URL=http://localhost:9090/api/v1/write"

REM Unset Grafana Cloud auth for local (no username/password)
set "K6_PROMETHEUS_RW_USERNAME="
set "K6_PROMETHEUS_RW_PASSWORD="
set "K6_PROMETHEUS_RW_SERVER_URL=%PROMETHEUS_URL%"

set "SCRIPT=%~1"
if "%SCRIPT%"=="" set "SCRIPT=k6/agest_smoke.js"

echo Running k6 with local Prometheus: %SCRIPT%
echo Prometheus: %PROMETHEUS_URL%
k6 run --out experimental-prometheus-rw "%SCRIPT%"
