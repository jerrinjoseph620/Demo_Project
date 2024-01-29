from selenium import webdriver

driver = webdriver.Edge()
url = "https://rcvacademy.com"
driver.get(url)
print(driver.title)
driver.maximize_window()
driver.minimize_window()
driver.close()