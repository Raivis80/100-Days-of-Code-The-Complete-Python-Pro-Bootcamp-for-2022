# Using Selenium and Python Navigate to the Tinder website
# Login with your Facebook account
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from selenium.common.exceptions import NoSuchElementException

from time import sleep

# Create a new instance of the Chrome driver
service = Service("D:\development\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get("https://tinder.com/")

sleep(2)
sign_in_button = driver.find_element(by=By.XPATH, value='//*[@id="q-586956664"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
sign_in_button.click()

sleep(2)
facebook_login = driver.find_element(by=By.XPATH, value='//*[@id="q1979629556"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login.click()
base_window = driver.window_handles[0]

sleep(3)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
# Switch to the login popup
allow_essential_cookies = driver.find_elements(by=By.CLASS_NAME, value='selected')
for element in allow_essential_cookies:
    print(element.text)
    if element.text == "Only allow essential cookies":
        element.click()
        break

email = driver.find_element(by=By.ID, value='email')
email.send_keys(os.environ.get("EMAIL"))

password = driver.find_element(by=By.ID, value='pass')
password.send_keys(os.environ.get("PASSWORD"))

login = driver.find_elements(By.TAG_NAME, "input")
for element in login:
    print(element.get_attribute("value"))
    if element.get_attribute("value") == "Log in":
        element.click()
        break

