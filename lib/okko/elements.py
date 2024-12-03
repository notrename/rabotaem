from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lib.okko.okko_page import OkkoPage

class Elements(OkkoPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.find()

    @staticmethod
    def find():
        xpath = "//nav//button"
        return xpath

