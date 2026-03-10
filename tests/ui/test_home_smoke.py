"""Smoke tests for agest.vn homepage."""

import pytest

from src.pages.home_page import HomePage

# Increased timeout for slow-loading pages (agest.vn can be slow)
PAGE_TIMEOUT = 30_000

# Reduce headless detection: real viewport + user agent
pytestmark = pytest.mark.browser_context_args(
    viewport={"width": 1280, "height": 720},
    user_agent=(
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
)


@pytest.mark.ui
@pytest.mark.smoke
def test_homepage_loads(home_page: HomePage) -> None:
    """Homepage loads and shows main heading."""
    home_page.navigate("")
    home_page.accept_cookies_if_present()
    home_page.heading_main.wait_for(state="visible", timeout=PAGE_TIMEOUT)


@pytest.mark.ui
@pytest.mark.smoke
def test_contact_link_visible(home_page: HomePage) -> None:
    """Get in Touch link is visible on homepage."""
    home_page.navigate("")
    home_page.accept_cookies_if_present()
    home_page.link_contact.first.wait_for(state="visible", timeout=PAGE_TIMEOUT)


@pytest.mark.ui
@pytest.mark.smoke
def test_services_section_present(home_page: HomePage) -> None:
    """Our Services section is present."""
    home_page.navigate("")
    home_page.accept_cookies_if_present()
    home_page.section_services.wait_for(state="visible", timeout=PAGE_TIMEOUT)


@pytest.mark.ui
@pytest.mark.smoke
def test_navigate_to_contact(home_page: HomePage, base_url: str) -> None:
    """Click Get in Touch navigates to contact page."""
    home_page.navigate("")
    home_page.accept_cookies_if_present()
    home_page.open_contact()
    home_page.page.wait_for_url(f"{base_url}/contact-us*", timeout=PAGE_TIMEOUT)
