import pytest
import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)#оборачиваем каждый тест функцией setup внутри класса
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()  #переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)  # передаем актуальный url в браузер
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email,"qqqqqqq89")
        login_page.should_be_authorized_user()

    # открываем страницу товара, проверяем появится ли там элемент
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()  # Открываем страницу товара
        page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    # тест на добавление товара в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_product_page()  # выполняем поиск элемента на странице промо и добавляем в корзину
        Product_page = ProductPage(browser, browser.current_url)  # передаем актуальный url в браузер
        Product_page.compare_the_name()  # сравниваем имя товара в корзине с именем товара, который добавляли
        Product_page.with_price_comparison()  # сравниваем цену товара в корзине с ценой, товара который добавляли


#параметризация, проверяем несоколько страниц промоакций на налчие бага
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #помечаем падающий тест как xfail
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

#тест на добавление товара в корзину
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser,link):
    link = link
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_product_page()  # выполняем поиск элемента на странице промо и добавляем в корзину 
    Product_page = ProductPage(browser, browser.current_url)#передаем актуальный url в браузер
    Product_page.compare_the_name()#сравниваем имя товара в корзине с именем товара, который доавляли
    Product_page.with_price_comparison()#сравниваем цену товара в корщине с ценой, товара который добавляли

#тест на проверку ссылки логина на странице
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#тест на проверку перехода на страницу логина
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

#добавляем товар в корзину , проверям повяится ли там элимент
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()#Открываем страницу товара
    page.adding_an_item_to_the_cart()#добавляем товар в корзину
    page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present

#открываем страницу товара, проверяем появится ли там элемент
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()#Открываем страницу товара
    page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present

#добавляем товар в корзину, проверям исчезнет ли элимент элимент
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()#Открываем страницу товара
    page.adding_an_item_to_the_cart()#добавляем товар в корзину
    page.the_element_should_disappear()#Проверяем, что нет сообщения об успехе с помощью is_disappeared

#переходим в корзину со станицы товара и выполняем проверки
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()#переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.search_in_the_basket() #проверяем, что в корзине нет товара
    basket_page.the_basket_is_empty()#проверяем, что есть текст о том что корзина пуста


