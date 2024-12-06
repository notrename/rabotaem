import os
from lib.okko.fixturies import *
from lib.avito.fixtures import *
from lib.gost_team.fixtures import *
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    driver_type = os.getenv('driver_type', 'chromedriver')  # По умолчанию Chrome

    if driver_type == 'chromedriver':
        driver = webdriver.Chrome()
        driver.maximize_window()  # Открываем браузер во весь экран
    elif driver_type == 'geckodriver':
        driver = webdriver.Firefox()
    elif driver_type == 'docker':
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(f"Unsupported driver type: {driver_type}")

    yield driver
    driver.quit()
