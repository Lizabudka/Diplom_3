from variables import URL_ACCOUNT, URL_ORDER_HISTORY
from account_page import AccountPage
from locators import CommonLocators


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

        assert account_page.wait_element_be_visible(CommonLocators.LOGIN_BUTTON), \
            f'Element did not appear {CommonLocators.LOGIN_BUTTON}'
