import pytest
from lib.demoqa.pages.demoqa_page import DemoQa


@pytest.fixture
def demoqa_page(browser) -> DemoQa:
    return DemoQa(driver=browser)
