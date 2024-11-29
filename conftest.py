import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def gost_team_page(browser: webdriver) -> OkkoPage:
    return OkkoPage(driver=browser)

@pytest.fixture
def gost_team_page_with_blog(browser: webdriver) -> AvitoPage:
    return AvitoPage(driver=browser)