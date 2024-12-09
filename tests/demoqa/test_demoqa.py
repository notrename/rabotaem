import time
import pytest
import allure
from lib.demoqa.elements.elements import Elements
from lib.demoqa.page.demoqa_page import DemoqaPage
from lib.demoqa.fixturies import *


class TestDemoqaPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, demo_qa_page: DemoqaPage):
        self.page = demo_qa_page
        self.element = Elements

    def test_open_form_page(self):
        self.page.open_demoqa_form()
        self.page.find_element_in_dom_tree(self.element.header_form())