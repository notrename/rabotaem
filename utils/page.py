from selenium.common import InvalidSessionIdException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.logger import Logger

class Page:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.logger = Logger().get_logger()

    def _wait_to_load(self, xpath: str) -> None:
        self.logger.info(f'Ожидание загрузки элемента по xpath: {xpath}')
        try:
            WebDriverWait(driver=self.__driver, timeout=10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f'Элемент {xpath} успешно загружен')
        except Exception as e:
            self.logger.error(f'Элемент {xpath} не загрузился: {e}')
            raise Exception(f'Элемент {xpath} не загрузился: {e}')

    def open_site(self, url: str, error_message=None) -> None:
        self.logger.info(f'Попытка открыть сайт: {url}')
        try:
            self.__driver.get(url)
            self.logger.info(f'Сайт {url} открылся')
        except InvalidSessionIdException as e:
            message = f"Потеряно соединение с браузером. Возможно браузер был закрыт или аварийно завершил работу\n{e}"
            self.logger.error(message)
            raise InvalidSessionIdException(message)
        except Exception as e:
            message = f"Не удалось открыть сайт {url}"
            self.logger.error(f"{error_message}\n{e}" or message)
            raise Exception(message)

    def xpath_is_present(self, xpath: str, silent: bool = True) -> None:
        self.logger.info(f'Попытка найти элемент по xpath: {xpath}')
        try:
            self.__driver.find_element(by=By.XPATH, value=xpath)
            self.logger.info(f'Элемент {xpath} успешно найден')
        except NoSuchElementException as e:
            self.logger.warning(f'Элемент {xpath} не найден')
            if not silent:
                raise NoSuchElementException(f'Xpath: {xpath} не найден')

    def click_element(self, xpath: str) -> None:
        self.logger.info(f'Попытка кликнуть по элементу по xpath: {xpath}')
        self._wait_to_load(xpath)  # Ожидаем загрузку элемента
        try:
            element = self.__driver.find_element(by=By.XPATH, value=xpath)
            element.click()
            if element.click() is not False:
                self.logger.info(f'Клик по элементу {xpath} выполнен успешно')
        except (ElementClickInterceptedException, StaleElementReferenceException) as e:
            self.logger.error(f'Не удалось кликнуть по элементу {xpath}: {e}')
            raise Exception(f'Не удалось кликнуть по элементу {xpath}: {e}')
        except NoSuchElementException as e:
            self.logger.error(f'Элемент не найден по xpath {xpath}: {e}')
            raise Exception(f'Элемент не найден по xpath {xpath}: {e}')

    def element_is_clickable(self, xpath: str) -> None:
        self.logger.info(f'Проверка доступности клика по элементу по xpath: {xpath}')
        self._wait_to_load(xpath)  # Ожидаем загрузку элемента
        try:
            self.__driver.find_element(by=By.XPATH, value=xpath)
            is_clickable = EC.element_to_be_clickable((By.XPATH, xpath))(self.__driver)
            if is_clickable:
                self.logger.info(f'Элемент {xpath} доступен для клика')
            else:
                raise Exception(f'Элемент {xpath} не доступен для клика')
        except (NoSuchElementException, StaleElementReferenceException) as e:
            self.logger.error(f'Ошибка при проверке кликабельности элемента {xpath}: {e}')
            raise Exception(f'Ошибка при проверке кликабельности элемента {xpath}: {e}')

    def refresh(self):
        self.__driver.refresh()