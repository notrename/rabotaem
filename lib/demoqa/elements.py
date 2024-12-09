from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lib.demoqa.demoqa_page import DemoqaPage


class Elements(DemoqaPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @staticmethod
    def header_form():
        xpath = str('//*[@id="app"]/header')
        return xpath
