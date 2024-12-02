from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page

class OkkoPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_okko_check(self):
        self.logger.warning('Запуск тест-сьюта Okko')
        self.logger.info('Запуск теста открытия главной страницы сайта Okko')
        """Открывает сайт Okko."""
        url = "https://okko.tv/?clientSessionId=19386d65-b2f9-7aaa-38f0-2f0bedf22974&sso=false"
        self.open_site(url)
        self.logger.info('Тест пройден')
        self.logger.warning('Запуск следующего теста')
        return True

    def open_okko(self):
        url = "https://okko.tv/?clientSessionId=19386d65-b2f9-7aaa-38f0-2f0bedf22974&sso=false"
        self.open_site(url)
        return True

    def find_element_in_dom_tree(self, xpath=None):
        self.logger.info('Запуск теста поиска элемента')
        self.open_okko()
        self.xpath_is_present(xpath=xpath, silent = True)
        self.logger.info('Тест пройден')
        self.logger.warning('Запуск следующего теста')

    def okko_page_element_is_clickable(self, xpath=None):
        self.logger.info('Запуск теста кликабельности элемента')
        self.open_okko()
        self.element_is_clickable(xpath=xpath)
        self.refresh()
        self.logger.info('Тест пройден')
        self.logger.warning('Запуск следующего теста')

    def okko_page_click_to_element(self, xpath=None):
        self.logger.info('Запуск теста клика по элементу')
        self.open_okko()
        self.click_element(xpath=xpath)
        self.refresh()
        self.logger.info('Тест пройден')
        self.logger.warning('Конец записей логирования')