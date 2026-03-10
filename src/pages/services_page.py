"""Services page object for agest.vn/services/*."""

from playwright.sync_api import Page

from src.pages.base import BasePage


class ServicesPage(BasePage):
    """Base for service detail pages (Software Engineering, Software Testing, etc.)."""

    def __init__(self, page: Page, base_url: str, service_path: str) -> None:
        super().__init__(page, base_url)
        self.service_path = service_path

    def navigate_to_service(self) -> None:
        """Navigate to this service page."""
        self.navigate(self.service_path)


# Service paths from agest.vn
SERVICE_PATHS = {
    "software-engineering": "services/software-engineering",
    "software-testing": "services/software-testing",
    "big-data-and-ai": "services/big-data-and-ai",
    "devops-and-cloud": "services/devops-and-cloud",
    "cyber-security": "services/cyber-security",
}
