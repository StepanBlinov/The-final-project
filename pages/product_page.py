from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def go_to_product_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket_link.click()
        self.solve_quiz_and_get_code()

    def compare_the_name(self):
        assert self.compare_items(*ProductPageLocators.FORM_OF_GOODS,
                                  *ProductPageLocators.NAME_OF_GOODS), "The product on the form is different"
        
    def with_price_comparison(self):
        assert self.compare_items(*ProductPageLocators.BASKET_VALUE,
                                  *ProductPageLocators.PRICE_OF_GOODS), "The price doesn't match"

