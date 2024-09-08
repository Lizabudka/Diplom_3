import allure
from .common_objects import Page
from .variables import URL_ORDER_HISTORY
from .locators import AccountPageLocators, CommonLocators, MainPageLocators


class AccountPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(f'Клик на кнопку "История заказов"')
    def click_on_order_history(self):
        self.try_click_on_element(AccountPageLocators.ORDER_HISTORY_LINK)
        self.wait_for_url(URL_ORDER_HISTORY)

    @allure.step(f'Клик на кнопку "Выход из аккаунта"')
    def click_on_logoff_button(self):
        self.try_click_on_element(AccountPageLocators.LOG_OFF_BUTTON)
        self.wait_element_be_visible(CommonLocators.LOGIN_BUTTON)

    @allure.step(f'Клик на кнопку хедера "Лента заказов"')
    def go_to_order_feed_page(self):
        self.try_click_on_element(CommonLocators.ORDER_FEED_BUTTON)
        self.wait_element_be_visible(MainPageLocators.ORDER_FEED_TEXT)
