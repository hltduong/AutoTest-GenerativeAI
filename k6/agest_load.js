// k6 load test with ramp-up for agest.vn
// Stages: 0-30s ramp to 10 VUs, 30-90s sustain, 90-120s ramp down
// Run: k6 run k6/agest_load.js

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '1m', target: 10 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<5000', 'p(99)<8000'],
    http_req_failed: ['rate<0.05'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://www.agest.vn';

export default function () {
  const res = http.get(`${BASE_URL}/`);
  check(res, { 'status 200': (r) => r.status === 200 });
  sleep(1);
}
