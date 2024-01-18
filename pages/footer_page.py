"""This section contains the basic steps for running footer tests"""
import time

from pages.base_page import BasePage
from locators.footer_locators import FooterLocators
from locators.pages_locators import PagesAndSectionsTitlesLocators


class FooterPage(BasePage):
    footer_locators = FooterLocators()
    pages_locators = PagesAndSectionsTitlesLocators()

    def current_and_forecast_apis_link_is_interactive(self):
        """Verify the Current and Forecast APIs link is interactive"""
        element = self.element_is_visible(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK)
        hover_element = self.hover_over_element(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK, 'pointer', 1)
        return element, hover_element

    def historical_weather_data_link_is_interactive(self):
        """Verify the Historical Weather Data link is interactive"""
        element = self.element_is_visible(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK)
        hover_element = self.hover_over_element(self.footer_locators.HISTORICAL_WEATHER_DATA_LINK, 'pointer', 1)
        return element, hover_element

    def weather_maps_link_is_interactive(self):
        """Verify the Weather Maps link is interactive"""
        element = self.element_is_visible(self.footer_locators.WEATHER_MAPS_LINK)
        hover_element = self.hover_over_element(self.footer_locators.WEATHER_MAPS_LINK, 'pointer', 1)
        return element, hover_element

    def weather_dashboard_link_is_interactive(self):
        """Verify the Weather Dashboard link is interactive"""
        element = self.element_is_visible(self.footer_locators.WEATHER_DASHBOARD_LINK)
        hover_element = self.hover_over_element(self.footer_locators.WEATHER_DASHBOARD_LINK, 'pointer', 1)
        return element, hover_element

    def widgets_link_is_interactive(self):
        """Verify the Widgets link is interactive"""
        element = self.element_is_visible(self.footer_locators.WIDGETS_LINK)
        hover_element = self.hover_over_element(self.footer_locators.WIDGETS_LINK, 'pointer', 1)
        return element, hover_element

    def how_to_start_link_is_interactive(self):
        """Verify the How to start link is interactive"""
        element = self.element_is_visible(self.footer_locators.HOW_TO_START_LINK)
        hover_element = self.hover_over_element(self.footer_locators.HOW_TO_START_LINK, 'pointer', 1)
        return element, hover_element

    def get_link_href(self, locator):
        return self.driver.find_element(*locator).get_attribute("href")

    def get_current_and_forecast_apis_link_href(self):
        return self.get_link_href(self.footer_locators.CURRENT_AND_FORECAST_APIS_LINK)
