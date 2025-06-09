from selenium import webdriver
from selenium.webdriver.common.by import By  # Finding an element based on {insert type}
from selenium.webdriver.common.keys import Keys  #  Allows keyboard keys to be auto-pressed#

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True) # KEEPS BROWSER OPEN

driver = webdriver.Edge(options=edge_options)
"""PREVIOUS DAY CHALLENGE BUT USING SELENIUM"""
# driver.get("https://www.amazon.com/TRAVANDO-Wallet-Blocking-AUSTIN-Minimalist/dp/B07P73KK1J/")
#
# dollar_price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# cents_price = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is ${dollar_price.text}.{cents_price.text}")

# driver.close()  # Closes a singular (particular) tab

"""EXAMPLE USING SELENIUM"""

# driver.get("https://www.python.org/")
#
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_widget = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a" )
# print(documentation_widget.text)
#
# # If locating a path fails, USE XPATH
# xpath_example = driver.find_element(By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(xpath_example.text)

"""ANOTHER EXAMPLE USING AUTO-CLICKS"""
# Example Signup
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
sign_up = driver.find_element(By.CSS_SELECTOR, value='[type="submit"]')
first_name.send_keys("uwu")
last_name.send_keys("uwu")
email.send_keys("uwu@uwu.com")
sign_up.send_keys(Keys.ENTER)


driver.quit()

