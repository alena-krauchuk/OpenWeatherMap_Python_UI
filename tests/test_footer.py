import pytest
from pages.footer_page import FooterPage
from locators.footer_locators import FooterLocators
from data.data_urls import url_main_page


class TestFooter:
    footer_locators = FooterLocators()

    def test_tc_01_01_01_check_presence_of_footer_on_pages(self, driver):
        """Checks if the footer is present in the DOM tree"""
        page = FooterPage(driver, url_main_page)
        page.open()
        assert page.element_is_visible(self.footer_locators.FOOTER_SECTION)

