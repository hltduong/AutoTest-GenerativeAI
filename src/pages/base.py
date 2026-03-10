"""Base page object for Playwright POM."""

from playwright.sync_api import Page


class BasePage:
    """Base class for all page objects."""

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def navigate(self, path: str = "") -> None:
        """Navigate to a path relative to base_url."""
        url = f"{self.base_url}/{path.lstrip('/')}" if path else self.base_url
        self.page.goto(url, wait_until="load", timeout=15_000)
