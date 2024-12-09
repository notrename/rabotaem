import pytest
from lib.demoqa.demoqa_page import DemoqaPage

@pytest.fixture
def demo_qa_page(browser) -> DemoqaPage:
    return DemoqaPage(driver=browser)
