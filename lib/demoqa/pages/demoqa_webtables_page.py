from selenium.webdriver.remote.webdriver import WebDriver

from lib.demoqa.elements.demoqa_webtables_page_elements import DemoQaWebtablesElements
from utils.page import Page


class DemoQaWebtablesPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://demoqa.com/checkbox'
        self.__driver = driver
        self.elems = DemoQaWebtablesElements(driver=driver)