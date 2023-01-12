import requests
import os
SHEETY_ENDPOINT = f"{os.environ.get('SHEETY_ENDPOINT')}/prices"


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.destination_data = {}
        self.headers = {
            "Authorization": f"Bearer {os.environ.get('SHEETY_API_KEY')}"
        }

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)