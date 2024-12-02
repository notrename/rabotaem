import pytest

from conftest import browser
from lib.okko.okko_page import OkkoPage

class TestOkkoPage:
    @pytest.fixture(autouse=True)
    def setup(self, okko_web_page: OkkoPage):
        self.page = okko_web_page  # Устанавливаем значение в фикстуре

    def test_open_main_page(self):
        """Шаг 1: Открываем главную страницу."""
        self.page.open_okko()

    def test_clickable(self):
        self.page.open_okko()
        self.page.element_is_clickable('//*[@id="root"]/div[2]/div[1]/div[2]/article[2]/div/div[1]/div[2]/a/button')

    def test_click_element(self):
        self.page.open_okko()
        self.page.click_element('//*[@id="root"]/div[2]/div[1]/div[2]/article[2]/div/div[1]/div[2]/a/button')

