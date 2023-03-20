
# Token received from according to instructions (Required)
token = ""
# id of the user from whom friends will be taken (Required)
user_id = ""
# Output format and path with the extension ".extension" (optional, the path has priority)
output_format_data = ""
output_file_path = ""
# Pagination adjustment pagination_end - number of friends, offset - offset relative to the beginning of the list.
# (optional, integer values)
pagination_end = None
offset = None

# Parameters necessary for the system to work (don't change)
api_version = "v=5.131"
base_url = "https://api.vk.com/method/"
api_method = "friends.get?"
