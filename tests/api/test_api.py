import pytest
import allure
from utils.base_api import Api


class TestAPI:
    def setup(self):
        """Установка базовых параметров перед каждым тестом."""
        self.base_url = 'https://restful-booker.herokuapp.com'
        self.username = "admin"
        self.password = "password123"
        self.token = self.create_auth_token()
        self.booking_id = None  # Инициализируем переменную для ID бронирования

    @allure.step('Создание токена аутентификации')
    def create_auth_token(self):
        """Создание токена аутентификации."""
        auth_url = f"{self.base_url}/auth"
        auth_data = {
            "username": self.username,
            "password": self.password
        }
        response = Api.post(auth_url, auth_data)
        assert response.status_code == 200, "Не удалось аутентифицироваться"
        return response.json()['token']

    @allure.step('Создание нового бронирования')
    def create_booking(self, booking_data):
        """Создание нового бронирования."""
        booking_url = f"{self.base_url}/booking"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = Api.post(booking_url, booking_data, headers=headers)
        assert response.status_code == 200, f"Не удалось создать бронирование: {response.text}"
        self.booking_id = response.json()['bookingid']  # Сохраняем ID созданного бронирования
        return response.json()

    @allure.title('Тест: Создание бронирования')
    @allure.step('Проверка успешного создания бронирования')
    def test_create_booking(self):
        """Проверка успешного создания бронирования."""
        booking_data = {
            "firstname": "Test",
            "lastname": "User",
            "totalprice": 123,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-07"
            },
            "additionalneeds": "Breakfast"
        }

        with allure.step('Создание бронирования'):
            response = self.create_booking(booking_data)

        with allure.step('Проверка данных бронирования'):
            assert response['booking']['firstname'] == booking_data['firstname'], "Имя не совпадает"
            assert response['booking']['lastname'] == booking_data['lastname'], "Фамилия не совпадает"

    @allure.title('Тест: Получение списка ID бронирований')
    @allure.step('Проверка возможности получения списка ID бронирований')
    def test_get_booking_ids(self):
        """Проверка возможности получения списка всех бронирований."""
        booking_ids_url = f"{self.base_url}/booking"

        with allure.step('Получение списка бронирований'):
            response = Api.get(booking_ids_url)

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200, "Не удалось получить ID бронирований"

        with allure.step('Проверка формата ответа'):
            assert isinstance(response.json(), list), "Ответ должен быть списком бронирований"
