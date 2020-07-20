from time import sleep

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

caps = DesiredCapabilities.CHROME

driver = webdriver.Remote(command_executor='http://54.183.169.175:4444/wd/hub', desired_capabilities=caps)

driver.get('https://www.google.com/')
print("Open Google")
sleep(5)

driver.quit()
