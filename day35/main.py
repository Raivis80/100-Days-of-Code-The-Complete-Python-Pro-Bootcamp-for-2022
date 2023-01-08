import requests
import smtplib
import os

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
MY_LAT = 53.286572
MY_LONG = -6.370580

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": WEATHER_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()
hourly = data["hourly"][:12]

will_rain = False

for hour in hourly:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella it will rain")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="rp42dev@gmail.com", password=EMAIL_PASSWORD)
        connection.sendmail(from_addr="your_email", to_addrs="rapet80@gmail.com",
                            msg="Subject:It's going to rain today \n\n Bring an umbrella")
