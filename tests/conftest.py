import random
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_Options
from selenium.webdriver.firefox.options import Options as firefox_Options
from variables import name, email, password, URL_API_REGISTER, URL_API_AUTH
from login_page import LoginPage
from main_page import MainPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
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


@pytest.fixture()
def register_user(driver):
    response = requests.post(URL_API_REGISTER, data={'email': email,
                                                     'password': password,
                                                     'name': name})
    yield response
    token = response.json()['accessToken']
    requests.delete(URL_API_AUTH, headers={'Authorization': token})


@pytest.fixture()
def log_in_page(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.log_in()
    return login_page


@pytest.fixture()
def get_random_element(driver):
    class Dummy:
        @staticmethod
        def get_element_from_list(locator):
            main_page = MainPage(driver)
            buns = main_page.get_elements_list(locator)
            random_ingredient_num = random.randrange(1, len(buns))
            random_bun_locator = locator[0], f'{locator[1]}[{random_ingredient_num}]'
            return random_bun_locator
    return Dummy
