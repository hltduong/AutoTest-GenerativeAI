"""Tests for services navigation on agest.vn."""

import pytest

from src.pages.services_page import ServicesPage, SERVICE_PATHS


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.parametrize("service_key,path", list(SERVICE_PATHS.items()))
def test_service_page_loads(page, base_url: str, service_key: str, path: str) -> None:
    """Each service page loads successfully."""
    services_page = ServicesPage(page, base_url, path)
    services_page.navigate_to_service()
    page.wait_for_load_state("domcontentloaded")
    assert page.url.startswith(f"{base_url}/services/")
