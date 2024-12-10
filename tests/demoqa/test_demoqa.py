import allure
import pytest
from lib.demoqa.pages.demoqa_page import DemoQaPage


@allure.feature('Тестирование UI DemoQa')
class TestDemoQaPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, demoqa_page: DemoQaPage):
        self.page = demoqa_page  # Устанавливаем значение в фикстуре

    @allure.story('Открытие страницы')
    def test_open_main_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot_element(self.page.elems.header_xpath())


    def test_go_to_checkbox_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Переход к чекбоксу'):
            self.page.go_to_checkbox_page()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()


    def test_go_to_uploaddownload_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Переход к чекбоксу'):
            self.page.go_to_uploaddownload_page()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()

    def test_go_to_webtables_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Переход к чекбоксу'):
            self.page.go_to_webtables_page()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()
