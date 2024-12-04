from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lib.okko.okko_page import OkkoPage

class Elements(OkkoPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @staticmethod
    def find():
        # xpath = str("//nav//a[contains(text(), 'Войти')]")
        xpath = str('//*[@id="root"]/div[2]/div[1]/div[1]/header[1]/nav/div/div[2]/div/button')
        return xpath

    @staticmethod
    def proceed():
        # xpath = str('//*[@id="root"]/div')
        xpath = str('//*[@id="root"]/div/div[2]')
        return xpath

    @staticmethod
    def find_button():
        # xpath = str('//*[@id="root"]/div')
        xpath = str('//*[@id="root"]/div[2]/div[1]/div[1]/header[1]/nav/div/div[1]')
        return xpath

    @staticmethod
    def find_input_window():
        xpath = str('//*[@id="root"]/div[2]/div[1]/div[1]/header[1]/nav/div[1]/div/div[1]/form/div/div/input')
        return xpath

    @staticmethod
    def find_after_click_find_button():
        xpath = str('//*[@id="root"]/div[2]/div[1]/div[2]/section[1]/div/div[1]/div/div[1]/a/div/figure/footer/div/span')
        return xpath