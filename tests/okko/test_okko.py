import pytest
from lib.okko.okko_page import OkkoPage

class TestOkkoPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, okko_web_page: OkkoPage):
        self.page = okko_web_page  # Устанавливаем значение в фикстуре

    def test_open_main_page(self):
        """Шаг 1: Открываем главную страницу."""
        self.page.open_okko()