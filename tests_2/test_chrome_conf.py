import pytest

from time import sleep


@pytest.mark.usefixtures("driver_chrome")
class TestChrome(object):
    def test_chrome_conf(self):
        self.driver.get('https://www.google.com/')
        print("Open Google in Chrome")
        sleep(2)
