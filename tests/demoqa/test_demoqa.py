import time
import pytest
import allure
from conftest import browser
from lib.demoqa.fixturies import DemoqaPage
from lib.demoqa.demoqa_page import DemoqaPage
from lib.demoqa.elements import Elements


class TestDemoqaPage:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self, demo_qa_page: DemoqaPage):
        self.page = demo_qa_page  # Устанавливаем значение в фикстуре
        self.element = Elements

    @allure.story('Тест открытия страницы')
    def test_open_main_page(self):
        with allure.step('Открытие страницы'):
            self.page.open_demoqa_form()