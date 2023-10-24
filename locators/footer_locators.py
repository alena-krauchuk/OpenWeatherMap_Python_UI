"""This section contains footer locators"""

from selenium.webdriver.common.by import By


class FooterLocators:
    COMPANY_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(3)")
    COPYRIGHT_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(4) > div:nth-child(1)")
    CURRENT_AND_FORECAST_APIS_LINK = (By.CSS_SELECTOR,
                                      "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(1) > a")
    DOWNLOAD_OPENWEATHER_APP_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(3)")
    FAQ_LINK = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(1) > div:nth-child(2) :nth-child(4) > a")
    FOOTER_SECTION = (By.CSS_SELECTOR, "#footer-website")
    HISTORICAL_WEATHER_DATA_LINK = (By.CSS_SELECTOR,
                                    "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(2) > a")
    HOW_TO_START_LINK = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(1) > div:nth-child(2) :nth-child(1) > a")
    OUR_TECHNOLOGY_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(2) :nth-child(1) ul :nth-child(1) > a")
    PRICING_LINK = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(1) > div:nth-child(2) :nth-child(2) > a")
    PRODUCT_COLLECTIONS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(1)")
    PRODUCT_COLLECTIONS_SECTION_TITLE = (By.CSS_SELECTOR,
                                         "#footer-website > div > div:nth-child(1) > div:nth-child(1) p")
    RMETS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(3) > div:nth-child(2)")
    SINGLE_LINKS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(3)")
    SOCIAL_MEDIA_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(4) > div:nth-child(2)")
    SUBSCRIBE_FOR_FREE_LINK = (By.CSS_SELECTOR,
                               "#footer-website > div > :nth-child(1) > div:nth-child(2) :nth-child(3) > a")
    SUBSCRIPTION_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(2)")
    SUBSCRIPTION_SECTION_TITLE = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(2) p")
    TECHNOLOGIES_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(1)")
    TECHNOLOGIES_SECTION_TITLE = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(1) p")
    TERMS_AND_CONDITIONS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(2)")
    WEATHER_DASHBOARD_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(4) > a")
    WEATHER_MAPS_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(3) > a")
    WIDGETS_LINK = (By.CSS_SELECTOR, "#footer-website div:nth-child(1) > div:nth-child(1) li:nth-child(5) > a")
