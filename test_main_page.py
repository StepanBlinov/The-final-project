import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginMainPage():
    #Переходим на страницу логина и делаем проверку формы
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  #переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)#получаем текущюю ссылку и предаем ее в браузер
        login_page.should_be_login_page()#проверям страницу логина

    #Проверяем, что есть ссылка, которая ведет на логин
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()#проверяем есть ли ссылка, которая ведет на логин


#переходим в корзину с главной страницы и выполняем проверки
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()#переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.search_in_the_basket()#проверяем, что в корзине нет товара
    basket_page.the_basket_is_empty()#проверяем, что есть текст о том что корзина пуста
    
