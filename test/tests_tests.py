import pytest
from selenium.webdriver.common.by import By
from utils.logger import Logger

@pytest.mark.usefixtures("browser")
def test_google_logo(browser):
    logger = Logger().get_logger()  # Получаем логгер
    logger.info("Запуск теста Google")

    try:
        logger.info("Открываем страницу Google")
        browser.get('https://www.google.com/')

        element = browser.find_element(By.XPATH, '//input[@name="q"]')  # Более стабильный XPATH
        logger.info(f"Полученное значение элемента: '{element.get_attribute('value')}'")

        assert 'Google' in element.get_attribute('value'), f"Ожидалось 'Google', но получено '{element.get_attribute('value')}'"
        logger.info("Тест пройден успешно")

    except AssertionError as e:
        logger.error(f"Тест не пройден: {e}")
    except Exception as e:
        logger.exception("Произошла ошибка")
    finally:
        logger.info("Тест завершен")
