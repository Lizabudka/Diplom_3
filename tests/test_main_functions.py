import pytest
from variables import URL_MAIN_PAGE, URL_ORDER_FEED, DESCRIPTION_TEXT
from main_page import MainPage
from login_page import LoginPage
from locators import MainPageLocators


class TestMainFunctions:

    def test_go_to_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()

        main_page = MainPage(driver)
        main_page.click_on_constructor()

        assert driver.current_url == URL_MAIN_PAGE, \
            f'{driver.current_url=} is not equal to {URL_MAIN_PAGE}'

    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_order_feed()

        assert driver.current_url == URL_ORDER_FEED, \
            f'{driver.current_url=} is not equal to {URL_ORDER_FEED}'

    @pytest.mark.parametrize('ingredient_list', [MainPageLocators.BUNS_LIST,
                                                 MainPageLocators.SAUCES_LIST,
                                                 MainPageLocators.INGREDIENTS_LIST])
    def test_click_on_ingredient_details_pop_up(self, driver, get_random_element, ingredient_list):
        main_page = MainPage(driver)
        main_page.go_to_main_page()

        random_ingredient = get_random_element.get_element_from_list(ingredient_list)
        element = driver.find_element(*random_ingredient)
        main_page.scroll_to_element(element)
        description_text = main_page.click_on_ingredient(random_ingredient)

        assert description_text == DESCRIPTION_TEXT

    def test_close_ingredient_details_window(self, driver, get_random_element):
        main_page = MainPage(driver)
        main_page.go_to_main_page()

        random_bun = get_random_element.get_element_from_list(MainPageLocators.BUNS_LIST)
        main_page.click_on_ingredient(random_bun)

        assert main_page.close_description_window(MainPageLocators.DESCRIPTION_CANCEL_BUTTON)
