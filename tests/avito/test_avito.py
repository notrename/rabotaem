import pytest
from lib.avito.avito_page import AvitoPage

class TestAvitoPage:
    @pytest.fixture(autouse=True)
    def setup(self, avito_web_page: AvitoPage):
        self.page = avito_web_page
    def test_open_main_page(self):
        self.page.open_site()