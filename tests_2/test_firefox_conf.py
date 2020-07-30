import pytest

from time import sleep


@pytest.mark.usefixtures("driver_firefox")
class TestFirefox(object):
    def test_firefox_conf(self):
        self.driver.get('https://www.google.com/')
        print("Open Google in Chrome")
        sleep(2)
