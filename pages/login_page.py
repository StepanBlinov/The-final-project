from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    #проверка на корректный url адрес
    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "Error in the login url"
        
    #проверкa, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login field not found"
        
    #проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The registration field is not found"
        
    #регистрируем нового пользователя
    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        mail.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()

