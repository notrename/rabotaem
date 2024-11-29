import pytest
from conftest import browser
# + импортировать сами классы

@pytest.fixture
def okko_web_page(browser: webdriver) -> OkkoPage:
    return OkkoPage(driver=browser)

@pytest.fixture
def avito_web_page(browser: webdriver) -> AvitoPage:
    return AvitoPage(driver=browser)