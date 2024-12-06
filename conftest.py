import os
from lib.okko.fixturies import *
from selenium import webdriver
from lib.avito.fixtures import *


@pytest.fixture(scope='function')
def browser():
    driver_type = os.getenv('driver_type', 'chromedriver')  # По умолчанию Chrome

    if driver_type == 'chromedriver':
        driver = webdriver.Chrome()
    elif driver_type == 'geckodriver':
        driver = webdriver.Firefox()
    elif driver_type == 'docker':
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Remote(
            command_executor='http://selenoid:4444/wd/hub',
            options=chrome_options,
        )
    else:
        raise ValueError(f"Unsupported driver type: {driver_type}")
    driver.maximize_window()  # Открываем браузер во весь экран

    yield driver
    driver.quit()
