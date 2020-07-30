from time import sleep

from selenium import webdriver


def test_two():
    capabilities = {
        "browserName": "firefox",
        "version": "78.0",
        "enableVNC": True,
        "enableVideo": False
    }

    driver = webdriver.Remote(
        command_executor="http://54.193.19.92:4444/wd/hub",
        desired_capabilities=capabilities)

    driver.get('https://www.google.com/')
    print("Opened in Firefox")
    sleep(2)

    driver.quit()
