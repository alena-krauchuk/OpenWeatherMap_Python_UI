import pytest
from pages.footer_page import FooterPage
from locators.footer_locators import FooterLocators
from data.data_urls import URL_MAIN_PAGE


class TestFooter:
    footer_locators = FooterLocators()

    def test_tc_01_01_01_check_presence_of_footer(self, driver):
        """Checks if the footer is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.FOOTER_SECTION)

    def test_tc_01_01_02_check_visibility_of_footer(self, driver):
        """Checks if the footer is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.FOOTER_SECTION)

