from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page

class OkkoPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_okko(self):
        """Открывает сайт Okko."""
        url = "https://okko.tv/?clientSessionId=19386d65-b2f9-7aaa-38f0-2f0bedf22974&sso=false"
        self.open_site(url)