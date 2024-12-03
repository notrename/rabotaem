import pytest
from conftest import browser
from lib.okko.fixturies import okko_web_page
from lib.okko.okko_page import OkkoPage
from lib.okko.elements import Elements

class TestOkkoPage:
    @pytest.fixture(autouse=True)
    def setup(self, okko_web_page: OkkoPage):
        self.page = okko_web_page  # Устанавливаем значение в фикстуре
        self.element = Elements

    def test_open_main_page(self):
        self.page.open_okko_check()

    def test_find(self):
        self.page.find_element_in_dom_tree(self.element.find())

    def test_clickable(self):
        self.page.okko_page_element_is_clickable(self.element.find())

    def test_click(self):
        self.page.okko_page_click_to_element(self.element.find())

    def test_click_and_proceed(self):
        self.page.click_and_proceed(xpath=self.element.find(), expected_xpath=self.element.proceed())



