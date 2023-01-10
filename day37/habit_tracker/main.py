import requests
import os
from datetime import datetime

#https://pixe.la/@rp42dev

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# response.raise_for_status()

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "exercise",
#     "unit": "minutes",
#     "type": "float",
#     "color": "shibafu",
# }

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now()

# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "30",
# }

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# response.raise_for_status()

# update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

# new_pixel_data = {
#     "quantity": "60",
# }
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# response.raise_for_status()

delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
response.raise_for_status()

print(response.text)
