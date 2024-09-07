from variables import URL_ACCOUNT, URL_ORDER_HISTORY
from account_page import AccountPage
from locators import CommonLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAccountPage:

    def test_logged_in_go_to_personal_account_page(self, driver, register_user, log_in_page):
        log_in_page.go_to_personal_account()
        assert driver.current_url == URL_ACCOUNT, \
            f'{driver.current_url=} is not equal {URL_ACCOUNT}'

    def test_logged_in_go_to_order_history_page(self, driver, register_user, log_in_page):
        log_in_page.go_to_personal_account()

        account_page = AccountPage(driver)
        account_page.click_on_order_history()

        assert driver.current_url == URL_ORDER_HISTORY, \
            f'{driver.current_url=} is not equal {URL_ORDER_HISTORY}'

    def test_logged_in_log_off_from_personal_account(self, driver, register_user, log_in_page):
        log_in_page.go_to_personal_account()

        account_page = AccountPage(driver)
        account_page.click_on_logoff_button()

        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            CommonLocators.LOGIN_BUTTON))
