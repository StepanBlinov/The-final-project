import pytest
from pages.product_page import ProductPageMissingEl


@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPageMissingEl(browser, link)
    page.open()#Открываем страницу товара
    page.adding_an_item_to_the_cart()#добавляем товар в корзину
    page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPageMissingEl(browser, link)
    page.open()#Открываем страницу товара
    page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPageMissingEl(browser, link)
    page.open()#Открываем страницу товара
    page.adding_an_item_to_the_cart()#добавляем товар в корзину
    page.the_element_should_disappear()#Проверяем, что нет сообщения об успехе с помощью is_disappeared
