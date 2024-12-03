from asyncio import timeout
from idlelib.run import exit_now

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page

class OkkoPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_okko_check(self):
        url = "https://okko.tv/?clientSessionId=19386d65-b2f9-7aaa-38f0-2f0bedf22974&sso=false"
        self.open_site(url)
        return True

    def open_okko(self):
        url = "https://okko.tv/?clientSessionId=19386d65-b2f9-7aaa-38f0-2f0bedf22974&sso=false"
        self.open_site(url)
        return True

    def find_element_in_dom_tree(self, xpath=None):
        self.open_okko()
        self.xpath_is_present(xpath=xpath, silent = True)

    def okko_page_element_is_clickable(self, xpath=None):
        self.open_okko()
        self.element_is_clickable(xpath=xpath)
        self.refresh()

    def okko_page_click_to_element(self, xpath=None):
        self.open_okko()
        self.click_element(xpath=xpath)
        self.refresh()

    def click_and_proceed(self, xpath=None, expected_xpath=None):
        self.open_okko()
        self.click_to_proceed(xpath=xpath, expected_xpath=expected_xpath)

