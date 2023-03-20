import json
import requests
from requests.models import Response

class VkApiRequests:
    def __init__(self, token: str, base_url: str, api_version: str):
        self.__validate_args(token, base_url)
        self.token = token
        self.base_url = base_url
        self.api_version = api_version



    def __validate_args(self, *args):
        for i in args:
            if type(i) != str:
                raise TypeError("VkApiRequests class object can only be initialized with arguments of type 'str'")
            if not i:
                raise ValueError("Values cannot be empty")


    def __get_request(self, api_method: str, fields: list[str]) -> Response:
        url = self.base_url + api_method + f"&access_token={self.token}&{self.api_version}"
        for i in fields:
            url += f"&{i}"
        try:
            return requests.get(url)
        except ConnectionError:
            print("Connection error")

    def get_friends_info(self, user_id: int, count: int = 1000, offset: int = 0) -> json:
        api_method = "friends.get?"
        fields = [str(user_id), "fields=country,city,bdate,sex", f"count={count}", f"offset={offset}"]
        response = self.__get_request(
            api_method=api_method,
            fields=fields)
        return response.json()
        # сделать обработчик ошибок платформы вк
