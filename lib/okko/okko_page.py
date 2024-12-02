from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page  # Импортируем базовый класс Page

class OkkoPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_okko(self):
        """Открывает сайт Okko."""
        url = "https://okko.tv/?clientSessionId=19386d65-b2f9-7aaa-38f0-2f0bedf22974&sso=false"
        self.open_site(url)

    def search_for_movie(self, movie_name: str):
        """Ищет фильм по названию."""
        self.logger.info(f'Поиск фильма: {movie_name}')
        search_box_xpath = "//input[@placeholder='Поиск']"  # XPath для поля поиска
        self._wait_to_load(search_box_xpath, self.browser_timeout)
        self.click_element(By.XPATH, search_box_xpath)
        self.__driver.find_element(By.XPATH, search_box_xpath).send_keys(movie_name)
        self.logger.info(f'Фильм {movie_name} был введен в поле поиска')

    def click_first_result(self):
        """Кликает по первому результату поиска."""
        first_result_xpath = "(//div[@class='result-item'])[1]"  # XPath для первого результата
        self.logger.info('Попытка кликнуть по первому результату поиска')
        self.click_element(By.XPATH, first_result_xpath)

    def is_movie_available(self, movie_name: str):
        """Проверяет, доступен ли фильм на странице."""
        movie_xpath = f"//h3[contains(text(), '{movie_name}')]"
        is_present = self.xpath_is_present(movie_xpath)
        if is_present:
            self.logger.info(f'Фильм {movie_name} доступен на странице')
        else:
            self.logger.warning(f'Фильм {movie_name} не найден на странице')
        return is_present