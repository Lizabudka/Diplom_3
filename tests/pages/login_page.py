from selenium.common import TimeoutException
from common_objects import Page
from variables import URL_LOGIN, email, password, URL_MAIN_PAGE
from locators import (LogInPageLocators, ResetPageLocators, CommonLocators,
                      MainPageLocators, AccountPageLocators)


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.driver.get(URL_LOGIN)
        self.wait_element_be_visible(LogInPageLocators.RESET_PASS_LINK)

    def click_on_reset_pass_button(self):
        self.try_click_on_element(LogInPageLocators.RESET_PASS_LINK)
        self.wait_element_be_visible(ResetPageLocators.RECOVER_BUTTON)

    def input_email_field(self):
        self.driver.find_element(*LogInPageLocators.EMAIL_FIELD).send_keys(email)

    def input_password_field(self):
        self.driver.find_element(*CommonLocators.PASSWORD_FIELD).send_keys(password)

    def click_on_login_button(self):
        self.try_click_on_element(CommonLocators.LOGIN_BUTTON)
        self.wait_element_be_visible(MainPageLocators.ACCOUNT_LINK)

    def log_in(self):
        self.input_email_field()
        self.input_password_field()
        self.click_on_login_button()

    def go_to_personal_account(self):
        self.try_click_on_element(MainPageLocators.ACCOUNT_LINK)
        try:
            self.wait_element_be_visible(AccountPageLocators.EMAIL)
        except TimeoutException:
            self.try_click_on_element(MainPageLocators.ACCOUNT_LINK)
            self.wait_element_be_visible(AccountPageLocators.EMAIL)

    def go_to_main_page(self):
        self.try_click_on_element(CommonLocators.CONSTRUCTOR_BUTTON)
        self.wait_element_be_visible(MainPageLocators.MAKE_BURGER_TEXT)

    def go_to_orders_feed(self):
        self.try_click_on_element(CommonLocators.ORDER_FEED_BUTTON)
        self.wait_element_be_visible(MainPageLocators.ORDER_FEED_TEXT)
