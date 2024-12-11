import requests
from utils import logger
import allure
from typing import Optional, Dict, Any

from utils.logger import Logger

# Настройка логирования
log = Logger().get_logger()

class Api:
    @staticmethod
    def get(url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        log.info(f"Отправка GET запроса к URL: {url} с параметрами: {params} и заголовком: {headers}")
        with allure.step(f"GET запрос к {url} с параметрами: {params} и заголовком: {headers}"):
            response = requests.get(url, params=params, headers=headers)
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            response.raise_for_status()
            return response.json()  # Возвращаем словарь

    @staticmethod
    def post(url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        log.info(f"Отправка POST запроса к URL: {url} с данными: {data} и заголовком: {headers}")
        with allure.step(f"POST запрос к {url} с данными: {data} и заголовком: {headers}"):
            response = requests.post(url, json=data, headers=headers)
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            response.raise_for_status()
            return response.json()  # Возвращаем словарь

    @staticmethod
    def put(url: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        log.info(f"Попытка отправить PUT запрос к URL: {url} с данными: {data}")
        with allure.step(f"PUT запрос к {url} с данными: {data}"):
            response = requests.put(url, json=data)
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            response.raise_for_status()
            return response.json()  # Возвращаем словарь

    @staticmethod
    def delete(url: str) -> int:
        log.info(f"Попытка отправить DELETE запрос к URL: {url}")
        with allure.step(f"DELETE запрос к {url}"):
            response = requests.delete(url)
            log.info(f"Получен ответ: {response.status_code}")  # Логируем ответ
            response.raise_for_status()
            return response.status_code  # Возвращаем статус код

    @staticmethod
    def patch(url: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        log.info(f"Попытка отправить PATCH запрос к URL: {url} с данными: {data}")
        with allure.step(f"PATCH запрос к {url} с данными: {data}"):
            response = requests.patch(url, json=data)
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            response.raise_for_status()
            return response.json()  # Возвращаем словарь
