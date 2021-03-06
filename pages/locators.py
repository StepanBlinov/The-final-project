from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")

class ProductPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, ".btn-lg.btn-primary")
    
    FORM_OF_GOODS = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    NAME_OF_GOODS = (By.CSS_SELECTOR, ".product_main h1")
    
    BASKET_VALUE = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")
    PRICE_OF_GOODS = (By.CSS_SELECTOR, "p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    FORM_OF_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    NAME_OF_GOODS_IN_BASKER = (By.CSS_SELECTOR, ".col-sm-4 h3 a")



