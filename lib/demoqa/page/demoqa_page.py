import time
import webbrowser

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page


class DemoqaPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)

    def open_demoqa_form(self):
        self.open_site(url='https://demoqa.com/automation-practice-form')

    def close_browser(self):
        self.__driver.quit()  # Закрывает все окна браузера и завершает сессию WebDriver

    def find_element_in_dom_tree(self, xpath=None):
        self.xpath_is_present(xpath=xpath, silent = True)


