from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lib.demoqa.elements.demoqa_chekbox_page_elements import DemoQaCheckBoxElements
from utils.page import Page


class DemoQaCheckBoxPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://demoqa.com/checkbox'
        self.__driver = driver
        self.elems = DemoQaCheckBoxElements(driver=driver)

    def open(self):
        self.open_site(
            url=self.url,
        )
        self.check_url_contains('checkbox')

    def is_button_state_changed(self):
        try:
            # Ожидание, пока иконка станет видимой
            WebDriverWait(self.elems.open_icon, 10).until(
                EC.visibility_of(self.elems.open_icon)
            )
            self.logger.info("Иконка стала видимой.")

            # Проверка, что элемент содержит класс 'rct-icon rct-icon-parent-open'
            if "rct-icon rct-icon-parent-open" in self.elems.open_icon.get_attribute("class"):
                self.logger.info("Иконка содержит нужный класс.")
                return True
            else:
                self.logger.info("Иконка не содержит нужный класс.")
                return False
        except Exception as e:
            self.logger.error(f"Ошибка при проверке состояния иконки: {e}")
            return False

    def is_visible_dropdown_elements(self):
        self.element_is_visible(self.elems.desktop_button)
        self.element_is_visible(self.elems.documents_button)
        self.element_is_visible(self.elems.downloads_button)
