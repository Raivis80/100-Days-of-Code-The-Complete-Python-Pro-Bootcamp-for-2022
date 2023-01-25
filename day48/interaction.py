from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

wiki_main = 'http://en.wikipedia.org/wiki/Main_Page'

# Create a new instance of the Chrome driver
service = Service("D:\development\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get(wiki_main)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()


# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
#
# search.send_keys(Keys.ENTER)

link = "https://www.appbrewery.co/p/newsletter/"
email = "rp42dev@gmail.com"

driver.get(link)

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(email)
email_input.send_keys(Keys.ENTER)


