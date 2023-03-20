import requests
from config import token, output_file_path, output_format_data, api_version, base_url




user_id = "&user_id=395025347"
count = "&count=10"
fields = "&fields=country,city,bdate,sex"
offset = "&offset=2"


url = base_url + user_id + count + offset + fields + version_and_token
r = api_requests.get(url)
response = r.json().get("response").get("items")



