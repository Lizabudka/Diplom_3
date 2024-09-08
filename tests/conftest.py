import random
import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_Options
from selenium.webdriver.firefox.options import Options as firefox_Options
from pages.variables import name, email, password, URL_API_REGISTER, URL_API_AUTH
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.step(f'Открытие окна браузера')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    with allure.step(f'Браузер {request.param}'):
        if request.param == 'firefox':
            firefox_options = firefox_Options()
            firefox_options.add_argument('--width=1920')
            firefox_options.add_argument('--height=1080')
            driver = webdriver.Firefox(options=firefox_options)
        elif request.param == 'chrome':
            chrome_options = chrome_Options()
            chrome_options.add_argument('--window-size=1920,1080')
            driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@allure.step(f'Регистрация пользователя через API с данными {email=}, {password=}, {name=}')
@pytest.fixture()
def register_user(driver):
    response = requests.post(URL_API_REGISTER, data={'email': email,
                                                     'password': password,
                                                     'name': name})
    yield response
    with allure.step(f'Удаление пользователя по токену {response.json()['accessToken']}'):
        token = response.json()['accessToken']
        requests.delete(URL_API_AUTH, headers={'Authorization': token})


@allure.step(f'Логин пользователя с данными {email=}, {password=}, {name=}')
@pytest.fixture()
def log_in_page(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.log_in()
    return login_page


@allure.step(f'Получение случайного элемента списка')
@pytest.fixture()
def get_random_element(driver):
    class Dummy:
        @staticmethod
        def get_element_from_list(locator):
            main_page = MainPage(driver)
            elements_list = main_page.get_elements_list(locator)
            random_element_num = random.randrange(1, len(elements_list))
            random_element_locator = locator[0], f'{locator[1]}[{random_element_num}]'
            return random_element_locator
    return Dummy


@allure.step(f'Получение номеров заказов')
@pytest.fixture()
def get_order_num(driver):
    class Dummy:
        @staticmethod
        def get_num_from_list(locator, postfix):
            main_page = MainPage(driver)
            elements_list = main_page.get_elements_list(locator)
            order_num_list = []
            for i in range(0, len(elements_list)):
                order_num = driver.find_element(
                    locator[0], f'{locator[1]}[{i+1}]/{postfix}').text
                order_num_list.append(order_num)
            return order_num_list
    return Dummy


@allure.step(f'Получение списка ингридиентов для заказа')
@pytest.fixture()
def ingredients_for_order(get_random_element):
    class Dummy:
        @staticmethod
        def get_ingredients_for_order():
            random_bun = get_random_element.get_element_from_list(MainPageLocators.BUNS_LIST)
            random_ingredient_1 = get_random_element.get_element_from_list(MainPageLocators.INGREDIENTS_LIST)
            random_ingredient_2 = get_random_element.get_element_from_list(MainPageLocators.INGREDIENTS_LIST)
            list_for_order = [random_bun, random_ingredient_1, random_ingredient_2]
            return list_for_order
    return Dummy


@allure.step(f'Создание заказа из полученного списка')
@pytest.fixture()
def create_order(driver):
    class Dummy:
        @staticmethod
        def create_order_from_list(list_for_order, main_page):
            with allure.step(f'Создаем заказы в кол-ве {list_for_order}, перетаскиваем игнридиенты в конструктор'):
                for i in list_for_order:
                    main_page.scroll_to_element(i)
                    main_page.drag_element_to_order(i)
                    if list_for_order[0] == i:
                        main_page.wait_element_disappear(MainPageLocators.EMPTY_BUN_IN_ORDER)
                    else:
                        ingredient_locator = (MainPageLocators.BASKET_LIST[0],
                                              f'{MainPageLocators.BASKET_LIST[1]}[{list_for_order.index(i)}]')
                        main_page.wait_element_be_visible(ingredient_locator)

            with allure.step('Клик на кнопку заказа'):
                main_page.click_order_button(MainPageLocators.ORDER_BUTTON)
            with allure.step('Поиск теста с индикацией заказа'):
                order_text = driver.find_element(*MainPageLocators.ORDER_INDICATOR_TEXT).text
            with allure.step('Лжидание замены дефолтного номера на номер заказа'):
                main_page.wait_element_disappear(MainPageLocators.ORDER_NUM_DEFAULT)
                order_num = driver.find_element(*MainPageLocators.ORDER_NUM).text
            return order_text, order_num
    return Dummy


@allure.step(f'Полный цикл создания заказа')
@pytest.fixture()
def create_order_end_to_end(ingredients_for_order, create_order):
    class Dummy:
        @staticmethod
        def create_order_and_close_window(main_page):
            list_for_order = ingredients_for_order.get_ingredients_for_order()
            order_info = create_order.create_order_from_list(list_for_order, main_page)
            main_page.close_description_window(MainPageLocators.DESCRIPTION_CANCEL_BUTTON)
            return order_info
    return Dummy
