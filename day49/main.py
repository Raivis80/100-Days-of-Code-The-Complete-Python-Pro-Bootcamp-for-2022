import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from selenium.common.exceptions import NoSuchElementException

import time

ACCOUNT_EMAIL = os.environ.get("EMAIL")
ACCOUNT_PASSWORD = os.environ.get("PASSWORD")
PHONE = os.environ.get("PHONE")

# Create a new instance of the Chrome driver
service = Service("D:\development\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3514925689&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CP%2CC%2CI&f_WT=2&geoId=104738515&keywords=web%20developer%20junior&location=Ireland&refresh=true")
sign_in_button = driver.find_element("link text", "Sign in")
sign_in_button.click()

time.sleep(2)

email = driver.find_element("id", "username")
email.send_keys(ACCOUNT_EMAIL)

password = driver.find_element("id", "password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)


time.sleep(2)

all_listings = driver.find_elements("class name", "job-card-container--clickable")

print(len(all_listings))

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element("class name", "jobs-apply-button")
        apply_button.click()
        time.sleep(2)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element("class name", "artdeco-text-input--input")
        if phone.get_attribute("value") == "":
            phone.send_keys(PHONE)

        button = driver.find_element("class name", "artdeco-button--primary")

        if button.get_attribute("aria-label") == "Submit application":
            button.click()
            print("Application submitted!")
        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        else:
            close_button = driver.find_element("class name", "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements("class name", "artdeco-modal__confirm-dialog-btn")[0]
            discard_button.click()
            print("Complex application, skipped.")
            continue

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element("class name", "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
