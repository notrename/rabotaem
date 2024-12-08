import pytest
import allure
import time
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
        with allure.step('Страница открыта'):
            print('Страница успешно открыта')

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
    #
    # def test_clickable(self):
    #     self.page.okko_page_element_is_clickable(self.element.subscription_button())
    #
    # def test_click(self):
    #     self.page.okko_page_click_to_element(self.element.subscription_button())
    #
    # def test_click_and_proceed(self):
    #     self.page.click_and_proceed(xpath=self.element.subscription_button(), expected_xpath=self.element.back_after_proceed_subscription_button())
    #
    # def test_click_at_find_and_wait_find_window(self):
    #     self.page.click_and_proceed(xpath=self.element.search_button(), expected_xpath=self.element.find_input_window())
    #
    # def test_finding_proces(self):
    #     self.page.click_and_proceed(xpath=self.element.search_button(), expected_xpath=self.element.find_input_window())
    #     self.page.fild(xpath=self.element.find_input_window(), value="Война")
    #     self.page.find_element_in_search(self.element.find_after_click_find_button())
    #
    # def test_using_category_movies(self):
    #     self.page.click_and_proceed(xpath=self.element.find_movies_element(), expected_xpath=self.element.expected_movies_element())

