// k6 smoke test for agest.vn (Week 8+)
// Run: k6 run k6/agest_smoke.js

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 2,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<3000'],
    http_req_failed: ['rate<0.05'],  // 5% - relaxed for intermittent network/site issues
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://www.agest.vn';

export default function () {
  const res = http.get(`${BASE_URL}/`);
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);
}
