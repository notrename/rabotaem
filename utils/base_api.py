import requests

class Api:
    @staticmethod
    def get(url, params=None, headers=None):
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response  # Вернуть объект Response

    @staticmethod
    def post(url, data=None, headers=None):
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response  # Вернуть объект Response

    @staticmethod
    def put(url, data=None):
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response  # Вернуть объект Response

    @staticmethod
    def delete(url):
        response = requests.delete(url)
        response.raise_for_status()
        return response.status_code

    @staticmethod
    def patch(url, data=None):
        response = requests.patch(url, json=data)
        response.raise_for_status()
        return response  # Вернуть объект Response
