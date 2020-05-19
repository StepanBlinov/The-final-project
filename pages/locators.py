from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, ".btn-lg.btn-primary")
    
    FORM_OF_GOODS = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    NAME_OF_GOODS = (By.CSS_SELECTOR, ".product_main h1")
    
    BASKET_VALUE = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")
    PRICE_OF_GOODS = (By.CSS_SELECTOR, "p.price_color")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    