import pytest
import allure
from utils.base_api import Api


class TestBookStoreAPI:
    base_url = "https://demoqa.com/swagger/#/"

    @allure.title('Тест: Проверка GET API')
    @allure.step("Отправляем GET")
    def test_ping_api_with_no_parameters(self):
        """Тест для проверки работоспособности API."""
        url = f"{self.base_url}/BookStore/v1/Books"

        # Выполнение GET запроса к эндпоинту
        response = Api.get(url)

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200, f"Ожидался статус 201, но получен {response.status_code}"

        with allure.step('Проверка сервера (в хэдэре ответа)'):
            dict_header = dict(response.headers)
        header_text = '\n'.join(f'{key}: {value}' for key, value in dict_header.items())
        allure.attach('Хэдер ответа', header_text, allure.attachment_type.TEXT)
        assert dict_header['Server'] == str(
            'nginx/1.17.10 (Ubuntu)'), f"Ожидался статус 200, но получен {response.status_code}"

        assert dict_header['Server'] == str('nginx/1.17.10 (Ubuntu)'), f"Ожидался статус 200, но получен {response.status_code}"
