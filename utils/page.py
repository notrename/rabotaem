from selenium.common import InvalidSessionIdException, TimeoutException, NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import Logger


class Page:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.browser_timeout = 2
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

    def element_is_visible(self, xpath: str, timeout: int = 2) -> bool:
        """
        Проверка, виден ли элемент на странице в течение заданного времени.
        """
        self.logger.info(f'Попытка проверить видимость элемента по xpath: {xpath}')
        try:
            WebDriverWait(self.__driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f'Элемент {xpath} видим на странице')
            return True
        except TimeoutException as e:
            self.logger.error(f'Элемент {xpath} не стал видимым за {timeout} секунд: {e}')
            return False
        except NoSuchElementException as e:
            self.logger.error(f'Элемент не найден по xpath {xpath}: {e}')
            return False

    def send_keys_to_input(self, xpath: str, text: str, timeout: int = 2) -> bool:
        """
        Отправка текста в поле ввода по xpath.
        """
        self.logger.info(f'Попытка отправить текст в поле ввода по xpath: {xpath}')
        try:
            input_field = WebDriverWait(self.__driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            input_field.clear()  # очищаем поле перед вводом
            input_field.send_keys(text)  # отправляем текст
            self.logger.info(f'Текст "{text}" успешно отправлен в поле {xpath}')
            return True
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'Не удалось отправить текст в поле {xpath}: {e}')
            return False
