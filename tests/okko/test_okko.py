import pytest
from conftest import browser
from lib.okko.fixturies import okko_web_page
from lib.okko.okko_page import OkkoPage

class TestOkkoPage:
    @pytest.fixture(autouse=True)
    def setup(self, okko_web_page: OkkoPage):
        self.page = okko_web_page  # Устанавливаем значение в фикстуре

    def test_open_main_page(self):
        self.page.open_okko_check()

    def test_find(self):
        self.page.find_element_in_dom_tree("//nav//button")

    def test_clickable(self):
        self.page.okko_page_element_is_clickable("//nav//button")

    def test_click(self):
        self.page.okko_page_click_to_element("//nav//button")


