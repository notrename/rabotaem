from selenium.common import InvalidSessionIdException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import Logger


class Page:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.browser_timeout = 10
        self.logger = Logger().get_logger()

    def _wait_to_load(self, xpath: str, timeout: int):
        WebDriverWait(driver=self.__driver, timeout=timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, xpath),
            )
        )

    def open_site(self, url: str, error_message=None):
        self.logger.info(f'Попытка открыть сайт: {url}')
        try:
            self.__driver.get(url)
        except InvalidSessionIdException as e:
            message = f"Потеряно соединение с браузером. Возможно браузер был закрыт или аварийно завершил работу\n{e}"
            raise InvalidSessionIdException(message)
        except TimeoutException as e:
            message = (
                f"Не дождались полной загрузки страницы в течение {self.browser_timeout} секунд"
            )
            raise TimeoutException(f"{error_message}\n{e}" or message)
        self.logger.info(f'Сайт {url} открылся')

    def xpath_is_present(self, xpath: str, silent: bool = True):
        self.logger.info(f'Попытка найти элемент по xpath\'y: {xpath}')
        try:
            self.__driver.find_element(by=By.XPATH, value=xpath)
            self.logger.info(f'Элемент успешно найден')
            return True
        except NoSuchElementException as e:
            self.logger.warning('Элемент не найден')
            if silent:
                return None
            raise NoSuchElementException(f'Xpath: {xpath} не найден')