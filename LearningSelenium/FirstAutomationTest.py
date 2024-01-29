from selenium import webdriver

driver = webdriver.Chrome()

url = "https://rcvacademy.com"

driver.get(url)

driver.implicitly_wait(5)

driver.maximize_window()

driver.implicitly_wait(5)

print(driver.title)

driver.close()