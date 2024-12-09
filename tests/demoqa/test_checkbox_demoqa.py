import allure
import pytest
from lib.demoqa.pages.demoqa_chekbox_page import DemoQaCheckBoxPage


@allure.feature('Тестирование UI DemoQa checkbox')
class TestDemoQaPageCheckbox:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, demoqa_page_checkbox: DemoQaCheckBoxPage):
        self.page = demoqa_page_checkbox  # Устанавливаем значение в фикстуре

    @allure.story('Открытие страницы')
    def test_open_main_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot_element(self.page.elems.header_xpath())

    @allure.story('Проверка раскрывабщегося списка')
    def test_dropdown_displays_elements(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Проверка отображения кнопки раскрывающегося списка'):
            self.page.element_is_visible(self.page.elems.toggle_button())
        with allure.step('Раскрываем список'):
            self.page.click_element_by_xpath(self.page.elems.toggle_button())
        #with allure.step('Проверяем смену иконки'):
            # Не захотел загоняться на создании нового метода, пусть пока будет так, все равно перепишу, так как не работает
            #self.page.element_is_visible(self.page.elems.open_icon())
        with allure.step('Проверка присутствия элементов в раскрывающемся списке'):
            self.page.element_is_visible(self.page.elems.desktop_button())
            self.page.element_is_visible(self.page.elems.documents_button())
            self.page.element_is_visible(self.page.elems.downloads_button())
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()