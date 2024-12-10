from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DemoQaCheckBoxElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def toggle_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="tree-node"]/ol/li/span/button'
        )

    @property
    def desktop_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Desktop"]'
        )

    @property
    def documents_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Documents"]'
        )

    @property
    def downloads_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Downloads"]'
        )

    @property
    def open_icon(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="tree-node"]/ol/li/span/label/span[2]/svg'
        )
