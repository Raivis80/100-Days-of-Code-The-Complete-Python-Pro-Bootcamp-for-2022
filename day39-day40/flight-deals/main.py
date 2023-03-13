from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_data import UserData
from user_manager import UserManager
# USER = UserManager.get_user_by_email("rp42dev@gmail.com")

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "MIA"

# if sheet_data[0]["iataCode"] == "":
#     city_names = [row["city"] for row in sheet_data]
#     codes = flight_search.get_destination_codes(city_names)
#     data_manager.update_destination_codes()
#     sheet_data = data_manager.get_destination_data()
#
# destinations = {
#     data["iataCode"]: {
#         "id": data["id"],
#         "city": data["city"],
#         "price": data["lowestPrice"]
#     }for data in sheet_data}
#
# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# for destination_code in destinations:
#     flight = flight_search.check_flights(
#         ORIGIN_CITY_IATA,
#         destination_code,
#         from_time=tomorrow,
#         to_time=six_month_from_today
#     )
#     if flight is None:
#         continue
#
#     if flight.price < destinations[destination_code]["price"]:
#
#         users = UserManager().get_users()
#         emails = [row["email"] for row in users]
#         names = [row["firstName"] for row in users]
#
#         message = f"Low price alert! Only {flight.price}GBP to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
#         if flight.stop_overs > 0:
#             message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."
#
#         link = flight.deap_link
#
#         NotificationManager().send_emails(emails, message, link)

flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        "NYC",
        from_time="2023-02-09",
        to_time="2023-02-09"
    )
print(flight)

if flight is None:
    print("No flights found.")

message = f"Low price alert! Only {flight.price}GBP to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
if flight.stop_overs > 0:
    message += f"\n\nFlight has {flight.stop_overs}, via {flight.via_city}."

link = flight.deap_link

NotificationManager().send_emails(["edgarstattoo@gmail.com", "rp42dev@gmail.com"], message, link)

# user_manager = UserManager()
# user_manager.create_user()

# current_user = user_manager.get_user_by_email("rp42dev@gmail.com")






