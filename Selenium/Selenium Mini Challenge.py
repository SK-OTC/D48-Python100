from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, value=".last time")
event_title = driver.find_elements(By.CSS_SELECTOR, value=".event-widget.last li a")

schedule = {}
for n in range(len(dates)):
    schedule[n] = {
        "time": dates[n].text,
    "name": event_title[n].text
    }

print(schedule)

driver.quit()