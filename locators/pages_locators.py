"""This section contains locators for titles of pages and sections on pages"""

from selenium.webdriver.common.by import By


class PagesAndSectionsTitlesLocators:
    CURRENT_AND_FORECAST_WEATHER_DATA_COLLECTION_TITLE = (By.CSS_SELECTOR, "#current h2")

