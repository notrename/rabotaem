from selenium.common import InvalidSessionIdException, TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
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

    def _wait_to_load(self, xpath: str, timeout: int) -> bool:
        self.logger.info(f'Ожидание загрузки элемента по xpath: {xpath}')
        try:
            WebDriverWait(driver=self.__driver, timeout=timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f'Элемент {xpath} успешно загружен')
            return True
        except TimeoutException as e:
            self.logger.error(f'Элемент {xpath} не загрузился за {timeout} секунд: {e}')
            return False

    def open_site(self, url: str, error_message=None) -> bool:
        self.logger.info(f'Попытка открыть сайт: {url}')
        try:
            self.__driver.get(url)
            self.logger.info(f'Сайт {url} открылся')
            return True
        except InvalidSessionIdException as e:
            message = f"Потеряно соединение с браузером. Возможно браузер был закрыт или аварийно завершил работу\n{e}"
            self.logger.error(message)
            raise InvalidSessionIdException(message)
        except TimeoutException as e:
            message = f"Не дождались полной загрузки страницы в течение {self.browser_timeout} секунд"
            self.logger.error(f"{error_message}\n{e}" or message)
            return False

    def xpath_is_present(self, xpath: str, silent: bool = True) -> bool:
        self.logger.info(f'Попытка найти элемент по xpath: {xpath}')
        try:
            self.__driver.find_element(by=By.XPATH, value=xpath)
            self.logger.info(f'Элемент {xpath} успешно найден')
            return True
        except NoSuchElementException as e:
            self.logger.warning(f'Элемент {xpath} не найден')
            if silent:
                return False
            raise NoSuchElementException(f'Xpath: {xpath} не найден')

    def click_element(self, xpath: str, timeout: int = 2) -> bool:
        self.logger.info(f'Попытка кликнуть по элементу по xpath\'y: {xpath}')
        try:
            element = WebDriverWait(self.__driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            self.logger.info(f'Клик по элементу {xpath} выполнен успешно')
            return True
        except (TimeoutException, ElementClickInterceptedException) as e:
            self.logger.error(f'Не удалось кликнуть по элементу {xpath}: {e}')
            return False
        except NoSuchElementException as e:
            self.logger.error(f'Элемент не найден по xpath {xpath}: {e}')
            return False
        except StaleElementReferenceException as e:
            self.logger.error(f'Ссылка на элемент устарела при попытке кликнуть по {xpath}: {e}')
            return False

    def element_is_clickable(self, xpath: str, timeout: int = 2) -> bool:
        self.logger.info(f'Попытка кликнуть по элементу {xpath}')
        try:
            element = WebDriverWait(self.__driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            self.logger.info(f'Элемент {xpath} кликабельный')
            return True
        except (TimeoutException, ElementClickInterceptedException) as e:
            self.logger.error(f'Элемент {xpath} не кликабельный, {e}')
            return False
