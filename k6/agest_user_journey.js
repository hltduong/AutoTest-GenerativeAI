// k6 user journey: Home -> Services -> Contact
// Simulates a typical visitor flow
// Run: k6 run k6/agest_user_journey.js

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 3,
  duration: '45s',
  thresholds: {
    http_req_duration: ['p(95)<4000'],
    http_req_failed: ['rate<0.03'],
    checks: ['rate>0.98'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://www.agest.vn';

export default function () {
  // Step 1: Visit homepage
  let res = http.get(`${BASE_URL}/`);
  check(res, { 'homepage ok': (r) => r.status === 200 });
  sleep(1);

  // Step 2: Browse a service page
  const services = [
    '/services/software-testing',
    '/services/software-engineering',
    '/services/big-data-and-ai',
  ];
  const service = services[__VU % services.length];
  res = http.get(`${BASE_URL}${service}`);
  check(res, { 'service page ok': (r) => r.status === 200 });
  sleep(1);

  // Step 3: Visit contact page
  res = http.get(`${BASE_URL}/contact-us`);
  check(res, { 'contact page ok': (r) => r.status === 200 });
  sleep(1);
}
