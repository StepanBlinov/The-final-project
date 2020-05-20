from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    #проверяем, что в корзине нет товара
    def search_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NAME_OF_GOODS_IN_BASKER), \
            "There is an item in the basket, but it should not be there"

    #проверяем, что есть текст о том что корзина пуста
    def the_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.FORM_OF_BASKET), \
            "No message Trash is empty"
