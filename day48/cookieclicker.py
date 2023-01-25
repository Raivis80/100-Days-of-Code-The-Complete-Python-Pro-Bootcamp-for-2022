from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

link = "http://orteil.dashnet.org/experiments/cookie/"

# Create a new instance of the Chrome driver
service = Service("D:\development\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get(link)

cookie = driver.find_element(By.ID, "cookie")
store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in store_items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in all_prices:
            if price.text != "":
                item_prices.append(int(price.text.split("-")[1].strip().replace(",", "")))
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(By.ID, "money")
        money = int(money_element.text.replace(",", ""))
        print(money)
        for cost, id in cookie_upgrades.items():
            if money > cost:
                upgrade_action = f"document.getElementById('{id}').click()"
                driver.execute_script(upgrade_action)
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps")
        print(cookie_per_s.text)
        break

driver.quit()