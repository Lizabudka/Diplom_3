import allure

from common_objects import Page
from locators import CommonLocators, MainPageLocators
from variables import URL_MAIN_PAGE, URL_ORDER_FEED
from selenium.webdriver import ActionChains


class MainPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на главную страницу')
    def go_to_main_page(self):
        self.driver.get(URL_MAIN_PAGE)
        self.wait_element_be_visible(MainPageLocators.MAKE_BURGER_TEXT)

    @allure.step('Переход на страницу с лентой заказов')
    def go_to_order_feed_page(self):
        self.driver.get(URL_ORDER_FEED)
        self.wait_element_be_visible(MainPageLocators.ORDER_FEED_TEXT)

    @allure.step('Клик на кнопку конструктора')
    def click_on_constructor(self):
        self.try_click_on_element(CommonLocators.CONSTRUCTOR_BUTTON)
        self.wait_element_be_visible(MainPageLocators.MAKE_BURGER_TEXT)

    @allure.step('Клик на кнопку ленты заказов')
    def click_on_order_feed(self):
        self.try_click_on_element(CommonLocators.ORDER_FEED_BUTTON)
        self.wait_element_be_visible(MainPageLocators.ORDER_FEED_TEXT)

    @allure.step('Клик на ингридиент')
    def click_on_ingredient(self, ingredient_locator):
        self.try_click_on_element(ingredient_locator)
        self.wait_element_be_visible(MainPageLocators.INGREDIENT_DESCRIPTION)
        description_text = self.driver.find_element(*MainPageLocators.INGREDIENT_DESCRIPTION).text
        return description_text

    @allure.step('Получение списка элементов')
    def get_elements_list(self, locator):
        self.wait_element_be_visible(locator)
        element_list = self.driver.find_elements(*locator)
        return element_list

    @allure.step('Прокрутка до элемента')
    def scroll_to_element(self, random_ingredient):
        element = self.driver.find_element(*random_ingredient)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    @allure.step('Закрытие всплывающего окна')
    def close_description_window(self, locator):
        self.try_click_on_element(locator)
        self.wait_element_disappear(locator)
        return True

    @allure.step('Перетаскивание ингридиента в бургер')
    def drag_element_to_order(self, ingredient):
        basket = self.driver.find_element(*MainPageLocators.BURGER_ORDER)
        ingredient = self.driver.find_element(*ingredient)
        ActionChains(self.driver).drag_and_drop(ingredient, basket).perform()

    @allure.step('Нажатие кнопки оформления заказа')
    def click_order_button(self, locator):
        self.try_click_on_element(locator)
        self.wait_element_be_visible(MainPageLocators.ORDER_INDICATOR_TEXT)

    @allure.step('Получить кол-во заказов за все время')
    def get_total_orders(self):
        self.scroll_to_element(MainPageLocators.ORDERS_TOTAL)
        number = self.driver.find_element(*MainPageLocators.ORDERS_TOTAL).text
        return number

    @allure.step('Получить кол-во заказов за сегодня')
    def get_today_orders(self):
        self.scroll_to_element(MainPageLocators.ORDERS_TODAY)
        number = self.driver.find_element(*MainPageLocators.ORDERS_TODAY).text
        return number

    @allure.step('Получить заказ, который сейчас в работе')
    def get_order_at_work(self):
        self.wait_element_disappear(MainPageLocators.NO_ORDERS)
        order_num = self.driver.find_element(*MainPageLocators.ORDER_AT_WORK).text
        return order_num
