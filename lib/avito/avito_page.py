from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page

class AvitoPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_avito(self):
        url = 'https://www.avito.ru/'
        self.open_site(url)
        return True