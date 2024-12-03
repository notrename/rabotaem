from lib.okko.fixturies import *
from selenium import webdriver


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Открываем браузер во весь экран
    yield driver
    driver.quit()


