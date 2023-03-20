import json
import requests
from requests.models import Response


class VkApiRequests:
    """Class for making requests to VK_API"""
    def __init__(self, token: str, base_url: str, api_version: str):
        self.__validate_args(token, base_url)
        self.token = token
        self.base_url = base_url
        self.api_version = api_version

    # Checking if all arguments for a request are strings
    def __validate_args(self, *args):
        for i in args:
            if type(i) != str:
                raise TypeError("VkApiRequests class object can only be initialized with arguments of type 'str'")
            if not i:
                raise ValueError("Values cannot be empty")

    # HTTP request send function
    def __get_request(self, api_method: str, fields: list[str]) -> Response:
        url = self.base_url + api_method + f"&access_token={self.token}&{self.api_version}"
        for i in fields:
            url += f"&{i}"
        try:
            return requests.get(url)
        except ConnectionError:
            print("Connection error")

    # A function that makes a request to get a list of friends and information about them
    def get_friends_info(self, user_id: int, count: int = 5000, offset: int = 0) -> json:
        api_method = "friends.get?"
        fields = [f"user_id={str(user_id)}", "fields=country,city,bdate,sex", f"count={count}", f"offset={offset}"]
        response = self.__get_request(
            api_method=api_method,
            fields=fields)
        return response.json()
        # сделать обработчик ошибок платформы вк
