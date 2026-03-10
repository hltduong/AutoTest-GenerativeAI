"""Contact page object for https://www.agest.vn/contact-us."""

from playwright.sync_api import Page

from src.pages.base import BasePage


class ContactPage(BasePage):
    """AGEST Vietnam contact page."""

    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)

    def navigate_to_contact(self) -> None:
        """Navigate to contact page."""
        self.navigate("contact-us")
