"""This section contains the basic steps for running footer tests"""
from pages.base_page import BasePage
from locators.footer_page_locators import FooterPageLocators


class FooterPage(BasePage):
    footer_locators = FooterPageLocators()

    def check_footer_presence(self):
        """Checks Footer is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.FOOTER_SECTION)
