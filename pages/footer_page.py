"""This section contains the basic steps for running footer tests"""
from pages.base_page import BasePage
from locators.footer_locators import FooterLocators


class FooterPage(BasePage):
    footer_locators = FooterLocators()
