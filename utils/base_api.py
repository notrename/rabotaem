import requests


class API:

    def send_get(self, url: str, params: dict, success: bool = True) -> dict:
        # logaem
        response = requests.get(url=url, params=params)
        # attachim params, url
        if success:
            assert response.status_code in range(200, 204)
            return response.json()
        else:
            assert response.status_code in range(400, 404)
            return response.json()
