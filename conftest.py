import pytest
from selenium import webdriver
from lib.okko.okko_page import OkkoPage

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
### del
@pytest.fixture
def okko_web_page(browser) -> OkkoPage:
    return OkkoPage(driver=browser)