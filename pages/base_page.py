import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators


class BasePage():
    #получаем браузер и ссылку
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    #открываем ссылку в браузере
    def open(self):
        self.browser.get(self.url)

    #перейти на страницу корзины
    def go_to_basket_page(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Backet link is not presented"
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    #перейти на страницу логина
    def go_to_login_page(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    #есть ли ссылка которая ведет на логин
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    #ищем есть ли элемент на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    #сравнить два элемента
    def compare_items(self, how, what,how_two, what_two):
        first = self.browser.find_element(how, what).text
        second = self.browser.find_element(how_two, what_two).text
        if first != second:
            return False
        return True

    #Элемент не появляется на странице в течении заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    #Элемент исчезнет в течении заданного времени
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    #проверяем что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

