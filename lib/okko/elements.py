from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lib.okko.okko_page import OkkoPage

class Elements(OkkoPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.find()
        self.proceed()

    @staticmethod
    def find():
        xpath = str("//nav//a[contains(text(), 'Войти')]")
        return xpath

    @staticmethod
    def proceed():
        xpath = str('//*[@id="root"]/div')
        return xpath
