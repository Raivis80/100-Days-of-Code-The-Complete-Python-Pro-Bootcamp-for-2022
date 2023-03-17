#Daft Property Scraper - Day 53 of #100DaysOfCode
# Scrapes Daft.ie for properties in a given price range and number of bedrooms
# and saves them to a google form using Selenium and BeautifulSoup
# convert to a google forms to a spreadsheet using

import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CHROME_DRIVER_PATH = "D:\development\chromedriver.exe"

# Google Sheet URL

google_sheet_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdLC8QopKt6qd1EB8UM4txBajd2qpNvwAboMkMJg7y-gJbxTA/viewform?usp=sf_link'

PREFIX = 'https://www.daft.ie'

URL = 'https://www.daft.ie/property-for-rent/dublin/houses?rentalPrice_to=2300&rentalPrice_from=500&numBeds_from=1'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


class ScrapeDaft:
    def __init__(self):
        self.response = requests.get(url=URL, headers=headers)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.all_properties = self.soup.find_all(name="li", class_="SearchPage__Result-gg133s-2")
        self.property_links = []
        self.property_prices = []
        self.property_addresses = []

    def get_property_links(self):
        for property in self.all_properties:
            link = property.find(name="a", )["href"]
            self.property_links.append(PREFIX + link)
        return self.property_links

    def get_property_prices(self):
        for property in self.all_properties:
            price = property.find(name="div", class_="TitleBlock__Price-sc-1avkvav-4").h3.getText()
            self.property_prices.append(price)
        return self.property_prices

    def get_property_addresses(self):
        for property in self.all_properties:
            address = property.find(name="h2", class_="TitleBlock__Address-sc-1avkvav-8").getText()
            self.property_addresses.append(address)
        return self.property_addresses


print("Scraping Daft.ie...")
daft = ScrapeDaft()
property_links = daft.get_property_links()
property_prices = daft.get_property_prices()
property_addresses = daft.get_property_addresses()


class GoogleSheet:
    def __init__(self, google_sheet_url):
        self.google_sheet_url = google_sheet_url
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(options=chrome_options, service=self.service)
        self.driver.get(self.google_sheet_url)
        self.driver.maximize_window()

    def fill_form(self, property_links, property_prices, property_addresses):
        for i in range(len(property_links)):
            inputs = self.driver.find_elements(By.XPATH, '//input[@type="text"]')
            inputs[0].send_keys(property_addresses[i])
            inputs[1].send_keys(property_prices[i])
            inputs[2].send_keys(property_links[i])

            self.driver.find_element(By.XPATH, '//div[@role="button"]').click()
            time.sleep(2)

            try:
                self.driver.find_element(By.XPATH, '//a[text()="Submit another response"]').click()
            except NoSuchElementException:
                pass
            time.sleep(2)


print("Filling out Google Sheet...")
google_sheet = GoogleSheet(google_sheet_url)
time.sleep(5)
google_sheet.fill_form(property_links, property_prices, property_addresses)


