import allure
import pytest
from lib.demoqa.pages.demoqa_page import DemoQaPage
from lib.demoqa.fixtures import demoqa_page


@allure.feature('Тестирование UI DemoQa')
class TestDemoQaPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, demoqa_page: DemoQaPage):
        self.page = demoqa_page  # Устанавливаем значение в фикстуре

    @allure.story('Открытие страницы')
    def test_open_main_page(self):
        self.page.open()
        self.page.attach_screenshot()

    def test_go_to_checkbox_page(self):
        self.page.go_to_checkbox_page()

    def test_go_to_uploaddownload_page(self):
        self.page.go_to_uploaddownload_page()

    def test_go_to_webtables_page(self):
        self.page.go_to_webtables_page()
