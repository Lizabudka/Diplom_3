import allure
import pytest
from variables import URL_MAIN_PAGE, URL_ORDER_FEED, DESCRIPTION_TEXT, INGREDIENT_COUNTER, ORDER_ID_TEXT
from main_page import MainPage
from login_page import LoginPage
from locators import MainPageLocators


class TestMainFunctions:

    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_constructor_page(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()

        main_page = MainPage(driver)
        main_page.click_on_constructor()

        assert driver.current_url == URL_MAIN_PAGE, \
            f'{driver.current_url=} is not equal to {URL_MAIN_PAGE}'

    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_order_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_order_feed()

        assert driver.current_url == URL_ORDER_FEED, \
            f'{driver.current_url=} is not equal to {URL_ORDER_FEED}'

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @pytest.mark.parametrize('ingredient_list', [MainPageLocators.BUNS_LIST,
                                                 MainPageLocators.SAUCES_LIST,
                                                 MainPageLocators.INGREDIENTS_LIST])
    def test_click_on_ingredient_details_pop_up(self, driver, get_random_element, ingredient_list):
        main_page = MainPage(driver)
        main_page.go_to_main_page()

        random_ingredient = get_random_element.get_element_from_list(ingredient_list)
        main_page.scroll_to_element(random_ingredient)
        description_text = main_page.click_on_ingredient(random_ingredient)

        assert description_text == DESCRIPTION_TEXT, \
            f'Expecting {DESCRIPTION_TEXT=}, but {description_text=} occurred'

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_window(self, driver, get_random_element):
        main_page = MainPage(driver)
        main_page.go_to_main_page()

        random_bun = get_random_element.get_element_from_list(MainPageLocators.BUNS_LIST)
        main_page.click_on_ingredient(random_bun)

        assert main_page.close_description_window(MainPageLocators.DESCRIPTION_CANCEL_BUTTON), \
            f'Element was not closed {MainPageLocators.DESCRIPTION_CANCEL_BUTTON}'

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @pytest.mark.parametrize('number_of_ingredients', [0, 1, 2])
    def test_add_ingredients_to_order_counter_increases(self, driver, get_random_element,
                                                        number_of_ingredients):
        main_page = MainPage(driver)
        main_page.go_to_main_page()

        random_ingredient = get_random_element.get_element_from_list(MainPageLocators.INGREDIENTS_LIST)
        main_page.scroll_to_element(random_ingredient)

        with allure.step('Перетаскиваем все ингридиенты в констуктор бургера'):
            for i in range(1, number_of_ingredients+1):
                main_page.drag_element_to_order(random_ingredient)
                ingredient_locator = (MainPageLocators.BASKET_LIST[0],
                                      f'{MainPageLocators.BASKET_LIST[1]}[{i}]')
                main_page.wait_element_be_visible(ingredient_locator)

        counter = int(driver.find_element(random_ingredient[0],
                                          f'{random_ingredient[1]}{INGREDIENT_COUNTER}').text)
        assert counter == number_of_ingredients, \
            (f'expected {number_of_ingredients=}, but actual number is {counter}, '
             f'{random_ingredient[1]}{INGREDIENT_COUNTER}')

    @allure.title('Залогиненный пользователь может оформить заказ.')
    def test_create_order_for_logged_user(self, driver, register_user, log_in_page,
                                          get_random_element, create_order, ingredients_for_order):
        log_in_page.go_to_main_page()
        main_page = MainPage(driver)

        list_for_order = ingredients_for_order.get_ingredients_for_order()
        order_info = create_order.create_order_from_list(list_for_order, main_page)

        assert order_info[0] == ORDER_ID_TEXT, \
            f'waiting for text {ORDER_ID_TEXT=} but got {order_info[0]=}'
