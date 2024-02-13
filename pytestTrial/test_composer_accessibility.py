# Test to verify that the composer is accessible from all the folders

import pytest
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from AppiumTests.creatingSession import newSession
import time
from loginData import getData
from AppiumTests import elements
from AppiumTests.Login import  login


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


def test_composer_accessibility():
    username, password = getData()
    login(driver,username,password)
    folders = ['Inbox', 'Sent Mail', 'Spam', 'Archive', 'Trash', 'Drafts', 'Scheduled']

    for folder in folders:
        elements.menu_ele(driver).click()
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("' + folder + '")').click()
        try:
            elements.new_mail_ele(driver)
        except:
            pytest.fail("Test Failed")
        time.sleep(5)
