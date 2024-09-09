from selenium.webdriver.common.by import By


class CommonLocators:
    OVERLAY = By.XPATH, './/*[contains(@class, "Modal_modal_overlay")]'
    PASSWORD_FIELD = By.XPATH, './/*[text()="Пароль"]/parent::*/input'
    PASSWORD_DIV = By.XPATH, './/*[text()="Пароль"]/parent::div'
    LOGIN_BUTTON = By.XPATH, './/button[text()="Войти"]'
    CONSTRUCTOR_BUTTON = By.XPATH, './/*[text()="Конструктор"]'
    ORDER_FEED_BUTTON = By.XPATH, './/*[@href="/feed"]'


class MainPageLocators:
    RESET_PASS_LINK = By.XPATH, './/*[text()="Восстановить пароль"]'
    ACCOUNT_LINK = By.XPATH, './/*[text()="Личный Кабинет"]'

    MAKE_BURGER_TEXT = By.XPATH, './/*[text()="Соберите бургер"]'
    ORDER_FEED_TEXT = By.XPATH, './/*[text()="Лента заказов"]'

    INGREDIENT_DESCRIPTION = By.XPATH, './/*[text()="Детали ингредиента"]'
    DESCRIPTION_CANCEL_BUTTON = By.XPATH, './/button[contains(@class, "close")]'

    BUNS_BUTTON = By.XPATH, './/span[text()="Булки"]'
    SAUCES_BUTTON = By.XPATH, './/span[text()="Соусы"]'
    INGREDIENTS_BUTTON = By.XPATH, './/span[text()="Начинки"]'

    BUNS_LIST = By.XPATH, './/*[contains(@class, "menuContainer")]/ul[1]/a'
    SAUCES_LIST = By.XPATH, './/*[contains(@class, "menuContainer")]/ul[2]/a'
    INGREDIENTS_LIST = By.XPATH, './/*[contains(@class, "menuContainer")]/ul[3]/a'

    BURGER_ORDER = By.XPATH, './/ul[contains(@class, "BurgerConstructor_basket")]'
    BASKET_LIST = By.XPATH, './/span[contains(@class, "BurgerConstructor_basket")]/li'
    EMPTY_BUN_IN_ORDER = By.XPATH, './/*[@alt="Перетяните булочку сюда (верх)"]'

    ORDER_INDICATOR_TEXT = By.XPATH, './/*[text()="идентификатор заказа"]'
    ORDER_NUM_DEFAULT = By.XPATH, './/h2[text()="9999"]'
    ORDER_NUM = By.XPATH, './/h2[contains(@class, "Modal_modal__title_shadow")]'
    ORDER_BUTTON = By.XPATH, './/button[text()="Оформить заказ"]'

    FIRST_ORDER = By.XPATH, './/ul[contains(@class, "OrderFeed_list")]/li[1]'
    ORDERS_LIST = By.XPATH, './/ul[contains(@class, "OrderFeed_list")]/li'
    ORDER_WINDOW = By.XPATH, './/*[contains(@class, "Modal_orderBox")]'
    ORDER_CONSIST = By.XPATH, './/*[text()="Cостав"]'
    ORDER_ID = By.XPATH, './/*[contains(@class, "Modal_orderBox")]/*[contains(text(), "#0")]'

    ORDERS_TOTAL = By.XPATH, './/*[text()="Выполнено за все время:"]/parent::div/p[2]'
    ORDERS_TODAY = By.XPATH, './/*[text()="Выполнено за сегодня:"]/parent::div/p[2]'

    ORDER_AT_WORK = By.XPATH, './/ul[contains(@class, "orderListReady")]/li'
    NO_ORDERS = By.XPATH, './/*[contains(text(), "Все текущие заказы готовы!")]'


class ResetPageLocators:
    EMAIL_FIELD = By.XPATH, './/input'
    RECOVER_BUTTON = By.XPATH, './/button[text()="Восстановить"]'
    VISIBILITY_ICON = By.XPATH, './/*[text()="Пароль"]/parent::*/div'
    TITLE_RESET_PASS = By.XPATH, './/*[text()="Восстановление пароля"]'


class LogInPageLocators:
    RESET_PASS_LINK = By.XPATH, './/*[text()="Восстановить пароль"]'
    EMAIL_FIELD = By.XPATH, './/*[text()="Email"]/parent::*/input'


class RegisterPageLocators:
    EMAIL_FIELD = By.XPATH, './/*[text()="Email"]/parent::*/input'
    NAME_FIELD = By.XPATH, './/*[text()="Имя"]/parent::*/input'
    REG_BUTTON = By.XPATH, './/button[text()="Зарегистрироваться"]'


class AccountPageLocators:
    EMAIL = By.XPATH, './/*[text()="Логин"]'
    ORDER_HISTORY_LINK = By.XPATH, './/*[text()="История заказов"]'
    LOG_OFF_BUTTON = By.XPATH, './/button[text()="Выход"]'
    ORDER_NUM = By.XPATH, './/*[contains(text(), "#0")]'
    ORDER_LIST = By.XPATH, './/*[contains(@class, "OrderHistory_list")]/li'
