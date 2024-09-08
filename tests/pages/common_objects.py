from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import CommonLocators
import allure


class Page:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_be_visible(self, locator):
        with allure.step(f'Waiting for {locator=} be visible'):
            WebDriverWait(self.driver, 3).until(
                    expected_conditions.visibility_of_element_located(locator))
        return True

    @allure.step('Trying to click on element')
    def try_click_on_element(self, locator):
        while True:
            try:
                self.driver.find_element(*locator).click()
                break
            except ElementClickInterceptedException:
                with allure.step('ElementClickInterceptedException occurred, '
                                 'trying to wait till overlay disappear and clicking again'):
                    try:
                        WebDriverWait(self.driver, 3).until_not(
                            expected_conditions.visibility_of_element_located(CommonLocators.OVERLAY))
                    except TimeoutException:
                        with allure.step('TimeoutException occurred, trying to click again'):
                            continue
                    continue

    def wait_for_url(self, url):
        with allure.step(f'Waiting for url to be {url}'):
            WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

    def wait_element_disappear(self, locator):
        with allure.step(f'Waiting for {locator=} to disappear'):
            WebDriverWait(self.driver, 3).until_not(
                expected_conditions.visibility_of_element_located(locator))
