import re
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains
from locators.wish_list_locators import WishListPageLocators as wl
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """This method opens a browser by the provided link"""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
           This method expects to verify that the elements are present in the DOM tree,
           but not necessarily visible and displayed on the page.
           Locator - is used to find the elements.
           Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
           """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

