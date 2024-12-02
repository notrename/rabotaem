from selenium import webdriver
from lib.okko.fixturies import *

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


