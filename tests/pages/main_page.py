from common_objects import Page
from locators import CommonLocators, MainPageLocators
from variables import URL_MAIN_PAGE


class MainPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_main_page(self):
        self.driver.get(URL_MAIN_PAGE)
        self.wait_element_be_visible(MainPageLocators.MAKE_BURGER_TEXT)

    def click_on_constructor(self):
        self.try_click_on_element(CommonLocators.CONSTRUCTOR_BUTTON)
        self.wait_element_be_visible(MainPageLocators.MAKE_BURGER_TEXT)

    def click_on_order_feed(self):
        self.try_click_on_element(CommonLocators.ORDER_FEED_BUTTON)
        self.wait_element_be_visible(MainPageLocators.ORDER_FEED_TEXT)

    def click_on_ingredient(self, ingredient_locator):
        self.try_click_on_element(ingredient_locator)
        self.wait_element_be_visible(MainPageLocators.INGREDIENT_DESCRIPTION)
        description_text = self.driver.find_element(*MainPageLocators.INGREDIENT_DESCRIPTION).text
        return description_text

    def click_on_constructor_buns(self):
        self.try_click_on_element(MainPageLocators.BUNS_BUTTON)
        self.wait_class_be_current(MainPageLocators.BUNS_BUTTON)

    def get_elements_list(self, locator):
        element_list = self.driver.find_elements(*locator)
        return element_list

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    def close_description_window(self, locator):
        self.try_click_on_element(locator)
        self.wait_element_disappear(locator)
        return True
