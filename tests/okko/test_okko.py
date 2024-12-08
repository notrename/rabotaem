import pytest
import allure
from conftest import browser
from lib.okko.fixturies import okko_web_page
from lib.okko.okko_page import OkkoPage
from lib.okko.elements import Elements


class TestOkkoPage:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self, okko_web_page: OkkoPage):
        self.page = okko_web_page  # Устанавливаем значение в фикстуре
        self.element = Elements

    @allure.story('Тест открытия страницы')
    def test_open_main_page(self):
        with allure.step('Открытие страницы'):
            self.page.open_okko()
        with allure.step('Ожидаем загрузку хедера'):
            self.page.xpath_is_present(self.element.header())
        with allure.step('Завершение теста'):
            print('Все блоки кода отработали успешно, тест успешно завершён')

    @allure.story('Тест возможности кликабельности кнопки')
    def test_clickable_new(self):
        with allure.step('Открытие страницы'):
            self.page.open_okko()
        with allure.step('Ожидаем загрузку хедера'): #Это мне показалось логичным решением, тк сама кнопка находится в хэдере и если он не прогрузится нет смысла искать элемент
            self.page.xpath_is_present(self.element.header())
        with allure.step(f'Ожидаем загрузку кнопки {self.element.subscription_button()}'):
            self.page.xpath_is_present(self.element.subscription_button())
        with allure.step('Тест кликабельности кнопки "Месяц за 1₽"'):
            self.page.element_is_clickable_xpath(self.element.subscription_button()), f'Элемент {self.element.subscription_button()} доступен для клика'
        with allure.step('Завершение теста'):
            print('Все блоки кода отработали успешно, тест успешно завершён')

    @allure.story('Тест поиск элемента')
    def test_find_element(self):
        with allure.step('Открытие страницы'):
                self.page.open_okko()
        with allure.step('Ожидаем загрузку хедера'): #Это мне показалось логичным решением, тк сама кнопка находится в хэдере и если он не прогрузится нет смысла искать элемент
            self.page.xpath_is_present(self.element.header())
        with allure.step(f'Ожидаем загрузку кнопки поиска по сайту {self.element.search_button()}'):
            self.page.xpath_is_present(self.element.search_button())
        with allure.step('Скриним элемент'):
            self.page.attach_screenshot_element(self.element.search_button())
        with allure.step('Завершение теста'):
            print('Все блоки кода отработали успешно, тест успешно завершён')
