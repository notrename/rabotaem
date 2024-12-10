from selenium.webdriver.remote.webdriver import WebDriver

from lib.demoqa.elements.demoqa_uploaddownlad_page_elements import DemoQaUploadDownloadElements
from utils.page import Page


class DemoQaUploadDownloadPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://demoqa.com/checkbox'
        self.__driver = driver
        self.elems = DemoQaUploadDownloadElements(driver=driver)