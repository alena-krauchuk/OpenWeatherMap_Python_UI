import re
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """This method opens a browser by the provided link"""
        self.driver.get(self.url)

    def go_to_element(self, element):
        """
        This method scrolls the page to the selected element, making it visible to the user.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

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

    def element_is_not_visible(self, locator, timeout=5):
        """
         This method expects to verify whether the element is invisible or not.
         The element is present in the DOM tree.
         Locator - is used to find the element.
         Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
         """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def get_text(self, locator):
        """
        This method get element text
        :return: element text
        """
        text = self.element_is_visible(locator)
        return text.text

    def find_element(self, locator):
        """
        This method find element on the page
        :return: element
        """
        return self.driver.find_element(*locator)

    def get_image_src(self, locator):
        """
        This method get attribute "src" of the element
        :return: attribute "src"
        """
        return self.driver.find_element(*locator).get_attribute("src")

    def action_move_to_element(self, element):
        """
        This method moves the mouse cursor to the center of the selected element, simulating a hover action.
        It can be used to test the interactivity of an element when the mouse cursor is hovering over it.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def hover_over_element(self, locator, css_property, seconds=20):
        """
        This method finds a visible element using the provided locator,
        simulates a hover action by moving the cursor to it,
        and then returns the value of the specified CSS property of the element.
        Locator - is used to find the element.
        Css_property - the name of the CSS property whose value is to be returned.
        """
        element = self.element_is_visible(locator)  # Get the WebElement using locator
        wait(self.driver, seconds)
        self.action_move_to_element(element)        # Move to the element
        return element.value_of_css_property(css_property)
