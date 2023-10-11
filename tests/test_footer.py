import pytest
from pages.footer_page import FooterPage
from locators.footer_locators import FooterLocators
from data.data_urls import URL_MAIN_PAGE


class TestFooter:
    footer_locators = FooterLocators()

    class TestFooterPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_01_check_presence_of_footer(self, driver):
            """Checks if the footer is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.FOOTER_SECTION)

        def test_tc_01_02_01_check_presence_of_product_collections_section(self, driver):
            """Checks if the Product Collections section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.PRODUCT_COLLECTIONS_SECTION)

    class TestFooterVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_01_02_check_visibility_of_footer(self, driver):
            """Checks if the footer is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.FOOTER_SECTION)
