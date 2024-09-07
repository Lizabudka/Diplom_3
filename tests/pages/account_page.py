from common_objects import Page
from variables import URL_ORDER_HISTORY
from locators import AccountPageLocators, CommonLocators


class AccountPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_order_history(self):
        self.try_click_on_element(AccountPageLocators.ORDER_HISTORY_LINK)
        self.wait_for_url(URL_ORDER_HISTORY)

    def click_on_logoff_button(self):
        self.try_click_on_element(AccountPageLocators.LOG_OFF_BUTTON)
        self.wait_element_be_visible(CommonLocators.LOGIN_BUTTON)
