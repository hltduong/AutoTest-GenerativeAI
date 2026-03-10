"""UI tests for easy-to-access pages on agest.vn."""

import pytest

from src.pages.home_page import HomePage
from src.pages.case_studies_page import CaseStudiesPage
from src.pages.about_page import AboutPage

PAGE_TIMEOUT = 30_000

pytestmark = pytest.mark.browser_context_args(
    viewport={"width": 1280, "height": 720},
    user_agent=(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
)


@pytest.mark.ui
@pytest.mark.smoke
def test_navigate_to_case_studies(home_page: HomePage, base_url: str) -> None:
    """Homepage -> Case Studies link navigates to case-studies page."""
    home_page.navigate("")
    home_page.accept_cookies_if_present()
    home_page.link_case_studies.first.scroll_into_view_if_needed()
    home_page.link_case_studies.first.click()
    home_page.page.wait_for_url(f"{base_url}/case-studies*", timeout=PAGE_TIMEOUT)
    assert "/case-studies" in home_page.page.url


@pytest.mark.ui
@pytest.mark.smoke
def test_case_studies_page_direct(page, base_url: str) -> None:
    """Direct navigation to /case-studies loads Case Studies heading."""
    case_page = CaseStudiesPage(page, base_url)
    case_page.navigate("case-studies")
    case_page.accept_cookies_if_present()
    case_page.heading_main.wait_for(state="visible", timeout=PAGE_TIMEOUT)


@pytest.mark.ui
@pytest.mark.smoke
def test_navigate_to_about_us(home_page: HomePage, base_url: str) -> None:
    """Homepage -> About Us link navigates to about-us page."""
    home_page.navigate("")
    home_page.accept_cookies_if_present()
    home_page.link_about_us.first.scroll_into_view_if_needed()
    home_page.link_about_us.first.click()
    home_page.page.wait_for_url(f"{base_url}/about-us*", timeout=PAGE_TIMEOUT)
    assert "/about-us" in home_page.page.url


@pytest.mark.ui
@pytest.mark.smoke
def test_about_page_direct(page, base_url: str) -> None:
    """Direct navigation to /about-us loads About heading."""
    about_page = AboutPage(page, base_url)
    about_page.navigate("about-us")
    about_page.accept_cookies_if_present()
    about_page.heading_main.wait_for(state="visible", timeout=PAGE_TIMEOUT)
