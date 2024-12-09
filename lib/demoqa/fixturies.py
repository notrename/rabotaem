import pytest
from lib.demoqa.page.demoqa_page import DemoqaPage

@pytest.fixture
def demo_qa_page(browser) -> DemoqaPage:
    return DemoqaPage(driver=browser)




import pytest
from lib.okko.okko_page import OkkoPage

@pytest.fixture
def okko_web_page(browser) -> OkkoPage:
    return OkkoPage(driver=browser)
