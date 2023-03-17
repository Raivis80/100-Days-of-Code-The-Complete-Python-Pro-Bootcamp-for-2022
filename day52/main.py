import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CHROME_DRIVER_PATH = "D:\development\chromedriver.exe"
SIMILAR_ACCOUNT = "https://www.instagram.com/coding_dev_/"

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

class InstaFollower:
    def __init__(self):
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(options=chrome_options, service=self.service)
        self.driver.get('https://www.instagram.com/accounts/login/')
        self.driver.maximize_window()

    def dismiss_popup(self):

        try:
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if button.text == "Only allow essential cookies":
                  button.click()
                  break
        except NoSuchElementException:
            pass

    def login(self):

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(4)
        try:
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if button.text == "Not now":
                    button.click()
                    break
        except NoSuchElementException:
            pass

        time.sleep(4)
        try:
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if button.text == "Not Now":
                    button.click()
                    break
        except NoSuchElementException:
            pass

    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)

        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, '//header/section/ul/li[2]/a')
        followers.click()

        time.sleep(4)
        modal = self.driver.find_element(By.XPATH, '//div[@role="dialog"]/div/div/div[2]')

        print(modal.get_attribute("class"))
        #
        # for i in range(10):
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     print(i)
        #     time.sleep(2)

    def follow(self):
        time.sleep(4)
        follow_buttons = self.driver.find_elements(By.TAG_NAME, "button")

        for button in follow_buttons:
            print(button.text, button.get_attribute("class"))
            if button.text == "Follow":
                self.driver.execute_script("arguments[0].click();", button)
                time.sleep(2)



bot = InstaFollower()

time.sleep(4)
bot.dismiss_popup()

time.sleep(4)
bot.login()

time.sleep(4)
bot.find_followers()

time.sleep(4)
bot.follow()
