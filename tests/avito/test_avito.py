import pytest
from lib.avito.avito_page import AvitoPage
from lib.avito.fixtures import avito_web_page

class TestAvitoPage:
    @pytest.fixture(autouse=True)
    def setup(self, avito_web_page: AvitoPage):
        self.page = avito_web_page  # Устанавливаем значение в фикстуре

    def test_open_main_page(self):
        self.page.open_avito_check()

    def test_find(self):
        self.page.avito_element_is_visible()

    def test_clickable(self):
        self.page.avito_send_keys_to_input()
