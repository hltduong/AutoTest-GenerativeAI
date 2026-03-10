#!/usr/bin/env bash
# Run k6 with Grafana Cloud Prometheus remote write.
# Set env vars in .env or export before running:
#   K6_PROMETHEUS_RW_SERVER_URL
#   K6_PROMETHEUS_RW_USERNAME
#   K6_PROMETHEUS_RW_PASSWORD

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

if [ -f .env ]; then
  set -a
  source .env
  set +a
  export K6_PROMETHEUS_RW_SERVER_URL
  export K6_PROMETHEUS_RW_USERNAME
  export K6_PROMETHEUS_RW_PASSWORD
fi

if [ -z "$K6_PROMETHEUS_RW_SERVER_URL" ]; then
  echo "Error: K6_PROMETHEUS_RW_SERVER_URL not set. Add to .env or export."
  exit 1
fi

SCRIPT="${1:-k6/agest_smoke.js}"
echo "Running k6 with Grafana Cloud: $SCRIPT"
k6 run --out experimental-prometheus-rw "$SCRIPT"
