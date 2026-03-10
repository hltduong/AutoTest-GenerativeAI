test result

1st:
╰─➤  pytest tests/ui/test_home_smoke.py -v
============================== test session starts ===============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0 -- /Users/dthuynh/Documents/Personal/source/AutoTest-GenerativeAI/.venv/bin/python3.14
cachedir: .pytest_cache
rootdir: /Users/dthuynh/Documents/Personal/source/AutoTest-GenerativeAI
configfile: pyproject.toml
plugins: anyio-4.12.1, playwright-0.7.2, xdist-3.8.0, base-url-2.1.0
collected 4 items                                                                

tests/ui/test_home_smoke.py::test_homepage_loads[chromium] PASSED          [ 25%]
tests/ui/test_home_smoke.py::test_contact_link_visible[chromium] PASSED    [ 50%]
tests/ui/test_home_smoke.py::test_services_section_present[chromium] PASSED [ 75%]
tests/ui/test_home_smoke.py::test_navigate_to_contact[chromium] PASSED     [100%]

=============================== 4 passed in 12.67s ===============================


2nd:
╰─➤  k6 run k6/agest_smoke.js                                                99 ↵

         /\      Grafana   /‾‾/  
    /\  /  \     |\  __   /  /   
   /  \/    \    | |/ /  /   ‾‾\ 
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/ 


     execution: local
        script: k6/agest_smoke.js
        output: -

     scenarios: (100.00%) 1 scenario, 2 max VUs, 1m0s max duration (incl. graceful stop):
              * default: 2 looping VUs for 30s (gracefulStop: 30s)



  █ THRESHOLDS 

    http_req_duration
    ✓ 'p(95)<3000' p(95)=1.76s

    http_req_failed
    ✓ 'rate<0.05' rate=0.00%


  █ TOTAL RESULTS 

    checks_total.......: 31      1.004986/s
    checks_succeeded...: 100.00% 31 out of 31
    checks_failed......: 0.00%   0 out of 31

    ✓ status is 200

    HTTP
    http_req_duration..............: avg=958.62ms min=376.72ms med=860.99ms max=1.91s p(90)=1.63s p(95)=1.76s
      { expected_response:true }...: avg=958.62ms min=376.72ms med=860.99ms max=1.91s p(90)=1.63s p(95)=1.76s
    http_req_failed................: 0.00%  0 out of 31
    http_reqs......................: 31     1.004986/s

    EXECUTION
    iteration_duration.............: avg=1.96s    min=1.37s    med=1.86s    max=3.03s p(90)=2.63s p(95)=2.81s
    iterations.....................: 31     1.004986/s
    vus............................: 2      min=2       max=2
    vus_max........................: 2      min=2       max=2

    NETWORK
    data_received..................: 9.6 MB 312 kB/s
    data_sent......................: 37 kB  1.2 kB/s




running (0m30.8s), 0/2 VUs, 31 complete and 0 interrupted iterations
default ✓ [======================================] 2 VUs  30s