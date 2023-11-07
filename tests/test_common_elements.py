from pages.footer_page import FooterPage
from locators.common_locators import CookiesPanelLocators
from data.data_urls import URL_MAIN_PAGE


class TestCookiesPanelPresence:
    footer_locators = CookiesPanelLocators()

    def test_tc_02_01_01_check_presence_of_cookies_panel(self, driver):
        """Checks if the cookies panel is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.COOKIES_PANEL), \
            "The cookies panel is not present in the DOM tree"
