## Amazon Price Tracker

import requests
from bs4 import BeautifulSoup
import smtplib
import os

AMAZON_URL = "https://www.amazon.com/Acer-AN515-57-79TD-i7-11800H-GeForce-Keyboard/dp/B09R65RN43/?_encoding=UTF8&pd_rd_w=tVrQA&content-id=amzn1.sym.10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_p=10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_r=74N0M0JT6MABKQXE5DWK&pd_rd_wg=MbMrH&pd_rd_r=b4ca8d19-38a2-4351-b1ab-a18b12fd6860&ref_=pd_gw_exports_top_sellers_unrec&th=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}

response = requests.get(url=AMAZON_URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
price_as_float = float(price.replace(".", ""))

print(price_as_float)

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

if price_as_float < 600:
    message = f"Subject:Price Alert!\n\n{AMAZON_URL} is now ${price_as_float}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)