import allure
import pytest

from lib.gost_team.pages.gost_team_order_testing_page import GostTeamOrderTestingPage
from lib.gost_team.pages.gost_team_page import GostTeamPage


@allure.feature('Тесты GostTeam')
class TestGostTeam:

    @pytest.fixture(scope='function', autouse=True)
    def setup(
        self,
        gost_team_page: GostTeamPage,
    ):
        self.page = gost_team_page

    @allure.story('Проверка возможности заказать тестирование')
    def test_order_testing(self):
        self.page.open()
        order_page = self.page.go_to_ordering_testing_page()
        order_page.on_page()
        order_page.check_is_active_elements()
