import os
from lib.okko.fixturies import *
from selenium import webdriver
from lib.avito.fixtures import *


@pytest.fixture(scope='module')
def browser():
    driver_type = os.getenv('driver_type', 'chromedriver')  # По умолчанию Chrome
    driver = None

    if driver_type == 'chromedriver':
        driver = webdriver.Chrome()
    elif driver_type == 'geckodriver':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported driver type: {driver_type}")

    yield driver
    driver.quit()
