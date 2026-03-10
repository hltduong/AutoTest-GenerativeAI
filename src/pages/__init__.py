"""Page objects for agest.vn."""

from src.pages.base import BasePage
from src.pages.home_page import HomePage
from src.pages.services_page import ServicesPage, SERVICE_PATHS
from src.pages.contact_page import ContactPage
from src.pages.case_studies_page import CaseStudiesPage
from src.pages.about_page import AboutPage

__all__ = [
    "BasePage",
    "HomePage",
    "ServicesPage",
    "ContactPage",
    "CaseStudiesPage",
    "AboutPage",
    "SERVICE_PATHS",
]
