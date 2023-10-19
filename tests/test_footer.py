from pages.footer_page import FooterPage
from locators.footer_locators import FooterLocators
from data.data_urls import URL_MAIN_PAGE


class TestFooter:

    class TestFooterPresence:

        class TestFooterSectionsPresence:
            footer_locators = FooterLocators()

            def test_tc_01_01_01_check_presence_of_footer(self, driver):
                """Checks if the footer is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.FOOTER_SECTION), \
                    "The footer is not present in the DOM tree"

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

            def test_tc_01_01_12_check_presence_of_current_and_forecast_apis_link(self, driver):
                """Checks if the Current and Forecast APIs link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK), \
                    "The Current and Forecast APIs link is not present in the DOM tree"

            def test_tc_01_01_13_check_presence_of_historical_weather_data_link(self, driver):
                """Checks if the Historical Weather Data link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK), \
                    "The Historical Weather Data link is not present in the DOM tree"

            def test_tc_01_01_14_check_presence_of_weather_maps_link(self, driver):
                """Checks if the Weather Maps link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.WEATHER_MAPS_LINK), \
                    "The Weather Maps link is not present in the DOM tree"

            def test_tc_01_01_15_check_presence_of_weather_dashboard_link(self, driver):
                """Checks if the Weather Dashboard link is present in the DOM tree"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_present(self.footer_locators.WEATHER_DASHBOARD_LINK), \
                    "The Weather Dashboard link is not present in the DOM tree"

    class TestFooterVisibility:
        footer_locators = FooterLocators()

        def test_tc_01_02_01_check_visibility_of_footer(self, driver):
            """Checks if the footer is visible on the Main Page"""
            page = FooterPage(driver, URL_MAIN_PAGE)
            page.open()
            assert page.element_is_visible(self.footer_locators.FOOTER_SECTION), "The footer is invisible on the page"

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

            def test_tc_01_02_12_check_visibility_of_current_and_forecast_apis_link(self, driver):
                """Checks if the Current and Forecast APIs link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK), \
                    "The Current and Forecast APIs link is invisible on the page"

            def test_tc_01_02_13_check_visibility_of_historical_weather_data_link(self, driver):
                """Checks if the Historical Weather Data link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK), \
                    "The Historical Weather Data link is invisible on the page"

            def test_tc_01_02_14_check_visibility_of_weather_maps_link(self, driver):
                """Checks if the Weather Maps link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.WEATHER_MAPS_LINK), \
                    "The Weather Maps link is invisible on the page"

            def test_tc_01_02_15_check_visibility_of_weather_dashboard_link(self, driver):
                """Checks if the Weather Dashboard link is visible on the Main Page"""
                page = FooterPage(driver, URL_MAIN_PAGE)
                page.open()
                assert page.element_is_visible(self.footer_locators.WEATHER_DASHBOARD_LINK), \
                    "The Weather Dashboard link is invisible on the page"
