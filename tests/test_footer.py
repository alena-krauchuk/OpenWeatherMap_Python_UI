import pytest
from pages.footer_page import FooterPage


class TestFooter:

    def test_tc_01_01_01_check_presence_of_footer_on_pages(self, driver):
        """Checks if the footer is present in the DOM tree"""
        page = FooterPage(driver)
        page.open()
        footer_section = page.check_footer_presence()
        assert footer_section, "Footer is not present in the DOM tree"
