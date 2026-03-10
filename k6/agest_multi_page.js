// k6 multi-page load test for agest.vn
// Tests key pages: home, contact, about, case-studies, services
// Run: k6 run k6/agest_multi_page.js

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 5,
  duration: '1m',
  thresholds: {
    http_req_duration: ['p(95)<5000'],
    http_req_failed: ['rate<0.05'],
    checks: ['rate>0.95'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://www.agest.vn';

const PAGES = [
  '/',
  '/contact-us',
  '/about-us',
  '/case-studies',
  '/services/software-engineering',
  '/services/software-testing',
  '/services/big-data-and-ai',
];

export default function () {
  for (const path of PAGES) {
    const res = http.get(`${BASE_URL}${path}`);
    check(res, {
      [`${path} status 200`]: (r) => r.status === 200,
    });
    sleep(0.5);
  }
  sleep(1);
}
