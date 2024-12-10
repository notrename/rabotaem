from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DemoQaElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def header(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=str('//header/a/img')
        )

    def element_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=f'//div[@class="card-body"]/h5[text()="Elements"]'
        )

    def checkbox_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=f'//li[span[text()="Check Box"]]'
        )

    def webtables_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=f'//li[span[text()="Web Tables"]]'
        )

    def uploaddownload_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=f'//li[span[text()="Upload and Download"]]'
        )