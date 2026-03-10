"""Home page object for https://www.agest.vn."""

from playwright.sync_api import Page

from src.pages.base import BasePage


class HomePage(BasePage):
    """AGEST Vietnam homepage - Driving Innovation through Technology."""

    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)

    # Locators - use resilient selectors (CSS + text) for headless compatibility
    @property
    def heading_main(self):
        # Fallback: h1 or role-based (some environments render differently)
        return self.page.locator("h1").filter(has_text="Driving Innovation").first

    def accept_cookies_if_present(self) -> None:
        """Accept cookie banner if visible (reduces overlay blocking content)."""
        for btn_name in ("Accept cookies", "Accept All"):
            try:
                btn = self.page.get_by_role("button", name=btn_name)
                btn.wait_for(state="visible", timeout=3000)
                btn.click()
                return
            except Exception:
                continue

    @property
    def link_contact(self):
        return self.page.locator('a:has-text("Get in Touch")').first

    @property
    def link_contact_footer(self):
        return self.page.locator('a:has-text("Get In Touch")').first

    @property
    def section_services(self):
        return self.page.locator("h2").filter(has_text="Our Services").first

    def link_service(self, name: str):
        """Get link for a service by name (e.g. Software Engineering, Software Testing)."""
        return self.page.get_by_role("link", name=name)

    def link_read_more(self, service: str):
        """Get Read More link for a service section."""
        return self.page.locator(f"text={service}").locator("..").get_by_role("link", name="Read More")

    def open_contact(self) -> None:
        """Click Get in Touch to open contact page."""
        self.link_contact.first.click()
