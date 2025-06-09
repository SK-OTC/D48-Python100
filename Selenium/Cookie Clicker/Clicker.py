from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException

cookie_link = "https://orteil.dashnet.org/experiments/cookie/"

start_time = datetime.now()
measured_time = datetime.now().time()

five_min = True
web_options = webdriver.EdgeOptions()
web_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=web_options)

driver.get(cookie_link)
click_cookie = driver.find_element(By.ID, value="cookie")
cookie_num = driver.find_element(By.ID, value="money")


while five_min:
    measured_time = datetime.now()  # Get current time
    timediff = measured_time - start_time
    click_cookie.click()
    buy_upgrade = {}
    if timediff.seconds == 300:
        five_min = False
        cps = driver.find_element(By.ID, value="cps")
        print(cps.text)
    try:
        if timediff.seconds % 5 == 0:
            perks = {}
            cookie_count = int(cookie_num.text)
            store = driver.find_elements(By.CSS_SELECTOR, value="#store b")
            for item in store:
                text = item.text
                if text != "":
                    perks[int(text.split()[-1].replace(",", ""))] = item
                    label = text.split()[0]

            for num, name in perks.items():
                if cookie_count > num:
                    buy_upgrade[num] = name
                    expensive_upgrade = max(buy_upgrade)
                    get_upgrade = perks[expensive_upgrade]
                    get_upgrade.click()
    except StaleElementReferenceException:
        pass

driver.quit()
