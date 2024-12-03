from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page
from lib.avito.elements.avito_page_elements import AvitoPageElements

class AvitoPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.__elements = AvitoPageElements(driver=driver)


    @property
    def elems(self):
        return self.__elements

    def open_avito(self):
        url = 'https://www.avito.ru/'
        self.open_site(url)
        return True

    def open_avito_check(self):
        self.logger.warning('Запуск тест-сьюта Avito')
        self.logger.info('Запуск теста открытия главной страницы сайта Avito')
        """Открывает сайт Avito."""
        url = 'https://www.avito.ru/'
        self.open_site(url)
        self.logger.info('Тест пройден')
        self.logger.warning('Запуск следующего теста')
        return True

    def avito_element_is_visible(self):
        self.logger.info('Запуск теста отображения элемента')
        self.open_avito()
        self.element_is_visible(self.elems.button_search, timeout=0)
        self.logger.info('Тест пройден')
        self.logger.warning('Запуск следующего теста')

    def avito_send_keys_to_input(self):
        self.logger.info('Запуск теста строки ввода')
        self.open_avito()
        self.send_keys_to_input(self.elems.input_search, 'Lexus GS 350', timeout=0)
        self.logger.info('Тест пройден')
        self.logger.warning('Конец записей логирования')