import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    # выполняем поиск элемента на странице промо и добавляем в корзину на странице промо
    def go_to_product_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket_link.click()
        self.solve_quiz_and_get_code()

    # сравниваем имя товара в корзине с именем товара, который добавляли
    def compare_the_name(self):
        assert self.compare_items(*ProductPageLocators.FORM_OF_GOODS,
                                  *ProductPageLocators.NAME_OF_GOODS), "The product on the form is different"

    # сравниваем цену товара в корзине с ценой, товара который добавляли
    def with_price_comparison(self):
        assert self.compare_items(*ProductPageLocators.BASKET_VALUE,
                                  *ProductPageLocators.PRICE_OF_GOODS), "The price doesn't match"

    # добавляем товар в корзину
    def adding_an_item_to_the_cart(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket_link.click()

    # Проверяем, что элемент не появляется на странице
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.FORM_OF_GOODS), \
            "Success message is presented, but should not be"

    # Проверяем, исчез ли элемент
    def the_element_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.FORM_OF_GOODS), \
            "Success message is presented, but should not be"
    
    #метод для получения проверочного кода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

