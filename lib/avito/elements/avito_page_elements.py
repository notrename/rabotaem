from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AvitoPageElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
    @property
    def button_search(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//button[@data-marker="search-form/submit-button"]',
        )

    @property
    def input_search(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//input[@data-marker="search-form/suggest/input"]',
        )
