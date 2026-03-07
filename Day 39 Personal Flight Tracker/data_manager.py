import os

import requests
from dotenv import load_dotenv

load_dotenv()
SHEETLY_ENDPOINT = os.getenv('SHEETLY_API_ENDPOINT')
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._auth = os.getenv('AUTHENTICATION_BEARER_TOKEN')

        self.destination_data = {}
        self.bearer_headers = {
            "Authorization": f"Bearer {self._auth}"
        }

    def get_flight_data (self):
        try:
            response = requests.get(
                url=SHEETLY_ENDPOINT,
                headers=self.bearer_headers
            )
            response.raise_for_status()
            data = response.json()["prices"]
            self.destination_data = data

            return self.destination_data
        except Exception as e:
            print(f"Failed to fetch the flight data", e)
            return None


    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            try:
                response = requests.put(
                    url=f"{SHEETLY_ENDPOINT}/{city['id']}",
                    json=new_data,
                    headers=self.bearer_headers
                )
                response.raise_for_status()
            except Exception as e:
                print(e)