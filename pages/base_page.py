import re
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.timeout = 10

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
        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
           This method expects to verify that the elements are present in the DOM tree,
           but not necessarily visible and displayed on the page.
           Locator - is used to find the elements.
           Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
           """
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def element_is_visible(self, locator, timeout=10):
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """
         This method expects to verify whether the element is invisible or not.
         The element is present in the DOM tree.
         Locator - is used to find the element.
         Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
         """
        return Wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def element_is_present_and_clickable(self, locator):
        with allure.step(f'Check element is visible and clickable: {locator}'):
            return (Wait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}") and
                    self.element_is_clickable(locator))

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
        Wait(self.driver, seconds)
        self.action_move_to_element(element)  # Move to the element
        return element.value_of_css_property(css_property)

    def get_actual_url_of_current_page(self):
        """
        This method allows to get URL of the current page
        """
        actual_url = self.driver.current_url
        return actual_url

    def check_expected_link(self, url):
        """An expectation for checking the current url.
        url is the expected url, which must be an exact match returns True
        if the url matches, false otherwise.
        """
        return Wait(self.driver, self.timeout).until(ec.url_to_be(url))

    def get_actual_title_of_current_page(self):
        """
        This method allows to get a title of the current page
        """
        actual_title = self.driver.title
        return actual_title
