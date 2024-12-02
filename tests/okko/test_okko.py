import pytest
from conftest import browser
from lib.okko.okko_page import OkkoPage
from utils.logger import Logger

# Конфигурируем логер
logger = Logger().get_logger()  # Получаем логер
i = logger.info # Упрощаем код

class TestOkkoPage:
    @pytest.fixture(autouse=True)
    def setup(self, okko_web_page: OkkoPage):
        self.page = okko_web_page  # Устанавливаем значение в фикстуре

    def test_open_main_page(self):
        test_name = '"Открытие главной страницы'
        i(f'Запускаем тест {test_name}')
        self.page.open_okko()
        i(f'Тест {test_name} завершён\n\n')

    def test_find_element_in_dom_tree(self):
        test_name = 'Поиск элемента'
        i(f'Запускаем тест {test_name}')
        self.page.open_okko()
        self.page.xpath_is_present('//*[@id="root"]/div[2]/div[1]/div[2]/article[2]/div/div[1]/div[2]/a/button')
        i(f'Тест {test_name} завершён\n\n')

    def test_clickable(self):
        test_name = 'Кликабельность элемента'
        i(f'Запускаем тест {test_name}')
        self.page.open_okko()
        self.page.element_is_clickable('//*[@id="root"]/div[2]/div[1]/div[2]/article[2]/div/div[1]/div[2]/a/button')
        i(f'Тест {test_name} завершён\n\n')

    def test_click_element(self):
        test_name = 'Клик по элементу'
        i(f'Запускаем тест {test_name}')
        self.page.open_okko()
        self.page.click_element('//*[@id="root"]/div[2]/div[1]/div[2]/article[2]/div/div[1]/div[2]/a/button')
        i(f'Тест {test_name} завершён\n\n')

