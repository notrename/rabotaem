from selenium import webdriver
from lib.avito.fixtures import *


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


