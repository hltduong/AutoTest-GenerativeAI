"""API smoke tests for agest.vn."""

import pytest

from src.clients.agest_client import AgestClient


@pytest.mark.api
@pytest.mark.smoke
def test_site_reachable(api_client: AgestClient) -> None:
    """agest.vn homepage returns 200."""
    status, reason = api_client.health_check()
    assert status == 200, f"Expected 200, got {status}: {reason}"


@pytest.mark.api
@pytest.mark.smoke
def test_contact_page_reachable(api_client: AgestClient) -> None:
    """Contact page returns 200."""
    resp = api_client.get("/contact-us")
    assert resp.status_code == 200
