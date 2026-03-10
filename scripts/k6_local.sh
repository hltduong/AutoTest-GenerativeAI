#!/usr/bin/env bash
# Run k6 with local Prometheus (Docker).
# Start stack first: docker compose -f docker/docker-compose.yml up -d

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

PROMETHEUS_URL="${K6_PROMETHEUS_RW_SERVER_URL:-http://localhost:9090/api/v1/write}"

# Unset Grafana Cloud auth for local (no username/password)
unset K6_PROMETHEUS_RW_USERNAME
unset K6_PROMETHEUS_RW_PASSWORD

SCRIPT="${1:-k6/agest_smoke.js}"
echo "Running k6 with local Prometheus: $SCRIPT"
echo "Prometheus: $PROMETHEUS_URL"
K6_PROMETHEUS_RW_SERVER_URL="$PROMETHEUS_URL" k6 run --out experimental-prometheus-rw "$SCRIPT"
