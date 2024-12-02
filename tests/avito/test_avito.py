import pytest
from conftest import browser
from lib.avito.avito_page import AvitoPage
from utils.logger import Logger

# Конфигурируем логер
logger = Logger().get_logger()  # Получаем логер
i = logger.info # Упрощаем код

class TestAvitoPage:
    @pytest.fixture(autouse=True)
    def setup(self, avito_web_page: AvitoPage):
        self.page = avito_web_page  # Устанавливаем значение в фикстуре

    def test_open_main_page(self):
        test_name = '"Открытие главной страницы'
        i(f'Запускаем тест {test_name}')
        assert self.page.open_avito(), i(f'Тест {test_name} провален\n\n')
        i(f'Тест {test_name} завершён\n\n')

    def test_element_is_visible(self):
        test_name = 'Проверка видимости элемента'
        i(f'Запускаем тест {test_name}')
        self.page.open_site('https://www.avito.ru/')
        assert self.page.element_is_visible('//*[@id="app"]/div/buyer-location/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div[2]/button', timeout=5), i(f'Тест {test_name} провален\n\n')
        i(f'Тест {test_name} завершён\n\n')

    def test_send_keys_to_input(self):
        test_name = 'Отправка текста в инпут'
        i(f'Запускаем тест {test_name}')
        self.page.open_site('https://www.avito.ru/')
        assert self.page.send_keys_to_input('/html/body/div[1]/div/buyer-location/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div[1]/div/div/label/div/div/input', 'Lexus GS 350', timeout=5), i(f'Тест {test_name} провален\n\n')
        i(f'Тест {test_name} завершён\n\n')