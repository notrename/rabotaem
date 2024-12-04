import pytest
from conftest import browser
from lib.okko.fixturies import okko_web_page
from lib.okko.okko_page import OkkoPage
from lib.okko.elements import Elements

class TestOkkoPage:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self, okko_web_page: OkkoPage):
        self.page = okko_web_page  # Устанавливаем значение в фикстуре
        self.element = Elements

    def test_open_main_page(self):
        self.page.open_okko_check()

    def test_find(self):
        self.page.find_element_in_dom_tree(self.element.subscription_button())

    def test_clickable(self):
        self.page.okko_page_element_is_clickable(self.element.subscription_button())

    def test_click(self):
        self.page.okko_page_click_to_element(self.element.subscription_button())

    def test_click_and_proceed(self):
        self.page.click_and_proceed(xpath=self.element.subscription_button(), expected_xpath=self.element.back_after_proceed_subscription_button())

    def test_click_at_find_and_wait_find_window(self):
        self.page.click_and_proceed(xpath=self.element.search_button(), expected_xpath=self.element.find_input_window())

    def test_finding_proces(self):
        self.page.click_and_proceed(xpath=self.element.search_button(), expected_xpath=self.element.find_input_window())
        self.page.fild(xpath=self.element.find_input_window(), value="Война")
        self.page.find_element_in_search(self.element.find_after_click_find_button())

    def test_using_category_movies(self):
        self.page.click_and_proceed(xpath=self.element.find_movies_element(), expected_xpath=self.element.expected_movies_element())







