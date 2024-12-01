import pytest
from conftest import browser
# + импортировать сами классы

@pytest.fixture
def okko_web_page(browser: webdriver) -> OkkoPage:
    return OkkoPage(driver=browser)