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

    class TestFooterVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_01_check_visibility_of_footer(self, driver):
            """Checks if the footer is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.FOOTER_SECTION), "The footer is invisible on the page"

        class TestFooterSectionsVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_02_check_visibility_of_product_collections_section(self, driver):
                """Checks if the Product Collections section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.PRODUCT_COLLECTIONS_SECTION), \
                    "The Product Collections section is invisible on the page"

            def test_tc_01_02_03_check_visibility_of_subscription_section(self, driver):
                """Checks if the Subscription section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.SUBSCRIPTION_SECTION), \
                    "The Subscription section is invisible on the page"

            def test_tc_01_02_04_check_visibility_of_technologies_section(self, driver):
                """Checks if the Technologies section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.TECHNOLOGIES_SECTION), \
                    "The Technologies section is invisible on the page"

            def test_tc_01_02_05_check_visibility_of_terms_and_conditions_section(self, driver):
                """Checks if the Terms and Conditions section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.TERMS_AND_CONDITIONS_SECTION), \
                    "The Terms and Conditions section is invisible on the page"

            def test_tc_01_02_06_check_visibility_of_company_section(self, driver):
                """Checks if the Company section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.COMPANY_SECTION), \
                    "The Company section is invisible on the page"

            def test_tc_01_02_07_check_visibility_of_single_links_section(self, driver):
                """Checks if the single links section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.SINGLE_LINKS_SECTION), \
                    "The single links section is invisible on the page"

            def test_tc_01_02_08_check_visibility_of_download_openweather_app_section(self, driver):
                """Checks if the Download OpenWeather app section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.DOWNLOAD_OPENWEATHER_APP_SECTION), \
                    "The Download OpenWeather app section is invisible on the page"

            def test_tc_01_02_09_check_visibility_of_copyright_section(self, driver):
                """Checks if the Copyright section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.COPYRIGHT_SECTION), \
                    "The Copyright section is invisible on the page"

            def test_tc_01_02_10_check_visibility_of_social_media_section(self, driver):
                """Checks if the Social media section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.SOCIAL_MEDIA_SECTION), \
                    "The Social media section is invisible on the page"

            def test_tc_01_02_11_check_visibility_of_rmets_section(self, driver):
                """Checks if the RMetS section is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.RMETS_SECTION), \
                    "The RMetS section is invisible on the page"

        class TestProductCollectionsSectionVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_12_check_visibility_of_product_collections_section_title(self, driver):
                """Checks if the Product Collections section's title is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.PRODUCT_COLLECTIONS_SECTION_TITLE), \
                    "The Product Collections section's title is invisible on the page"

            def test_tc_01_02_13_check_visibility_of_current_and_forecast_apis_link(self, driver):
                """Checks if the Current and Forecast APIs link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK), \
                    "The Current and Forecast APIs link is invisible on the page"

            def test_tc_01_02_14_check_visibility_of_historical_weather_data_link(self, driver):
                """Checks if the Historical Weather Data link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK), \
                    "The Historical Weather Data link is invisible on the page"

            def test_tc_01_02_15_check_visibility_of_weather_maps_link(self, driver):
                """Checks if the Weather Maps link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.WEATHER_MAPS_LINK), \
                    "The Weather Maps link is invisible on the page"

            def test_tc_01_02_16_check_visibility_of_weather_dashboard_link(self, driver):
                """Checks if the Weather Dashboard link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.WEATHER_DASHBOARD_LINK), \
                    "The Weather Dashboard link is invisible on the page"

            def test_tc_01_02_17_check_visibility_of_widgets_link(self, driver):
                """Checks if the Widgets link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.WIDGETS_LINK), \
                    "The Widgets link is invisible on the page"

        class TestSubscriptionSectionVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_18_check_visibility_of_subscription_section_title(self, driver):
                """Checks if the Subscription section's title is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.SUBSCRIPTION_SECTION_TITLE), \
                    "The Subscription section's title is invisible on the page"

            def test_tc_01_02_19_check_visibility_of_how_to_start_link(self, driver):
                """Checks if the How to start link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.HOW_TO_START_LINK), \
                    "The How to start link is invisible on the page"

            def test_tc_01_02_20_check_visibility_of_pricing_link(self, driver):
                """Checks if the Pricing link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.PRICING_LINK), \
                    "The Pricing link is invisible on the page"

            def test_tc_01_02_21_check_visibility_of_subscribe_for_free_link(self, driver):
                """Checks if the Subscribe for free link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.SUBSCRIBE_FOR_FREE_LINK), \
                    "The Subscribe for free link is invisible on the page"

            def test_tc_01_02_22_check_visibility_of_faq_link(self, driver):
                """Checks if the FAQ link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.FAQ_LINK), "The FAQ link is invisible on the page"

        class TestTechnologiesSectionVisibility:
            footer_locators = FooterLocators()

            def test_tc_01_02_23_check_visibility_of_technologies_section_title(self, driver):
                """Checks if the Technologies section's title is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.TECHNOLOGIES_SECTION_TITLE), \
                    "The Technologies section's title is invisible on the page"

            def test_tc_01_02_24_check_visibility_of_our_technology_link(self, driver):
                """Checks if the Our technology link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.OUR_TECHNOLOGY_LINK), \
                    "The Our technology link is invisible on the page"

            def test_tc_01_02_25_check_visibility_of_accuracy_and_quality_of_weather_data_link(self, driver):
                """Checks if the Accuracy and quality of weather data link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.ACCURACY_AND_QUALITY_OF_WEATHER_DATA_LINK), \
                    "The Accuracy and quality of weather data link is invisible on the page"

            def test_tc_01_02_26_check_visibility_of_connect_your_weather_station_link(self, driver):
                """Checks if the Connect your weather station link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.CONNECT_YOUR_WEATHER_STATION_LINK), \
                    "The Connect your weather station link is invisible on the page"

