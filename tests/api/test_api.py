import pytest
from utils.base_api import Api


class TestAPI:
    def setup(self):
        self.base_url = 'https://restful-booker.herokuapp.com'
        self.username = "admin"
        self.password = "password123"
        self.token = self.create_auth_token()
        self.booking_id = None  # Инициализируем переменную для ID бронирования

    def create_auth_token(self):
        auth_url = f"{self.base_url}/auth"
        auth_data = {
            "username": self.username,
            "password": self.password
        }
        response = Api.post(auth_url, auth_data)
        assert response.status_code == 200, "Failed to authenticate"
        return response.json()['token']

    def create_booking(self, booking_data):
        booking_url = f"{self.base_url}/booking"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = Api.post(booking_url, booking_data, headers=headers)
        assert response.status_code == 200, f"Failed to create booking: {response.text}"
        self.booking_id = response.json()['bookingid']  # Сохраняем ID созданного бронирования
        return response.json()

    def test_create_booking(self):
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
        response = self.create_booking(booking_data)
        assert response['booking']['firstname'] == booking_data['firstname']
        assert response['booking']['lastname'] == booking_data['lastname']

    def test_get_booking_ids(self):
        booking_ids_url = f"{self.base_url}/booking"
        response = Api.get(booking_ids_url)
        assert response.status_code == 200, "Failed to get booking IDs"
        assert isinstance(response.json(), list), "Response should be a list of bookings"