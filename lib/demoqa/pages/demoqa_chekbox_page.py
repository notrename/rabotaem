from selenium.webdriver.remote.webdriver import WebDriver

from lib.demoqa.elements.demoqa_chekbox_page_elements import DemoQaCheckBoxElements
from utils.page import Page


class DemoQaCheckBoxPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://demoqa.com/checkbox'
        self.__driver = driver
        self.elems = DemoQaCheckBoxElements(driver=driver)