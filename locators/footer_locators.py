"""This section contains footer locators"""

from selenium.webdriver.common.by import By


class FooterLocators:
    ABOUT_US_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(2) :nth-child(3) ul :nth-child(1) a")
    ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK = (By.CSS_SELECTOR,
                                                 "#footer-website div :nth-child(2) :nth-child(1) ul :nth-child(2) a")
    ASK_A_QUESTION_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(2) :nth-child(3) ul :nth-child(4) a")
    BLOG_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(2) :nth-child(3) ul :nth-child(2) a")
    COMPANY_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(3)")
    COMPANY_SECTION_TITLE = (By.CSS_SELECTOR, "#footer-website div :nth-child(1) :nth-child(3) > p")
    COMPANY_SECTION_CONTENT = (By.CSS_SELECTOR, "#footer-website div :nth-child(1) :nth-child(3) div")
    CONNECT_YOUR_WEATHER_STATION_LINK = (By.CSS_SELECTOR,
                                         "#footer-website div :nth-child(2) :nth-child(1) ul :nth-child(3) a")
    COPYRIGHT_ELEMENT_01 = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(4) > :nth-child(1) > :nth-child(1)")
    COPYRIGHT_ELEMENT_02 = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(4) > :nth-child(1) > :nth-child(3)")
    COPYRIGHT_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(4) > div:nth-child(1)")
    CURRENT_AND_FORECAST_APIS_LINK = (By.CSS_SELECTOR,
                                      "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(1) a")
    DOWNLOAD_OPENWEATHER_APP_SECTION = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(3) > :nth-child(1)")
    DOWNLOAD_OPENWEATHER_APP_SECTION_TITLE = (By.CSS_SELECTOR, "#footer-website > div :nth-child(3) > :nth-child(1) p")
    DOWNLOAD_ON_THE_APP_STORE_IMAGE = (By.CSS_SELECTOR,
                                       "#footer-website div :nth-child(3) :nth-child(1) :nth-child(2) :nth-child(1) img")
    DOWNLOAD_ON_THE_APP_STORE_LINK = (By.CSS_SELECTOR,
                                      "#footer-website > div > :nth-child(3) :nth-child(1) a:nth-child(1)")
    FACEBOOK_IMAGE = (By.CSS_SELECTOR, ".social > a:nth-child(1) img")
    FACEBOOK_LINK = (By.CSS_SELECTOR, ".social > a:nth-child(1)")
    FAQ_LINK = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(1) > div:nth-child(2) :nth-child(4) a")
    FOOTER_SECTION = (By.CSS_SELECTOR, "#footer-website")
    GET_IT_ON_GOOGLE_PLAY_IMAGE = (By.CSS_SELECTOR,
                                   "#footer-website div :nth-child(3) > :nth-child(1) :nth-child(2) :nth-child(2) img")
    GET_IT_ON_GOOGLE_PLAY_LINK = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(3) :nth-child(1) a:nth-child(2)")
    GITHUB_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(4) :nth-child(2) a:nth-child(6)")
    HISTORICAL_WEATHER_DATA_LINK = (By.CSS_SELECTOR,
                                    "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(2) a")
    HOW_TO_START_LINK = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(1) > div:nth-child(2) :nth-child(1) > a")
    LINKEDIN_IMAGE = (By.CSS_SELECTOR, ".social > a:nth-child(3) img")
    LINKEDIN_LINK = (By.CSS_SELECTOR, ".social > a:nth-child(3)")
    MEDIUM_IMAGE = (By.CSS_SELECTOR, ".social > a:nth-child(4) img")
    MEDIUM_LINK = (By.CSS_SELECTOR, ".social > a:nth-child(4)")
    OPENWEATHER_FOR_BUSINESS_LINK = (By.CSS_SELECTOR,
                                     "#footer-website div :nth-child(2) :nth-child(3) ul :nth-child(3) a")
    OUR_TECHNOLOGY_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(2) :nth-child(1) ul :nth-child(1) a")
    PRICING_LINK = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(1) > div:nth-child(2) :nth-child(2) > a")
    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "#footer-website > div > :nth-child(2) > :nth-child(2) ul :nth-child(2) a")
    PRODUCT_COLLECTIONS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(1)")
    PRODUCT_COLLECTIONS_SECTION_TITLE = (By.CSS_SELECTOR,
                                         "#footer-website > div > div:nth-child(1) > div:nth-child(1) p")
    RMETS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(3) > div:nth-child(2)")
    RMETS_SECTION_TITLE = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(3) > div:nth-child(2) p")
    RMETS_IMAGE = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(3) > div:nth-child(2) img")
    SINGLE_LINKS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(3)")
    SOCIAL_MEDIA_SECTION = (By.CSS_SELECTOR, "#footer-website div :nth-child(4) > :nth-child(2)")
    SUBSCRIBE_FOR_FREE_LINK = (By.CSS_SELECTOR,
                               "#footer-website > div > :nth-child(1) > div:nth-child(2) :nth-child(3) a")
    SUBSCRIPTION_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(2)")
    SUBSCRIPTION_SECTION_TITLE = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(1) > div:nth-child(2) p")
    TECHNOLOGIES_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(1)")
    TECHNOLOGIES_SECTION_TITLE = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(1) p")
    TELEGRAM_IMAGE = (By.CSS_SELECTOR, ".social > a:nth-child(5) img")
    TELEGRAM_LINK = (By.CSS_SELECTOR, ".social > a:nth-child(5)")
    TERMS_AND_CONDITIONS_OF_SALE_LINK = (By.CSS_SELECTOR,
                                         "#footer-website > div > :nth-child(2) > :nth-child(2) ul :nth-child(1) a")
    TERMS_AND_CONDITIONS_SECTION = (By.CSS_SELECTOR, "#footer-website > div > div:nth-child(2) > div:nth-child(2)")
    TERMS_AND_CONDITIONS_SECTION_TITLE = (By.CSS_SELECTOR,
                                          "#footer-website > div > div:nth-child(2) > div:nth-child(2) p")
    TWITTER_IMAGE = (By.CSS_SELECTOR, ".social > a:nth-child(2) img")
    TWITTER_LINK = (By.CSS_SELECTOR, ".social > a:nth-child(2)")
    WEATHER_DASHBOARD_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(4) a")
    WEATHER_MAPS_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(3) a")
    WEBSITE_TERMS_AND_CONDITIONS_LINK = (By.CSS_SELECTOR,
                                         "#footer-website > div > :nth-child(2) > :nth-child(2) ul :nth-child(3) a")
    WIDGETS_LINK = (By.CSS_SELECTOR, "#footer-website div :nth-child(1) :nth-child(1) ul :nth-child(5) a")
