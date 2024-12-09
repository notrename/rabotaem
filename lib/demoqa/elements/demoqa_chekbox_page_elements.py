from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DemoQaCheckBoxElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def toggle_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="tree-node"]/ol/li/span/button'
        )

    def desktop_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Desktop"]'
        )

    def documents_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Documents"]'
        )

    def downloads_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Downloads"]'
        )

    def open_icon(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//svg[contains(@class, "rct-icon-parent-open")]'
        )