from selenium import webdriver

"""It basically bypass the driver dependecy that requires constant manual download
wrt to the chrome version which is a tedious process by importing ChromeDriverManager 
which again is installed using PIP.
"""

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://rcvacademy.com"
driver.get(url)
print(driver.title)
driver.maximize_window()
driver.minimize_window()
driver.close()