import pytest
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from AppiumTests.Login import login
from AppiumTests.creatingSession import newSession
import time


def setup_function():
    print("Starting Testcases\n")
    global appium_service
    appium_service = AppiumService()
    appium_service.start()
    global driver
    driver = newSession()


def teardown_function():
    print("Completed Testcases\n")
    time.sleep(2)
    driver.quit()
    appium_service.stop()


def getData():
    return [
        ["kushagra@titan.email", ""],
    ]

@pytest.mark.parametrize("username,password",getData())
def test_login(username, password):
    assert login(driver,username, password), "Login Failed"
    # assert False

