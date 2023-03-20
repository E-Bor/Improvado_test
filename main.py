from config import token, base_url, user_id, api_version, output_file_path, output_format_data, offset, \
    pagination_end
from services.api_requests.vk_api import VkApiRequests
from services.data_processing.create_data import DataHandler
from services.data_recording.writer import DataWriter

from pprint import pprint

handler = DataHandler()
writer = DataWriter()
request = VkApiRequests(token, base_url, api_version)


if __name__ == "__main__":

    data = request.get_friends_info(user_id, pagination_end, offset)
    prepared_data = handler.get_prepared_friends_list(data)
    writer.save_file(prepared_data, output_file_path, output_format_data)
    pprint(prepared_data)



