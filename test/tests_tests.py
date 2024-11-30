import pytest
from selenium.webdriver.common.by import By
from utils.logger import Logger

# Конфигурируем логер
logger = Logger().get_logger()  # Получаем логер
i = logger.info # Упрощаем код

@pytest.mark.usefixtures("browser")
def test_google_logo(browser):
    test_name = 'Google check'
    i("Запуск теста")
    i("Открытие страницы Google")
    browser.get('https://www.google.com/')
    element = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')  # Более стабильный XPATH
    i(f"Полученное значение элемента: '{element.get_attribute('value')}'")
    assert 'Поиск в Google' == element.get_attribute('value'), f"Ожидалось 'Поиск в Google', но получено '{element.get_attribute('value')}'"
    i(f"Тест {test_name} завершен")