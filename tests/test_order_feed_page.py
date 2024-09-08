import pytest
from account_page import AccountPage
from main_page import MainPage
from locators import MainPageLocators, AccountPageLocators
from variables import ORDER_NUM_POSTFIX


class TestOrderFeed:

    def test_click_on_order_details_window_pop_up(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed_page()

        main_page.try_click_on_element(MainPageLocators.FIRST_ORDER)
        main_page.wait_element_be_visible(MainPageLocators.ORDER_WINDOW)

        assert (driver.find_element(*MainPageLocators.ORDER_CONSIST) and
                driver.find_element(*MainPageLocators.ORDER_ID),
                f'Данные о номере заказа и о его составе не найдены')

    @pytest.mark.parametrize('order_count', [1, 3])
    def test_orders_from_history_are_in_order_feed(self, driver, order_count, register_user,
                                                   log_in_page, get_order_num, create_order_end_to_end):
        log_in_page.go_to_main_page()
        main_page = MainPage(driver)

        for i in range(order_count):
            create_order_end_to_end.create_order_and_close_window(main_page)

        log_in_page.go_to_personal_account()
        account_page = AccountPage(driver)
        account_page.click_on_order_history()

        user_order_list = get_order_num.get_num_from_list(
            AccountPageLocators.ORDER_LIST, ORDER_NUM_POSTFIX)

        account_page.go_to_order_feed_page()
        all_orders_list = get_order_num.get_num_from_list(
            MainPageLocators.ORDERS_LIST, ORDER_NUM_POSTFIX)

        assert all(i in all_orders_list for i in user_order_list), \
            f'expecting that {user_order_list=} will be in {all_orders_list=}'

    def test_create_order_orders_total_amount_increases(self, driver, register_user,
                                                        log_in_page, create_order_end_to_end):
        log_in_page.go_to_orders_feed()

        main_page = MainPage(driver)
        total_orders = int(main_page.get_total_orders())
        main_page.click_on_constructor()

        create_order_end_to_end.create_order_and_close_window(main_page)

        main_page.click_on_order_feed()
        total_orders_new = int(main_page.get_total_orders())

        assert total_orders + 1 == total_orders_new

    def test_create_order_orders_today_amount_increases(self, driver, register_user,
                                                        log_in_page, create_order_end_to_end):
        log_in_page.go_to_orders_feed()

        main_page = MainPage(driver)
        today_orders = int(main_page.get_today_orders())
        main_page.click_on_constructor()

        create_order_end_to_end.create_order_and_close_window(main_page)

        main_page.click_on_order_feed()
        today_orders_new = int(main_page.get_today_orders())

        assert today_orders + 1 == today_orders_new

    def test_create_order_order_is_at_work(self, driver, register_user, log_in_page, create_order_end_to_end):
        log_in_page.go_to_main_page()
        main_page = MainPage(driver)

        order_info = create_order_end_to_end.create_order_and_close_window(main_page)

        main_page.click_on_order_feed()
        order_at_work = main_page.get_order_at_work()

        assert f'0{order_info[1]}' == order_at_work
