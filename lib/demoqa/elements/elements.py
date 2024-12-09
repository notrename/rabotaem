from selenium.webdriver.remote.webdriver import WebDriver
from lib.demoqa.page.demoqa_page import DemoqaPage
from selenium.webdriver.common.by import By


class Elements(DemoqaPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @staticmethod
    def header_form():
        xpath = str('//*[@id="app"]/div/div/div/div[2]/div[2]/h5')
        return xpath
