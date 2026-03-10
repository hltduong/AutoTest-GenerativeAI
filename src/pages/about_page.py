"""About Us page object for https://www.agest.vn/about-us."""

from playwright.sync_api import Page

from src.pages.base import BasePage


class AboutPage(BasePage):
    """AGEST Vietnam About Us page."""

    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)

    @property
    def heading_main(self):
        return self.page.locator("h1").filter(has_text="Delivering Quality").first
