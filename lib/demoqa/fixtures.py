import pytest
from lib.demoqa.pages.demoqa_page import DemoQaPage
from lib.demoqa.pages.demoqa_chekbox_page import DemoQaCheckBoxPage


@pytest.fixture
def demoqa_page(browser) -> DemoQaPage:
    return DemoQaPage(driver=browser)

@pytest.fixture
def demoqa_page_checkbox(browser) -> DemoQaCheckBoxPage:
    return DemoQaCheckBoxPage(driver=browser)