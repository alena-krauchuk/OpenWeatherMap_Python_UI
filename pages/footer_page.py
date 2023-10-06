"""This section contains the basic steps for running footer tests"""
from pages.base_page import BasePage
from locators.footer_locators import FooterLocators


class FooterPage(BasePage):
    footer_locators = FooterLocators()

    def check_footer_presence(self):
        """Checks Footer is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.FOOTER_SECTION)
