from pytest import fixture
from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@fixture(scope="class")
def driver_chrome(request):
    caps = DesiredCapabilities.CHROME
    driver = webdriver.Remote(command_executor='http://18.144.87.8:4444/wd/hub', desired_capabilities=caps)
    request.cls.driver = driver
    yield
    driver.close()


@fixture(scope="class")
def driver_firefox(request):
    caps = DesiredCapabilities.FIREFOX
    driver = webdriver.Remote(command_executor='http://18.144.87.8:4444/wd/hub', desired_capabilities=caps)
    request.cls.driver = driver
    yield
    driver.close()
