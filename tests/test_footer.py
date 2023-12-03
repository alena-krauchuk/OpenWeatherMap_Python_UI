from pages.footer_page import FooterPage
from locators.footer_locators import FooterLocators
from data.data_urls import URL_MAIN_PAGE, FooterImageUrls
from data.footer_data import FooterElementsText


class TestFooterPresence:
    footer_locators = FooterLocators()

    def test_tc_01_01_01_check_presence_of_footer(self, driver):
        """Checks if the footer is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.FOOTER_SECTION), \
            "The footer is not present in the DOM tree"

    class TestFooterSectionsPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_02_check_presence_of_product_collections_section(self, driver):
            """Checks if the Product Collections section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.PRODUCT_COLLECTIONS_SECTION), \
                "The Product Collections section is not present in the DOM tree"

        def test_tc_01_01_03_check_presence_of_subscription_section(self, driver):
            """Checks if the Subscription section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.SUBSCRIPTION_SECTION), \
                "The Subscription section is not present in the DOM tree"

        def test_tc_01_01_04_check_presence_of_technologies_section(self, driver):
            """Checks if the Technologies section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.TECHNOLOGIES_SECTION), \
                "The Technologies section is not present in the DOM tree"

        def test_tc_01_01_05_check_presence_of_terms_and_conditions_section(self, driver):
            """Checks if the Terms and Conditions section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.TERMS_AND_CONDITIONS_SECTION), \
                "The Terms and Conditions section is not present in the DOM tree"

        def test_tc_01_01_06_check_presence_of_company_section(self, driver):
            """Checks if the Company section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.COMPANY_SECTION), \
                "The Company section is not present in the DOM tree"

        def test_tc_01_01_07_check_presence_of_single_links_section(self, driver):
            """Checks if the single links section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.SINGLE_LINKS_SECTION), \
                "The single links section is not present in the DOM tree"

        def test_tc_01_01_08_check_presence_of_download_openweather_app_section(self, driver):
            """Checks if the Download OpenWeather app section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.DOWNLOAD_OPENWEATHER_APP_SECTION), \
                "The Download OpenWeather app section is not present in the DOM tree"

        def test_tc_01_01_09_check_presence_of_rmets_section(self, driver):
            """Checks if the RMetS section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.RMETS_SECTION), \
                "The RMetS section is not present in the DOM tree"

        def test_tc_01_01_10_check_presence_of_copyright_section(self, driver):
            """Checks if the Copyright section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.COPYRIGHT_SECTION), \
                "The Copyright section is not present in the DOM tree"

        def test_tc_01_01_11_check_presence_of_social_media_section(self, driver):
            """Checks if the Social media section is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.SOCIAL_MEDIA_SECTION), \
                "The Social media section is not present in the DOM tree"

    class TestProductCollectionsSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_12_check_presence_of_product_collections_section_title(self, driver):
            """Checks if the Product Collections section's title is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.PRODUCT_COLLECTIONS_SECTION_TITLE), \
                "The Product Collections section's title is not present in the DOM tree"

        def test_tc_01_01_13_check_presence_of_current_and_forecast_apis_link(self, driver):
            """Checks if the Current and Forecast APIs link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK), \
                "The Current and Forecast APIs link is not present in the DOM tree"

        def test_tc_01_01_14_check_presence_of_historical_weather_data_link(self, driver):
            """Checks if the Historical Weather Data link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK), \
                "The Historical Weather Data link is not present in the DOM tree"

        def test_tc_01_01_15_check_presence_of_weather_maps_link(self, driver):
            """Checks if the Weather Maps link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.WEATHER_MAPS_LINK), \
                "The Weather Maps link is not present in the DOM tree"

        def test_tc_01_01_16_check_presence_of_weather_dashboard_link(self, driver):
            """Checks if the Weather Dashboard link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.WEATHER_DASHBOARD_LINK), \
                "The Weather Dashboard link is not present in the DOM tree"

        def test_tc_01_01_17_check_presence_of_widgets_link(self, driver):
            """Checks if the Widgets link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.WIDGETS_LINK), \
                "The Widgets link is not present in the DOM tree"

    class TestSubscriptionSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_18_check_presence_of_subscription_section_title(self, driver):
            """Checks if the Subscription section's title is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.SUBSCRIPTION_SECTION_TITLE), \
                "The Subscription section's title is not present in the DOM tree"

        def test_tc_01_01_19_check_presence_of_how_to_start_link(self, driver):
            """Checks if the How to start link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.HOW_TO_START_LINK), \
                "The How to start link is not present in the DOM tree"

        def test_tc_01_01_20_check_presence_of_pricing_link(self, driver):
            """Checks if the Pricing link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.PRICING_LINK), \
                "The Pricing link is not present in the DOM tree"

        def test_tc_01_01_21_check_presence_of_subscribe_for_free_link(self, driver):
            """Checks if the Subscribe for free link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.SUBSCRIBE_FOR_FREE_LINK), \
                "The Subscribe for free link is not present in the DOM tree"

        def test_tc_01_01_22_check_presence_of_faq_link(self, driver):
            """Checks if the FAQ link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.FAQ_LINK), \
                "The FAQ link is not present in the DOM tree"

    class TestTechnologiesSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_23_check_presence_of_technologies_section_title(self, driver):
            """Checks if the Technologies section's title is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.TECHNOLOGIES_SECTION_TITLE), \
                "The Technologies section's title is not present in the DOM tree"

        def test_tc_01_01_24_check_presence_of_our_technology_link(self, driver):
            """Checks if the Our technology link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.OUR_TECHNOLOGY_LINK), \
                "The Our technology link is not present in the DOM tree"

        def test_tc_01_01_25_check_presence_of_accuracy_and_quality_of_weather_data_link(self, driver):
            """Checks if the Accuracy and quality of weather data link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK), \
                "The Accuracy and quality of weather data link is not present in the DOM tree"

        def test_tc_01_01_26_check_presence_of_connect_your_weather_station_link(self, driver):
            """Checks if the Connect your weather station link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.CONNECT_YOUR_WEATHER_STATION_LINK), \
                "The Connect your weather station link is not present in the DOM tree"

    class TestTermsAndConditionsSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_27_check_presence_of_terms_and_conditions_section_title(self, driver):
            """Checks if the Terms & Conditions section's title is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.TERMS_AND_CONDITIONS_SECTION_TITLE), \
                "The Terms & Conditions section's title is not present in the DOM tree"

        def test_tc_01_01_28_check_presence_of_terms_and_conditions_of_sale_link(self, driver):
            """Checks if the Terms and conditions of sale link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.TERMS_AND_CONDITIONS_OF_SALE_LINK), \
                "The Terms and conditions of sale link is not present in the DOM tree"

        def test_tc_01_01_29_check_presence_of_privacy_policy_link(self, driver):
            """Checks if the Privacy Policy link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.PRIVACY_POLICY_LINK), \
                "The Privacy Policy link is not present in the DOM tree"

        def test_tc_01_01_30_check_presence_of_website_terms_and_conditions_link(self, driver):
            """Checks if the Website terms and conditions link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.WEBSITE_TERMS_AND_CONDITIONS_LINK), \
                "The Website terms and conditions link is not present in the DOM tree"

    class TestCompanySectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_31_check_presence_of_company_section_title(self, driver):
            """Checks if the Company section's title is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.COMPANY_SECTION_TITLE), \
                "The Company section's title is not present in the DOM tree"

        def test_tc_01_01_32_check_presence_of_company_section_content(self, driver):
            """Checks if the Company section's content is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.COMPANY_SECTION_CONTENT), \
                "The Company section's content is not present in the DOM tree"

    class TestSingleLinksSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_33_check_presence_of_about_us_link(self, driver):
            """Checks if the About us link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.ABOUT_US_LINK), \
                "The About us link is not present in the DOM tree"

        def test_tc_01_01_34_check_presence_of_blog_link(self, driver):
            """Checks if the Blog link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.BLOG_LINK), \
                "The Blog link is not present in the DOM tree"

        def test_tc_01_01_35_check_presence_of_openweather_for_business_link(self, driver):
            """Checks if the OpenWeather for Business link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.OPENWEATHER_FOR_BUSINESS_LINK), \
                "The OpenWeather for Business link is not present in the DOM tree"

        def test_tc_01_01_36_check_presence_of_ask_a_question_link(self, driver):
            """Checks if the Ask a question link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.ASK_A_QUESTION_LINK), \
                "The Ask a question link is not present in the DOM tree"

    class TestDownloadOpenWeatherAppSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_37_check_presence_of_download_openweather_app_section_title(self, driver):
            """Checks if the Download OpenWeather app section's title is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.DOWNLOAD_OPENWEATHER_APP_SECTION_TITLE), \
                "The Download OpenWeather app section's title is not present in the DOM tree"

        def test_tc_01_01_38_check_presence_of_download_on_the_app_store_link(self, driver):
            """Checks if the Download on the App Store link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.DOWNLOAD_ON_THE_APP_STORE_LINK), \
                "The Download on the App Store link is not present in the DOM tree"

        def test_tc_01_01_39_check_presence_of_get_it_on_google_play_link(self, driver):
            """Checks if the GET IT ON Google Play link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.GET_IT_ON_GOOGLE_PLAY_LINK), \
                "The GET IT ON Google Play link is not present in the DOM tree"

    class TestRmetsSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_40_check_presence_of_rmets_section_title(self, driver):
            """Checks if the RMetS section's title is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.RMETS_SECTION_TITLE), \
                "The RMetS section's title is not present in the DOM tree"

        def test_tc_01_01_41_check_presence_of_rmets_element(self, driver):
            """Checks if the RMetS element is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.RMETS_IMAGE), \
                "The RMetS element is not present in the DOM tree"

    class TestCopyrightSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_42_check_presence_of_copyright_element_01(self, driver):
            """Checks if the Copyright element 01 is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.COPYRIGHT_ELEMENT_01), \
                "The Copyright element 01 is not present in the DOM tree"

        def test_tc_01_01_43_check_presence_of_copyright_element_02(self, driver):
            """Checks if the Copyright element 02 is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.COPYRIGHT_ELEMENT_02), \
                "The Copyright element 02 is not present in the DOM tree"

    class TestSocialMediaSectionPresence:
        footer_locators = FooterLocators()

        def test_tc_01_01_44_check_presence_of_facebook_link(self, driver):
            """Checks if the Facebook link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.FACEBOOK_LINK), \
                "The Facebook link is not present in the DOM tree"

        def test_tc_01_01_45_check_presence_of_twitter_link(self, driver):
            """Checks if the Twitter link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.TWITTER_LINK), \
                "The Twitter link is not present in the DOM tree"

        def test_tc_01_01_46_check_presence_of_linkedin_link(self, driver):
            """Checks if the Linkedin link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.LINKEDIN_LINK), \
                "The Linkedin link is not present in the DOM tree"

        def test_tc_01_01_47_check_presence_of_medium_link(self, driver):
            """Checks if the Medium link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.MEDIUM_LINK), \
                "The Medium link is not present in the DOM tree"

        def test_tc_01_01_48_check_presence_of_telegram_link(self, driver):
            """Checks if the Telegram link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.TELEGRAM_LINK), \
                "The Telegram link is not present in the DOM tree"

        def test_tc_01_01_49_check_presence_of_github_link(self, driver):
            """Checks if the GitHub link is present in the DOM tree"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_present(self.footer_locators.GITHUB_LINK), \
                "The GitHub link is not present in the DOM tree"


class TestFooterVisibility:
    footer_locators = FooterLocators()

    def test_tc_01_02_01_check_visibility_of_footer(self, driver):
        """Checks if the footer is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.FOOTER_SECTION), \
            "The footer is invisible on the Main Page"

    class TestFooterSectionsVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_02_check_visibility_of_product_collections_section(self, driver):
            """Checks if the Product Collections section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.PRODUCT_COLLECTIONS_SECTION), \
                "The Product Collections section is invisible on the Main Page"

        def test_tc_01_02_03_check_visibility_of_subscription_section(self, driver):
            """Checks if the Subscription section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.SUBSCRIPTION_SECTION), \
                "The Subscription section is invisible on the Main Page"

        def test_tc_01_02_04_check_visibility_of_technologies_section(self, driver):
            """Checks if the Technologies section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.TECHNOLOGIES_SECTION), \
                "The Technologies section is invisible on the Main Page"

        def test_tc_01_02_05_check_visibility_of_terms_and_conditions_section(self, driver):
            """Checks if the Terms and Conditions section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.TERMS_AND_CONDITIONS_SECTION), \
                "The Terms and Conditions section is invisible on the Main Page"

        def test_tc_01_02_06_check_visibility_of_company_section(self, driver):
            """Checks if the Company section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.COMPANY_SECTION), \
                "The Company section is invisible on the Main Page"

        def test_tc_01_02_07_check_visibility_of_single_links_section(self, driver):
            """Checks if the single links section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.SINGLE_LINKS_SECTION), \
                "The single links section is invisible on the Main Page"

        def test_tc_01_02_08_check_visibility_of_download_openweather_app_section(self, driver):
            """Checks if the Download OpenWeather app section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.DOWNLOAD_OPENWEATHER_APP_SECTION), \
                "The Download OpenWeather app section is invisible on the Main Page"

        def test_tc_01_02_09_check_visibility_of_copyright_section(self, driver):
            """Checks if the Copyright section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.COPYRIGHT_SECTION), \
                "The Copyright section is invisible on the Main Page"

        def test_tc_01_02_10_check_visibility_of_social_media_section(self, driver):
            """Checks if the Social media section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.SOCIAL_MEDIA_SECTION), \
                "The Social media section is invisible on the Main Page"

        def test_tc_01_02_11_check_visibility_of_rmets_section(self, driver):
            """Checks if the RMetS section is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.RMETS_SECTION), \
                "The RMetS section is invisible on the Main Page"

    class TestProductCollectionsSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_12_check_visibility_of_product_collections_section_title(self, driver):
            """Checks if the Product Collections section's title is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.PRODUCT_COLLECTIONS_SECTION_TITLE), \
                "The Product Collections section's title is invisible on the Main Page"

        def test_tc_01_02_13_check_visibility_of_current_and_forecast_apis_link(self, driver):
            """Checks if the Current and Forecast APIs link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK), \
                "The Current and Forecast APIs link is invisible on the Main Page"

        def test_tc_01_02_14_check_visibility_of_historical_weather_data_link(self, driver):
            """Checks if the Historical Weather Data link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK), \
                "The Historical Weather Data link is invisible on the Main Page"

        def test_tc_01_02_15_check_visibility_of_weather_maps_link(self, driver):
            """Checks if the Weather Maps link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.WEATHER_MAPS_LINK), \
                "The Weather Maps link is invisible on the Main Page"

        def test_tc_01_02_16_check_visibility_of_weather_dashboard_link(self, driver):
            """Checks if the Weather Dashboard link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.WEATHER_DASHBOARD_LINK), \
                "The Weather Dashboard link is invisible on the Main Page"

        def test_tc_01_02_17_check_visibility_of_widgets_link(self, driver):
            """Checks if the Widgets link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.WIDGETS_LINK), \
                "The Widgets link is invisible on the Main Page"

    class TestSubscriptionSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_18_check_visibility_of_subscription_section_title(self, driver):
            """Checks if the Subscription section's title is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.SUBSCRIPTION_SECTION_TITLE), \
                "The Subscription section's title is invisible on the Main Page"

        def test_tc_01_02_19_check_visibility_of_how_to_start_link(self, driver):
            """Checks if the How to start link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.HOW_TO_START_LINK), \
                "The How to start link is invisible on the Main Page"

        def test_tc_01_02_20_check_visibility_of_pricing_link(self, driver):
            """Checks if the Pricing link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.PRICING_LINK), \
                "The Pricing link is invisible on the Main Page"

        def test_tc_01_02_21_check_visibility_of_subscribe_for_free_link(self, driver):
            """Checks if the Subscribe for free link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.SUBSCRIBE_FOR_FREE_LINK), \
                "The Subscribe for free link is invisible on the Main Page"

        def test_tc_01_02_22_check_visibility_of_faq_link(self, driver):
            """Checks if the FAQ link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.FAQ_LINK), \
                "The FAQ link is invisible on the Main Page"

    class TestTechnologiesSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_23_check_visibility_of_technologies_section_title(self, driver):
            """Checks if the Technologies section's title is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.TECHNOLOGIES_SECTION_TITLE), \
                "The Technologies section's title is invisible on the Main Page"

        def test_tc_01_02_24_check_visibility_of_our_technology_link(self, driver):
            """Checks if the Our technology link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.OUR_TECHNOLOGY_LINK), \
                "The Our technology link is invisible on the Main Page"

        def test_tc_01_02_25_check_visibility_of_accuracy_and_quality_of_weather_data_link(self, driver):
            """Checks if the Accuracy and quality of weather data link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK), \
                "The Accuracy and quality of weather data link is invisible on the Main Page"

        def test_tc_01_02_26_check_visibility_of_connect_your_weather_station_link(self, driver):
            """Checks if the Connect your weather station link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.CONNECT_YOUR_WEATHER_STATION_LINK), \
                "The Connect your weather station link is invisible on the Main Page"

    class TestTermsAndConditionsSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_27_check_visibility_of_terms_and_conditions_section_title(self, driver):
            """Checks if the Terms & Conditions section's title is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.TERMS_AND_CONDITIONS_SECTION_TITLE), \
                "The Terms & Conditions section's title is invisible on the Main Page"

        def test_tc_01_02_28_check_visibility_of_terms_and_conditions_of_sale_link(self, driver):
            """Checks if the Terms and conditions of sale link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.TERMS_AND_CONDITIONS_OF_SALE_LINK), \
                "The Terms and conditions of sale link is invisible on the Main Page"

        def test_tc_01_02_29_check_visibility_of_privacy_policy_link(self, driver):
            """Checks if the Privacy Policy link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.PRIVACY_POLICY_LINK), \
                "The Privacy Policy link is invisible on the Main Page"

        def test_tc_01_02_30_check_visibility_of_website_terms_and_conditions_link(self, driver):
            """Checks if the Website terms and conditions link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.WEBSITE_TERMS_AND_CONDITIONS_LINK), \
                "The Website terms and conditions link is invisible on the Main Page"

    class TestCompanySectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_31_check_visibility_of_company_section_title(self, driver):
            """Checks if the Company section's title is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.COMPANY_SECTION_TITLE), \
                "The Company section's title is invisible on the Main Page"

        def test_tc_01_02_32_check_visibility_of_company_section_content(self, driver):
            """Checks if the Company section's content is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.COMPANY_SECTION_CONTENT), \
                "The Company section's content is invisible on the Main Page"

    class TestSingleLinksSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_33_check_visibility_of_about_us_link(self, driver):
            """Checks if the About us link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.ABOUT_US_LINK), \
                "The About us link is invisible on the Main Page"

        def test_tc_01_02_34_check_visibility_of_blog_link(self, driver):
            """Checks if the Blog link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.BLOG_LINK), \
                "The Blog link is invisible on the Main Page"

        def test_tc_01_02_35_check_visibility_of_openweather_for_business_link(self, driver):
            """Checks if the OpenWeather for Business link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.OPENWEATHER_FOR_BUSINESS_LINK), \
                "The OpenWeather for Business link is invisible on the Main Page"

        def test_tc_01_02_36_check_visibility_of_ask_a_question_link(self, driver):
            """Checks if the Ask a question link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.ASK_A_QUESTION_LINK), \
                "The Ask a question link is invisible on the Main Page"

    class TestDownloadOpenWeatherAppSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_37_check_visibility_of_download_openweather_app_section_title(self, driver):
            """Checks if the Download OpenWeather app section's title is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.DOWNLOAD_OPENWEATHER_APP_SECTION_TITLE), \
                "The Download OpenWeather app section's title is invisible on the Main Page"

        def test_tc_01_02_38_check_visibility_of_download_on_the_app_store_link(self, driver):
            """Checks if the Download on the App Store link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.DOWNLOAD_ON_THE_APP_STORE_LINK), \
                "The Download on the App Store link is invisible on the Main Page"

        def test_tc_01_02_39_check_visibility_of_get_it_on_google_play_link(self, driver):
            """Checks if the GET IT ON Google Play link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.GET_IT_ON_GOOGLE_PLAY_LINK), \
                "The GET IT ON Google Play link is invisible on the Main Page"

    class TestRmetsSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_40_check_visibility_of_rmets_section_title(self, driver):
            """Checks if the RMetS section's title is invisible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_not_visible(self.footer_locators.RMETS_SECTION_TITLE), \
                "The RMetS section's title is visible on the Main Page"

        def test_tc_01_02_41_check_visibility_of_rmets_element(self, driver):
            """Checks if the RMetS element is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.RMETS_IMAGE), \
                "The RMetS element is invisible on the Main Page"

    class TestCopyrightSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_42_check_visibility_of_copyright_element_01(self, driver):
            """Checks if the Copyright element 01 is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.COPYRIGHT_ELEMENT_01), \
                "The Copyright element 01 is invisible on the Main Page"

        def test_tc_01_02_43_check_visibility_of_copyright_element_02(self, driver):
            """Checks if the Copyright element 02 is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.COPYRIGHT_ELEMENT_02), \
                "The Copyright element 02 is invisible on the Main Page"

    class TestSocialMediaSectionVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_44_check_visibility_of_facebook_link(self, driver):
            """Checks if the Facebook link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.FACEBOOK_LINK), \
                "The Facebook link is invisible on the Main Page"

        def test_tc_01_02_45_check_visibility_of_twitter_link(self, driver):
            """Checks if the Twitter link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.TWITTER_LINK), \
                "The Twitter link is invisible on the Main Page"

        def test_tc_01_02_46_check_visibility_of_linkedin_link(self, driver):
            """Checks if the Linkedin link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.LINKEDIN_LINK), \
                "The Linkedin link is invisible on the Main Page"

        def test_tc_01_02_47_check_visibility_of_medium_link(self, driver):
            """Checks if the Medium link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.MEDIUM_LINK), \
                "The Medium link is invisible on the Main Page"

        def test_tc_01_02_48_check_visibility_of_telegram_link(self, driver):
            """Checks if the Telegram link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.TELEGRAM_LINK), \
                "The Telegram link is invisible on the Main Page"

        def test_tc_01_02_49_check_visibility_of_github_link(self, driver):
            """Checks if the GitHub link is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.GITHUB_LINK), \
                "The GitHub link is invisible on the Main Page"


class TestFooterElementsText:
    footer_locators = FooterLocators()

    class TestProductCollectionsSectionText:
        footer_locators = FooterLocators()

        def test_tc_01_03_01_check_text_of_product_collections_section_title(self, driver):
            """Checks if text of the Product Collections section's title is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.PRODUCT_COLLECTIONS_SECTION_TITLE)
            expected_text = FooterElementsText.PRODUCT_COLLECTIONS_SECTION_TITLE_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Product Collections " \
                                                 f"section's title does not match expected '{expected_text}' " \
                                                 f"on the Main Page"

        def test_tc_01_03_02_check_text_of_current_and_forecast_apis_link(self, driver):
            """Checks if text of the Current and Forecast APIs link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK)
            expected_text = FooterElementsText.CURRENT_AND_FORECAST_APIS_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Current and Forecast APIs " \
                                                 f"link does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_03_check_text_of_historical_weather_data_link(self, driver):
            """Checks if text of the Historical Weather Data link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK)
            expected_text = FooterElementsText.HISTORICAL_WEATHER_DATA_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Historical Weather Data " \
                                                 f"link does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_04_check_text_of_weather_maps_link(self, driver):
            """Checks if text of the Weather Maps link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.WEATHER_MAPS_LINK)
            expected_text = FooterElementsText.WEATHER_MAPS_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Weather Maps link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_05_check_text_of_weather_dashboard_link(self, driver):
            """Checks if text of the Weather Dashboard link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.WEATHER_DASHBOARD_LINK)
            expected_text = FooterElementsText.WEATHER_DASHBOARD_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Weather Dashboard link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_06_check_text_of_widgets_link(self, driver):
            """Checks if text of the Widgets link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.WIDGETS_LINK)
            expected_text = FooterElementsText.WIDGETS_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Widgets link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

    class TestSubscriptionSectionText:
        footer_locators = FooterLocators()

        def test_tc_01_03_07_check_text_of_subscription_section_title(self, driver):
            """Checks if text of the Subscription section's title is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.SUBSCRIPTION_SECTION_TITLE)
            expected_text = FooterElementsText.SUBSCRIPTION_SECTION_TITLE_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Subscription section's " \
                                                 f"title does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_08_check_text_of_how_to_start_link(self, driver):
            """Checks if text of the How to start link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.HOW_TO_START_LINK)
            expected_text = FooterElementsText.HOW_TO_START_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the How to start link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_09_check_text_of_pricing_link(self, driver):
            """Checks if text of the Pricing link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.PRICING_LINK)
            expected_text = FooterElementsText.PRICING_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Pricing link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_10_check_text_of_subscribe_for_free_link(self, driver):
            """Checks if text of the Subscribe for free link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.SUBSCRIBE_FOR_FREE_LINK)
            expected_text = FooterElementsText.SUBSCRIBE_FOR_FREE_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Subscribe for free link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_11_check_text_of_faq_link(self, driver):
            """Checks if text of the FAQ link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.FAQ_LINK)
            expected_text = FooterElementsText.FAQ_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the FAQ link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

    class TestTechnologiesSectionText:
        footer_locators = FooterLocators()

        def test_tc_01_03_12_check_text_of_technologies_section_title(self, driver):
            """Checks if text of the Technologies section's title is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.TECHNOLOGIES_SECTION_TITLE)
            expected_text = FooterElementsText.TECHNOLOGIES_SECTION_TITLE_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Technologies section's " \
                                                 f"title does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_13_check_text_of_our_technology_link(self, driver):
            """Checks if text of the Our technology link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.OUR_TECHNOLOGY_LINK)
            expected_text = FooterElementsText.OUR_TECHNOLOGY_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Our technology link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_14_check_text_of_accuracy_and_quality_of_weather_data_link(self, driver):
            """Checks if text of the Accuracy and quality of weather data link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK)
            expected_text = FooterElementsText.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Accuracy and quality " \
                                                 f"of weather data link does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_15_check_text_of_connect_your_weather_station_link(self, driver):
            """Checks if text of the Connect your weather station link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.CONNECT_YOUR_WEATHER_STATION_LINK)
            expected_text = FooterElementsText.CONNECT_YOUR_WEATHER_STATION_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Connect your weather " \
                                                 f"station link does not match expected '{expected_text}' on the Main Page"

    class TestTermsAndConditionsSectionText:
        footer_locators = FooterLocators()

        def test_tc_01_03_16_check_text_of_terms_and_conditions_section_title(self, driver):
            """Checks if text of the Terms & Conditions section's title is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.TERMS_AND_CONDITIONS_SECTION_TITLE)
            expected_text = FooterElementsText.TERMS_AND_CONDITIONS_SECTION_TITLE_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Terms & Conditions " \
                                                 f"section's title does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_17_check_text_of_terms_and_conditions_of_sale_link(self, driver):
            """Checks if text of the Terms and conditions of sale link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.TERMS_AND_CONDITIONS_OF_SALE_LINK)
            expected_text = FooterElementsText.TERMS_AND_CONDITIONS_OF_SALE_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Terms and conditions " \
                                                 f"of sale link does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_18_check_text_of_privacy_policy_link(self, driver):
            """Checks if text of the Privacy Policy link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.PRIVACY_POLICY_LINK)
            expected_text = FooterElementsText.PRIVACY_POLICY_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Privacy Policy link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_19_check_text_of_website_terms_and_conditions_link(self, driver):
            """Checks if text of the Website terms and conditions link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.WEBSITE_TERMS_AND_CONDITIONS_LINK)
            expected_text = FooterElementsText.WEBSITE_TERMS_AND_CONDITIONS_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Website terms " \
                                                 f"and conditions link does not match expected '{expected_text}' on the Main Page"

    class TestCompanySectionText:
        footer_locators = FooterLocators()

        def test_tc_01_03_20_check_text_of_company_section_title(self, driver):
            """Checks if text of the Company section's title is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.COMPANY_SECTION_TITLE)
            expected_text = FooterElementsText.COMPANY_SECTION_TITLE_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Company section's title " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_21_check_text_of_company_section_content(self, driver):
            """Checks if text of the Company section's content is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.COMPANY_SECTION_CONTENT)
            expected_text = FooterElementsText.COMPANY_SECTION_CONTENT_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Company section's content " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

    class TestSingleLinksSectionText:
        footer_locators = FooterLocators()

        def test_tc_01_03_22_check_text_of_about_us_link(self, driver):
            """Checks if text of the About us link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.ABOUT_US_LINK)
            expected_text = FooterElementsText.ABOUT_US_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the About us link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_23_check_text_of_blog_link(self, driver):
            """Checks if text of the Blog link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.BLOG_LINK)
            expected_text = FooterElementsText.BLOG_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Blog link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_24_check_text_of_openweather_for_business_link(self, driver):
            """Checks if text of the OpenWeather for Business link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.OPENWEATHER_FOR_BUSINESS_LINK)
            expected_text = FooterElementsText.OPENWEATHER_FOR_BUSINESS_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the OpenWeather for Business " \
                                                 f"link does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_25_check_text_of_ask_a_question_link(self, driver):
            """Checks if text of the Ask a question link is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.ASK_A_QUESTION_LINK)
            expected_text = FooterElementsText.ASK_A_QUESTION_LINK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Ask a question link " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

    class TestDownloadOpenWeatherAppSectionText:
        footer_locators = FooterLocators()

        def test_tc_01_03_26_check_text_of_download_openweather_app_section_title(self, driver):
            """Checks if text of the Download OpenWeather app section's title is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.DOWNLOAD_OPENWEATHER_APP_SECTION_TITLE)
            expected_text = FooterElementsText.DOWNLOAD_OPENWEATHER_APP_SECTION_TITLE_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Download OpenWeather app " \
                                                 f"section's title does not match expected '{expected_text}' on the Main Page"

    class TestCopyrightSectionText:
        footer_locators = FooterLocators()

        def test_tc_01_03_27_check_text_of_copyright_element_01(self, driver):
            """Checks if text of the Copyright element 01 is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.COPYRIGHT_ELEMENT_01)
            expected_text = FooterElementsText.COPYRIGHT_ELEMENT_01_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Copyright element 01 " \
                                                 f"does not match expected '{expected_text}' on the Main Page"

        def test_tc_01_03_28_check_text_of_copyright_element_02(self, driver):
            """Checks if text of the Copyright element 02 is correct on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            actual_text = page.get_text(self.footer_locators.COPYRIGHT_ELEMENT_02)
            expected_text = FooterElementsText.COPYRIGHT_ELEMENT_02_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of the Copyright element 02 " \
                                                 f"does not match expected '{expected_text}' on the Main Page"


class TestFooterElementsImage:
    footer_locators = FooterLocators()

    def test_tc_01_04_01_check_image_presence_in_download_on_the_app_store_link(self, driver):
        """Checks if an image in the Download on the App Store link is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.DOWNLOAD_ON_THE_APP_STORE_IMAGE), \
            "An image in the Download on the App Store link is not present in the DOM tree"

    def test_tc_01_04_02_check_image_visibility_in_download_on_the_app_store_link(self, driver):
        """Checks if an image in the Download on the App Store link is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.DOWNLOAD_ON_THE_APP_STORE_IMAGE), \
            "An image in the Download on the App Store link is invisible on the Main Page"

    def test_tc_01_04_03_check_image_correctness_in_download_on_the_app_store_link(self, driver):
        """Checks if the image in the Download on the App Store link is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.DOWNLOAD_ON_THE_APP_STORE_IMAGE) == \
               FooterImageUrls.DOWNLOAD_ON_THE_APP_STORE_IMAGE_URL, "The image in the Download on the App Store link" \
                                                                    "is incorrect"

    def test_tc_01_04_04_check_image_presence_in_get_it_on_google_play_link(self, driver):
        """Checks if an image in the GET IT ON Google Play link is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.GET_IT_ON_GOOGLE_PLAY_IMAGE), \
            "An image in the GET IT ON Google Play link is not present in the DOM tree"

    def test_tc_01_04_05_check_image_visibility_in_get_it_on_google_play_link(self, driver):
        """Checks if an image in the GET IT ON Google Play link is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.GET_IT_ON_GOOGLE_PLAY_IMAGE), \
            "An image in the GET IT ON Google Play link is invisible on the Main Page"

    def test_tc_01_04_06_check_image_correctness_in_get_it_on_google_play_link(self, driver):
        """Checks if the image in the GET IT ON Google Play link is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.GET_IT_ON_GOOGLE_PLAY_IMAGE) == \
               FooterImageUrls.GET_IT_ON_GOOGLE_PLAY_IMAGE_URL, "The image in the GET IT ON Google Play link " \
                                                                "is incorrect"

    def test_tc_01_04_07_check_image_presence_in_rmets_element(self, driver):
        """Checks if an image in the RMetS element is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.RMETS_IMAGE), "An image in the RMetS element " \
                                                                          "is not present in the DOM tree"

    def test_tc_01_04_08_check_image_visibility_in_rmets_element(self, driver):
        """Checks if an image in the RMetS element is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.RMETS_IMAGE), "An image in the RMetS element " \
                                                                          "is invisible on the Main Page"

    def test_tc_01_04_09_check_image_correctness_in_rmets_element(self, driver):
        """Checks if the image in the RMetS element is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.RMETS_IMAGE) == FooterImageUrls.RMETS_IMAGE_URL, \
            "The image in the RMetS element is incorrect"

    def test_tc_01_04_10_check_image_presence_in_facebook_link(self, driver):
        """Checks if an image in the Facebook link is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.FACEBOOK_IMAGE), "An image in the Facebook link " \
                                                                             "is not present in the DOM tree"

    def test_tc_01_04_11_check_image_visibility_in_facebook_link(self, driver):
        """Checks if an image in the Facebook link is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.FACEBOOK_IMAGE), "An image in the Facebook link " \
                                                                             "is invisible on the Main Page"

    def test_tc_01_04_12_check_image_correctness_in_facebook_link(self, driver):
        """Checks if the image in the Facebook link is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.FACEBOOK_IMAGE) == FooterImageUrls.FACEBOOK_IMAGE_URL, \
            "The image in the Facebook link is incorrect"

    def test_tc_01_04_13_check_image_presence_in_twitter_link(self, driver):
        """Checks if an image in the Twitter link is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.TWITTER_IMAGE), "An image in the Twitter link " \
                                                                            "is not present in the DOM tree"

    def test_tc_01_04_14_check_image_visibility_in_twitter_link(self, driver):
        """Checks if an image in the Twitter link is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.TWITTER_IMAGE), "An image in the Twitter link " \
                                                                            "is invisible on the Main Page"

    def test_tc_01_04_15_check_image_correctness_in_twitter_link(self, driver):
        """Checks if the image in the Twitter link is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.TWITTER_IMAGE) == FooterImageUrls.TWITTER_IMAGE_URL, \
            "The image in the Twitter link is incorrect"

    def test_tc_01_04_16_check_image_presence_in_linkedin_link(self, driver):
        """Checks if an image in the LinkedIn link is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.LINKEDIN_IMAGE), "An image in the LinkedIn link " \
                                                                             "is not present in the DOM tree"

    def test_tc_01_04_17_check_image_visibility_in_linkedin_link(self, driver):
        """Checks if an image in the LinkedIn link is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.LINKEDIN_IMAGE), "An image in the LinkedIn link " \
                                                                            "is invisible on the Main Page"

    def test_tc_01_04_18_check_image_correctness_in_linkedin_link(self, driver):
        """Checks if the image in the LinkedIn link is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.LINKEDIN_IMAGE) == FooterImageUrls.LINKEDIN_IMAGE_URL, \
            "The image in the LinkedIn link is incorrect"

    def test_tc_01_04_19_check_image_presence_in_medium_link(self, driver):
        """Checks if an image in the Medium link is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.MEDIUM_IMAGE), "An image in the Medium link " \
                                                                           "is not present in the DOM tree"

    def test_tc_01_04_20_check_image_visibility_in_medium_link(self, driver):
        """Checks if an image in the Medium link is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.MEDIUM_IMAGE), "An image in the Medium link " \
                                                                           "is invisible on the Main Page"

    def test_tc_01_04_21_check_image_correctness_in_medium_link(self, driver):
        """Checks if the image in the Medium link is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.MEDIUM_IMAGE) == FooterImageUrls.MEDIUM_IMAGE_URL, \
            "The image in the Medium link is incorrect"

    def test_tc_01_04_22_check_image_presence_in_telegram_link(self, driver):
        """Checks if an image in the Telegram link is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.TELEGRAM_IMAGE), "An image in the Telegram link " \
                                                                             "is not present in the DOM tree"

    def test_tc_01_04_23_check_image_visibility_in_telegram_link(self, driver):
        """Checks if an image in the Telegram link is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.TELEGRAM_IMAGE), "An image in the Telegram link " \
                                                                             "is invisible on the Main Page"

    def test_tc_01_04_24_check_image_correctness_in_telegram_link(self, driver):
        """Checks if the image in the Telegram link is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.TELEGRAM_IMAGE) == FooterImageUrls.TELEGRAM_IMAGE_URL, \
            "The image in the Telegram link is incorrect"

    def test_tc_01_04_25_check_image_presence_in_github_link(self, driver):
        """Checks if an image in the GitHub link is present in the DOM tree"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_present(self.footer_locators.GITHUB_IMAGE), "An image in the GitHub link " \
                                                                           "is not present in the DOM tree"

    def test_tc_01_04_26_check_image_visibility_in_github_link(self, driver):
        """Checks if an image in the GitHub link is visible on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_visible(self.footer_locators.GITHUB_IMAGE), "An image in the GitHub link " \
                                                                           "is invisible on the Main Page"

    def test_tc_01_04_27_check_image_correctness_in_github_link(self, driver):
        """Checks if the image in the GitHub link is correct"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.get_image_src(self.footer_locators.GITHUB_IMAGE) == FooterImageUrls.GITHUB_IMAGE_URL, \
            "The image in the GitHub link is incorrect"


class TestFooterLinksClickability:
    footer_locators = FooterLocators()

    def test_tc_01_05_01_check_clickability_of_current_and_forecast_apis_link(self, driver):
        """Checks if the Current and Forecast APIs link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK), \
            "The Current and Forecast APIs link is not clickable on the Main Page"

    def test_tc_01_05_02_check_clickability_of_historical_weather_data_link(self, driver):
        """Checks if the Historical Weather Data link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK), \
            "The Historical Weather Data link is not clickable on the Main Page"

    def test_tc_01_05_03_check_clickability_of_weather_maps_link(self, driver):
        """Checks if the Weather Maps link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.WEATHER_MAPS_LINK), \
            "The Weather Maps link is not clickable on the Main Page"

    def test_tc_01_05_04_check_clickability_of_weather_dashboard_link(self, driver):
        """Checks if the Weather Dashboard link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.WEATHER_DASHBOARD_LINK), \
            "The Weather Dashboard link is not clickable on the Main Page"

    def test_tc_01_05_05_check_clickability_of_widgets_link(self, driver):
        """Checks if the Widgets link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.WIDGETS_LINK), \
            "The Widgets link is not clickable on the Main Page"

    def test_tc_01_05_06_check_clickability_of_how_to_start_link(self, driver):
        """Checks if the How to start link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.HOW_TO_START_LINK), \
            "The How to start link is not clickable on the Main Page"

    def test_tc_01_05_07_check_clickability_of_pricing_link(self, driver):
        """Checks if the Pricing link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.PRICING_LINK), \
            "The Pricing link is not clickable on the Main Page"

    def test_tc_01_05_08_check_clickability_of_subscribe_for_free_link(self, driver):
        """Checks if the Subscribe for free link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.SUBSCRIBE_FOR_FREE_LINK), \
            "The Subscribe for free link is not clickable on the Main Page"

    def test_tc_01_05_09_check_clickability_of_faq_link(self, driver):
        """Checks if the FAQ link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.FAQ_LINK), \
            "The FAQ link is not clickable on the Main Page"

    def test_tc_01_05_10_check_clickability_of_our_technology_link(self, driver):
        """Checks if the Our technology link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.OUR_TECHNOLOGY_LINK), \
            "The Our technology link is not clickable on the Main Page"

    def test_tc_01_05_11_check_clickability_of_accuracy_and_quality_of_weather_data_link(self, driver):
        """Checks if the Accuracy and quality of weather data link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK), \
            "The Accuracy and quality of weather data link is not clickable on the Main Page"

    def test_tc_01_05_12_check_clickability_of_connect_your_weather_station_link(self, driver):
        """Checks if the Connect your weather station link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.CONNECT_YOUR_WEATHER_STATION_LINK), \
            "The Connect your weather station link is not clickable on the Main Page"

    def test_tc_01_05_13_check_clickability_of_terms_and_conditions_of_sale_link(self, driver):
        """Checks if the Terms and conditions of sale link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.TERMS_AND_CONDITIONS_OF_SALE_LINK), \
            "The Terms and conditions of sale link is not clickable on the Main Page"

    def test_tc_01_05_14_check_clickability_of_privacy_policy_link(self, driver):
        """Checks if the Privacy Policy link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.PRIVACY_POLICY_LINK), \
            "The Privacy Policy link is not clickable on the Main Page"

    def test_tc_01_05_15_check_clickability_of_website_terms_and_conditions_link(self, driver):
        """Checks if the Website terms and conditions link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.WEBSITE_TERMS_AND_CONDITIONS_LINK), \
            "The Website terms and conditions link is not clickable on the Main Page"

    def test_tc_01_05_16_check_clickability_of_about_us_link(self, driver):
        """Checks if the About us link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.ABOUT_US_LINK), \
            "The About us link is not clickable on the Main Page"

    def test_tc_01_05_17_check_clickability_of_blog_link(self, driver):
        """Checks if the Blog link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.BLOG_LINK), \
            "The Blog link is not clickable on the Main Page"

    def test_tc_01_05_18_check_clickability_of_openweather_for_business_link(self, driver):
        """Checks if the OpenWeather for Business link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.OPENWEATHER_FOR_BUSINESS_LINK), \
            "The OpenWeather for Business link is not clickable on the Main Page"

    def test_tc_01_05_19_check_clickability_of_ask_a_question_link(self, driver):
        """Checks if the Ask a question link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.ASK_A_QUESTION_LINK), \
            "The Ask a question link is not clickable on the Main Page"

    def test_tc_01_05_20_check_clickability_of_download_on_the_app_store_link(self, driver):
        """Checks if the Download on the App Store link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.DOWNLOAD_ON_THE_APP_STORE_LINK), \
            "The Download on the App Store link is not clickable on the Main Page"

    def test_tc_01_05_21_check_clickability_of_get_it_on_google_play_link(self, driver):
        """Checks if the GET IT ON Google Play link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.GET_IT_ON_GOOGLE_PLAY_LINK), \
            "The GET IT ON Google Play link is not clickable on the Main Page"

    def test_tc_01_05_22_check_clickability_of_facebook_link(self, driver):
        """Checks if the Facebook link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.FACEBOOK_LINK), \
            "The Facebook link is not clickable on the Main Page"

    def test_tc_01_05_23_check_clickability_of_twitter_link(self, driver):
        """Checks if the Twitter link is clickable on the Main Page"""
        page = FooterPage(driver, URL_MAIN_PAGE)
        page.open()
        assert page.element_is_clickable(self.footer_locators.TWITTER_LINK), \
            "The Twitter link is not clickable on the Main Page"
