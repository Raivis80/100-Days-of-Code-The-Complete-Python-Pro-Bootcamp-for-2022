from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Create a new instance of the Chrome driver
service = Service("D:\development\chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get("https://www.python.org/")

# search = driver.find_element(By.NAME, "q")
# print(search.tag_name)
# print(search.get_attribute("placeholder"))
# search.send_keys("Upcoming Events")
# search_button = driver.find_element(By.CLASS_NAME, "search-button")
# search_button.click()
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)



# documentation_link = driver.find_element(By.LINK_TEXT, "Documentation")
# print(documentation_link.text)

# bug_link_xpath = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link_xpath.text)

# all_links = driver.find_elements(By.TAG_NAME, "a")


event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for i in range(len(event_titles)):
    event = {i: {'time': event_times[i].text, 'name': event_titles[i].text}}
    events.update(event)

print(events)

# driver.quit()