"""This section contains locators for using on any page"""

from selenium.webdriver.common.by import By


class CookiesPanelLocators:
    ALLOW_ALL_BUTTON = (By.CSS_SELECTOR, "button.stick-footer-panel__link")
    COOKIES_PANEL = (By.CSS_SELECTOR, ".stick-footer-panel")
    COOKIES_PANEL_DESCRIPTION = (By.CSS_SELECTOR, ".stick-footer-panel p")
    MANAGE_COOKIES_LINK = (By.CSS_SELECTOR, "button.stick-footer-panel__link")
