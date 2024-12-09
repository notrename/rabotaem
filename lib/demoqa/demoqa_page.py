from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page


class DemoqaPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_demoqa_form(self):
        url = "https://demoqa.com/automation-practice-form"
        self.open_site(url)
        return True