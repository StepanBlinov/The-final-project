import time
from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
