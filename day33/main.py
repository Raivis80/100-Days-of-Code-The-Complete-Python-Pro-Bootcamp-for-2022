import requests
from datetime import datetime as dt
MY_LAT = 53.286572
MY_LONG = -6.370580

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print("Sunrise in Dublin is at: " + sunrise.split("T")[1].split(":")[0] + ":" + sunrise.split("T")[1].split(":")[1])
print("Sunset in Dublin is at: " + sunset.split("T")[1].split(":")[0] + ":" + sunset.split("T")[1].split(":")[1])

time_now = dt.now()
print(time_now)
