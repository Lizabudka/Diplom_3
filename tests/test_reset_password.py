from pages.variables import ACTIVE_STATUS
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.locators import ResetPageLocators, CommonLocators
import allure


class TestResetPassword:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_reset_password_page(self, driver):
        login_page = LoginPage(driver)

        login_page.go_to_login_page()
        login_page.click_on_reset_pass_button()

        assert login_page.wait_element_be_visible(ResetPageLocators.TITLE_RESET_PASS), \
            f'Element did not appear {ResetPageLocators.TITLE_RESET_PASS}'

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_for_password_reset_go_to_next_page(self, driver):
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.go_to_reset_password_page()

        reset_pass_page.input_email()
        reset_pass_page.click_recovery_button()

        assert reset_pass_page.wait_element_be_visible(CommonLocators.PASSWORD_FIELD), \
            f'Element did not appear {CommonLocators.PASSWORD_FIELD}'

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_reset_password_input_data(self, driver):
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.go_to_reset_password_page()
        password_div = reset_pass_page.reset_password()

        assert (ACTIVE_STATUS in password_div,
                f' status: {ACTIVE_STATUS} should be in {password_div=}')
