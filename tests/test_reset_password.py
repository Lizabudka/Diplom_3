from variables import active_status
from login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from reset_password_page import ResetPasswordPage
from locators import ResetPageLocators, CommonLocators


class TestResetPassword:

    def test_go_to_reset_password_page(self, driver):
        login_page = LoginPage(driver)

        login_page.go_to_login_page()
        login_page.click_on_reset_pass_button()

        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ResetPageLocators.TITLE_RESET_PASS))

    def test_input_email_for_password_reset_go_to_next_page(self, driver):
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.go_to_reset_password_page()

        reset_pass_page.input_email()
        reset_pass_page.click_recovery_button()

        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            CommonLocators.PASSWORD_FIELD))

    def test_reset_password_input_data(self, driver):
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.go_to_reset_password_page()
        password_div = reset_pass_page.reset_password()

        assert (active_status in password_div,
                f' status: {active_status} should be in {password_div=}')
