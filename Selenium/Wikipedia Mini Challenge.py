from selenium import webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)


driver = webdriver.Edge(edge_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_num = driver.find_element(By.CSS_SELECTOR, value="[title='Special:Statistics']")

print(article_num.text)
article_num.click() # Self-clicks link

driver.quit()