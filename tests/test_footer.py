from pages.footer_page import FooterPage
from locators.footer_locators import FooterLocators
from data.data_urls import URL_MAIN_PAGE


class TestFooter:

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

            def test_tc_01_01_09_check_presence_of_copyright_section(self, driver):
                """Checks if the Copyright section is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.COPYRIGHT_SECTION), \
                    "The Copyright section is not present in the DOM tree"

            def test_tc_01_01_10_check_presence_of_social_media_section(self, driver):
                """Checks if the Social media section is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.SOCIAL_MEDIA_SECTION), \
                    "The Social media section is not present in the DOM tree"

            def test_tc_01_01_11_check_presence_of_rmets_section(self, driver):
                """Checks if the RMetS section is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.RMETS_SECTION), \
                    "The RMetS section is not present in the DOM tree"

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

        class TestCompanySectionPresence:
            footer_locators = FooterLocators()

            def test_tc_01_01_30_check_presence_of_company_section_title(self, driver):
                """Checks if the Company section's title is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.COMPANY_SECTION_TITLE), \
                    "The Company section's title is not present in the DOM tree"

            def test_tc_01_01_31_check_presence_of_company_section_content(self, driver):
                """Checks if the Company section's content is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.COMPANY_SECTION_CONTENT), \
                    "The Company section's content is not present in the DOM tree"

        class TestSingleLinksSectionPresence:
            footer_locators = FooterLocators()

            def test_tc_01_01_32_check_presence_of_about_us_link(self, driver):
                """Checks if the About us link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.ABOUT_US_LINK), \
                    "The About us link is not present in the DOM tree"

            def test_tc_01_01_33_check_presence_of_blog_link(self, driver):
                """Checks if the Blog link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.BLOG_LINK), \
                    "The Blog link is not present in the DOM tree"

            def test_tc_01_01_34_check_presence_of_openweather_for_business_link(self, driver):
                """Checks if the OpenWeather for Business link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.OPENWEATHER_FOR_BUSINESS_LINK), \
                    "The OpenWeather for Business link is not present in the DOM tree"

            def test_tc_01_01_35_check_presence_of_ask_a_question_link(self, driver):
                """Checks if the Ask a question link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.ASK_A_QUESTION_LINK), \
                    "The Ask a question link is not present in the DOM tree"

        class TestDownloadOpenWeatherAppSectionPresence:
            footer_locators = FooterLocators()

            def test_tc_01_01_36_check_presence_of_download_openweather_app_section_title(self, driver):
                """Checks if the Download OpenWeather app section's title is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.DOWNLOAD_OPENWEATHER_APP_SECTION_TITLE), \
                    "The Download OpenWeather app section's title is not present in the DOM tree"

            def test_tc_01_01_37_check_presence_of_download_on_the_app_store_link(self, driver):
                """Checks if the Download on the App Store link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.DOWNLOAD_ON_THE_APP_STORE_LINK), \
                    "The Download on the App Store link is not present in the DOM tree"

            def test_tc_01_01_38_check_presence_of_get_it_on_google_play_link(self, driver):
                """Checks if the GET IT ON Google Play link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.GET_IT_ON_GOOGLE_PLAY_LINK), \
                    "The GET IT ON Google Play link is not present in the DOM tree"

        class TestRmetsSectionPresence:
            footer_locators = FooterLocators()

            def test_tc_01_01_39_check_presence_of_rmets_section_title(self, driver):
                """Checks if the RMetS section's title is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.RMETS_SECTION_TITLE), \
                    "The RMetS section's title is not present in the DOM tree"

            def test_tc_01_01_40_check_presence_of_rmets_element(self, driver):
                """Checks if the RMetS element is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.RMETS_ELEMENT), \
                    "The RMetS element is not present in the DOM tree"

        class TestCopyrightSectionPresence:
            footer_locators = FooterLocators()

            def test_tc_01_01_41_check_presence_of_copyright_element_01(self, driver):
                """Checks if the Copyright element 01 is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.COPYRIGHT_ELEMENT_01), \
                    "The Copyright element 01 is not present in the DOM tree"

            def test_tc_01_01_42_check_presence_of_copyright_element_02(self, driver):
                """Checks if the Copyright element 02 is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.COPYRIGHT_ELEMENT_02), \
                    "The Copyright element 02 is not present in the DOM tree"

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

        class TestCompanySectionVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_30_check_visibility_of_company_section_title(self, driver):
                """Checks if the Company section's title is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.COMPANY_SECTION_TITLE), \
                    "The Company section's title is invisible on the Main Page"

            def test_tc_01_02_31_check_visibility_of_company_section_content(self, driver):
                """Checks if the Company section's content is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.COMPANY_SECTION_CONTENT), \
                    "The Company section's content is invisible on the Main Page"

        class TestSingleLinksSectionVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_32_check_visibility_of_about_us_link(self, driver):
                """Checks if the About us link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.ABOUT_US_LINK), \
                    "The About us link is invisible on the Main Page"

            def test_tc_01_02_33_check_visibility_of_blog_link(self, driver):
                """Checks if the Blog link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.BLOG_LINK), \
                    "The Blog link is invisible on the Main Page"

            def test_tc_01_02_34_check_visibility_of_openweather_for_business_link(self, driver):
                """Checks if the OpenWeather for Business link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.OPENWEATHER_FOR_BUSINESS_LINK), \
                    "The OpenWeather for Business link is invisible on the Main Page"

            def test_tc_01_02_35_check_visibility_of_ask_a_question_link(self, driver):
                """Checks if the Ask a question link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.ASK_A_QUESTION_LINK), \
                    "The Ask a question link is invisible on the Main Page"

        class TestDownloadOpenWeatherAppSectionVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_36_check_visibility_of_download_openweather_app_section_title(self, driver):
                """Checks if the Download OpenWeather app section's title is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.DOWNLOAD_OPENWEATHER_APP_SECTION_TITLE), \
                    "The Download OpenWeather app section's title is invisible on the Main Page"

            def test_tc_01_02_37_check_visibility_of_download_on_the_app_store_link(self, driver):
                """Checks if the Download on the App Store link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.DOWNLOAD_ON_THE_APP_STORE_LINK), \
                    "The Download on the App Store link is invisible on the Main Page"

            def test_tc_01_02_38_check_visibility_of_get_it_on_google_play_link(self, driver):
                """Checks if the GET IT ON Google Play link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.GET_IT_ON_GOOGLE_PLAY_LINK), \
                    "The GET IT ON Google Play link is invisible on the Main Page"

        class TestRmetsSectionVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_39_check_visibility_of_rmets_section_title(self, driver):
                """Checks if the RMetS section's title is invisible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_not_visible(self.footer_locators.RMETS_SECTION_TITLE), \
                    "The RMetS section's title is visible on the Main Page"

            def test_tc_01_02_40_check_visibility_of_rmets_element(self, driver):
                """Checks if the RMetS element is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.RMETS_ELEMENT), \
                    "The RMetS element is invisible on the Main Page"

        class TestCopyrightSectionVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_41_check_visibility_of_copyright_element_01(self, driver):
                """Checks if the Copyright element 01 is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.COPYRIGHT_ELEMENT_01), \
                    "The Copyright element 01 is invisible on the Main Page"

            def test_tc_01_02_42_check_visibility_of_copyright_element_02(self, driver):
                """Checks if the Copyright element 02 is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.COPYRIGHT_ELEMENT_02), \
                    "The Copyright element 02 is invisible on the Main Page"
