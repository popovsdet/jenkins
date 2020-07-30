from time import sleep

from selenium import webdriver


def test_chrome_d():
    capabilities = {
        "browserName": "chrome",
        "version": "84.0",
        "enableVNC": True,
        "enableVideo": False
    }

    driver = webdriver.Remote(
        command_executor="http://54.193.19.92:4444/wd/hub",
        desired_capabilities=capabilities)

    driver.get('https://www.google.com/')
    print("Open Google in Chrome")
    sleep(2)

    driver.quit()
