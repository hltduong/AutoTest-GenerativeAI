"""Pytest fixtures for agest.vn automation."""

import pytest

from config.settings import BASE_URL

# Allure: attach Playwright screenshot on UI test failure
try:
    import allure

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item):
        outcome = yield
        rep = outcome.get_result()
        if rep.when == "call" and rep.failed and "page" in item.fixturenames:
            try:
                page = item.funcargs.get("page")
                if page:
                    screenshot = page.screenshot()
                    allure.attach(
                        screenshot,
                        name="failure-screenshot",
                        attachment_type=allure.attachment_type.PNG,
                    )
            except Exception:
                pass
except ImportError:
    pass
from src.clients.agest_client import AgestClient
from src.pages.home_page import HomePage
from src.pages.contact_page import ContactPage
from src.pages.services_page import ServicesPage, SERVICE_PATHS
from src.pages.case_studies_page import CaseStudiesPage
from src.pages.about_page import AboutPage


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for agest.vn."""
    return BASE_URL


@pytest.fixture
def api_client(base_url: str) -> AgestClient:
    """Reusable API client."""
    return AgestClient(base_url=base_url)


# Playwright fixtures are provided by pytest-playwright
# page, browser, context, etc. are available automatically

@pytest.fixture
def home_page(page, base_url: str) -> HomePage:
    """Home page object for agest.vn."""
    return HomePage(page, base_url)


@pytest.fixture
def contact_page(page, base_url: str) -> ContactPage:
    """Contact page object."""
    return ContactPage(page, base_url)


@pytest.fixture(params=list(SERVICE_PATHS.values()))
def service_path(request) -> str:
    """Parametrized service path for data-driven tests."""
    return request.param


@pytest.fixture
def case_studies_page(page, base_url: str) -> CaseStudiesPage:
    """Case Studies page object."""
    return CaseStudiesPage(page, base_url)


@pytest.fixture
def about_page(page, base_url: str) -> AboutPage:
    """About Us page object."""
    return AboutPage(page, base_url)
