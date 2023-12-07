"""This section contains the basic steps for running footer tests"""
from pages.base_page import BasePage
from locators.footer_locators import FooterLocators


class FooterPage(BasePage):
    footer_locators = FooterLocators()

    def current_and_forecast_apis_link_is_interactive(self):
        """Verify the Current and Forecast APIs link is interactive"""
        element = self.element_is_visible(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK)
        hovered_over_element = self.hover_over_element(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK, 'pointer', 1)
        return element, hovered_over_element

    def historical_weather_data_link_is_interactive(self):
        """Verify the Historical Weather Data link is interactive"""
        element = self.element_is_visible(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK)
        hovered_over_element = self.hover_over_element(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK, 'pointer', 1)
        return element, hovered_over_element
