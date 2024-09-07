from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import CommonLocators


class Page:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_be_visible(self, locator):
        WebDriverWait(self.driver, 3).until(
                expected_conditions.visibility_of_element_located(locator))

    def try_click_on_element(self, locator):
        while True:
            try:
                self.driver.find_element(*locator).click()
                break
            except ElementClickInterceptedException:
                WebDriverWait(self.driver, 3).until_not(
                    expected_conditions.visibility_of_element_located(CommonLocators.OVERLAY))
                continue

    def wait_for_url(self, url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

    def wait_class_be_current(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_attribute_to_include(locator, 'current'))

    def wait_element_disappear(self, locator):
        WebDriverWait(self.driver, 3).until_not(
            expected_conditions.visibility_of_element_located(locator))
