╰─➤  pytest tests/ui/ -v
============================== test session starts ===============================
platform darwin -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0 -- /Users/dthuynh/Documents/Personal/source/AutoTest-GenerativeAI/.venv/bin/python3.14
cachedir: .pytest_cache
rootdir: /Users/dthuynh/Documents/Personal/source/AutoTest-GenerativeAI
configfile: pyproject.toml
plugins: anyio-4.12.1, playwright-0.7.2, xdist-3.8.0, base-url-2.1.0
collected 13 items                                                               

tests/ui/test_home_smoke.py::test_homepage_loads[chromium] PASSED          [  7%]
tests/ui/test_home_smoke.py::test_contact_link_visible[chromium] PASSED    [ 15%]
tests/ui/test_home_smoke.py::test_services_section_present[chromium] PASSED [ 23%]
tests/ui/test_home_smoke.py::test_navigate_to_contact[chromium] PASSED     [ 30%]
tests/ui/test_pages_navigation.py::test_navigate_to_case_studies[chromium] FAILED [ 38%]
tests/ui/test_pages_navigation.py::test_case_studies_page_direct[chromium] PASSED [ 46%]
tests/ui/test_pages_navigation.py::test_navigate_to_about_us[chromium] FAILED [ 53%]
tests/ui/test_pages_navigation.py::test_about_page_direct[chromium] PASSED [ 61%]
tests/ui/test_services_navigation.py::test_service_page_loads[chromium-software-engineering-services/software-engineering] PASSED [ 69%]
tests/ui/test_services_navigation.py::test_service_page_loads[chromium-software-testing-services/software-testing] PASSED [ 76%]
tests/ui/test_services_navigation.py::test_service_page_loads[chromium-big-data-and-ai-services/big-data-and-ai] PASSED [ 84%]
tests/ui/test_services_navigation.py::test_service_page_loads[chromium-devops-and-cloud-services/devops-and-cloud] PASSED [ 92%]
tests/ui/test_services_navigation.py::test_service_page_loads[chromium-cyber-security-services/cyber-security] PASSED [100%]

==================================== FAILURES ====================================
____________________ test_navigate_to_case_studies[chromium] _____________________
tests/ui/test_pages_navigation.py:30: in test_navigate_to_case_studies
    case_page.heading_main.wait_for(state="visible", timeout=PAGE_TIMEOUT)
.venv/lib/python3.14/site-packages/playwright/sync_api/_generated.py:18074: in wait_for
    self._sync(self._impl_obj.wait_for(timeout=timeout, state=state))
.venv/lib/python3.14/site-packages/playwright/_impl/_locator.py:710: in wait_for
    await self._frame.wait_for_selector(
.venv/lib/python3.14/site-packages/playwright/_impl/_frame.py:369: in wait_for_selector
    await self._channel.send(
.venv/lib/python3.14/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
.venv/lib/python3.14/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("h1").filter(has_text="Case Studies").first to be visible
______________________ test_navigate_to_about_us[chromium] _______________________
tests/ui/test_pages_navigation.py:53: in test_navigate_to_about_us
    about_page.heading_main.wait_for(state="visible", timeout=PAGE_TIMEOUT)
.venv/lib/python3.14/site-packages/playwright/sync_api/_generated.py:18074: in wait_for
    self._sync(self._impl_obj.wait_for(timeout=timeout, state=state))
.venv/lib/python3.14/site-packages/playwright/_impl/_locator.py:710: in wait_for
    await self._frame.wait_for_selector(
.venv/lib/python3.14/site-packages/playwright/_impl/_frame.py:369: in wait_for_selector
    await self._channel.send(
.venv/lib/python3.14/site-packages/playwright/_impl/_connection.py:69: in send
    return await self._connection.wrap_api_call(
.venv/lib/python3.14/site-packages/playwright/_impl/_connection.py:559: in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
E   playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 30000ms exceeded.
E   Call log:
E     - waiting for locator("h1").filter(has_text="Delivering Quality").first to be visible
============================ short test summary info =============================
FAILED tests/ui/test_pages_navigation.py::test_navigate_to_case_studies[chromium] - playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("h1").filter(has_text="Case Studies").first to be visible
FAILED tests/ui/test_pages_navigation.py::test_navigate_to_about_us[chromium] - playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("h1").filter(has_text="Delivering Quality").first to be visible
==================== 2 failed, 11 passed in 100.80s (0:01:40) ====================