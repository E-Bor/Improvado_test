from config import token, base_url, test_user_id, api_version
from services.api_requests.vk_api import VkApiRequests
from services.data_processing.create_data import DataHandler
from pprint import pprint


handler = DataHandler()

test = VkApiRequests(token, base_url, api_version)
data = test.get_friends_info(test_user_id)





