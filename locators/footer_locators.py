"""This section contains footer locators"""

from selenium.webdriver.common.by import By


class FooterLocators:
    FOOTER_SECTION = (By.CSS_SELECTOR, "#footer-website")
    PRODUCT_COLLECTIONS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(1)")
    SUBSCRIPTION_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(2)")
    TECHNOLOGIES_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(1)")
    TERMS_AND_CONDITIONS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(2)")
