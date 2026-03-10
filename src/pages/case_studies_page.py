"""Case Studies page object for https://www.agest.vn/case-studies."""

from playwright.sync_api import Page

from src.pages.base import BasePage


class CaseStudiesPage(BasePage):
    """AGEST Vietnam Case Studies page."""

    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)

    @property
    def heading_main(self):
        return self.page.locator("h1").filter(has_text="Case Studies").first

    @property
    def link_more_case_studies(self):
        return self.page.locator('a:has-text("Read More")').first
