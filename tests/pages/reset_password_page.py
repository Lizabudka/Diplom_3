import allure
from common_objects import Page
from locators import ResetPageLocators, CommonLocators
from variables import email, password, URL_FORGOT_PASS


class ResetPasswordPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу со сбросом пароля')
    def go_to_reset_password_page(self):
        self.driver.get(URL_FORGOT_PASS)

    @allure.step('Ввод email')
    def input_email(self):
        self.driver.find_element(*ResetPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.step('Клик на кнопку восстановления пароля')
    def click_recovery_button(self):
        self.try_click_on_element(ResetPageLocators.RECOVER_BUTTON)
        self.wait_element_be_visible(CommonLocators.PASSWORD_FIELD)

    @allure.step('Ввод пароля')
    def input_password(self):
        self.driver.find_element(*CommonLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step('Клик на кнопку отображения пароля')
    def click_on_visibility_icon(self):
        self.try_click_on_element(ResetPageLocators.VISIBILITY_ICON)
        return self.driver.find_element(*CommonLocators.PASSWORD_DIV).get_attribute("class")

    @allure.step('Цикл восстановление пароля')
    def reset_password(self):
        self.input_email()
        self.click_recovery_button()
        self.input_password()
        password_div = self.click_on_visibility_icon()
        return password_div
