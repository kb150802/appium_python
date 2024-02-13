import pytest
from appium.webdriver.appium_service import AppiumService

from AppiumTests.Login import login
from AppiumTests.creatingSession import newSession
import time
from loginData import getData


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
