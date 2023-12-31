from pages.footer_page import FooterPage
from locators.common_locators import CookiesPanelLocators
from data.data_urls import URL_MAIN_PAGE


class TestCookiesPanelPresence:
    cookies_panel_locators = CookiesPanelLocators()

    def test_tc_02_01_01_check_presence_of_cookies_panel(self, driver):
        """Checks if the cookies panel is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.cookies_panel_locators.COOKIES_PANEL), \
            "The cookies panel is not present in the DOM tree"

    def test_tc_02_01_02_check_presence_of_cookies_panel_description(self, driver):
        """Checks if the cookies panel description is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.cookies_panel_locators.COOKIES_PANEL_DESCRIPTION), \
            "The cookies panel description is not present in the DOM tree"

    def test_tc_02_01_03_check_presence_of_button_allow_all(self, driver):
        """Checks if the Allow all button on cookies panel is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.cookies_panel_locators.ALLOW_ALL_BUTTON), \
            "The Allow all button on cookies panel is not present in the DOM tree"

    def test_tc_02_01_04_check_presence_of_manage_cookies_link(self, driver):
        """Checks if the Manage cookies link on cookies panel is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.cookies_panel_locators.MANAGE_COOKIES_LINK), \
            "The Manage cookies link on cookies panel is not present in the DOM tree"


class TestCookiesPanelVisibility:
    cookies_panel_locators = CookiesPanelLocators()

    def test_tc_02_02_01_check_visibility_of_cookies_panel(self, driver):
        """Checks if the cookies panel is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.cookies_panel_locators.COOKIES_PANEL), \
            "The cookies panel is invisible on the Main Page"

    def test_tc_02_02_02_check_visibility_of_cookies_panel_description(self, driver):
        """Checks if the cookies panel description is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.cookies_panel_locators.COOKIES_PANEL_DESCRIPTION), \
            "The cookies panel description is invisible on the Main Page"

    def test_tc_02_02_03_check_visibility_of_allow_all_button(self, driver):
        """Checks if the button Allow all on cookies panel is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.cookies_panel_locators.ALLOW_ALL_BUTTON), \
            "The button Allow all on cookies panel is invisible on the Main Page"

    def test_tc_02_02_04_check_presence_of_manage_cookies_link(self, driver):
        """Checks if the Manage cookies link on cookies panel is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.cookies_panel_locators.MANAGE_COOKIES_LINK), \
            "The Manage cookies link on cookies panel is invisible on the Main Page"
