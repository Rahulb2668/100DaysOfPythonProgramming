import os
import time
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
load_dotenv()

ORIGIN_CITY="DXB"

data_manager = DataManager()
flight_sheet_data = data_manager.get_flight_data()
flight_search = FlightSearch()

for data in flight_sheet_data:
    if data['iataCode'] == "" :
        data['iataCode'] = flight_search.flight_search_code(data['city'])
        time.sleep(2)

data_manager.destination_data = flight_sheet_data
data_manager.update_destination_data()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in flight_sheet_data:
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY,
        destination_city_code=destination["iataCode"],
        depart_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")