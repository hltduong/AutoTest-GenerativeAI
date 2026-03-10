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

    def accept_cookies_if_present(self) -> None:
        """Accept cookie banner if visible."""
        for btn_name in ("Accept cookies", "Accept All"):
            try:
                btn = self.page.get_by_role("button", name=btn_name)
                btn.wait_for(state="visible", timeout=3000)
                btn.click()
                return
            except Exception:
                continue
