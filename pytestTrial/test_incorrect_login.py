import pytest
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from AppiumTests.creatingSession import newSession
import time
from loginData import get_incorrect_data, get_invalid_data
from AppiumTests import elements


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


@pytest.mark.parametrize("username,password",get_incorrect_data())
def test_incorrect_login(username, password):
    elements.login_email_ele(driver).send_keys(username)
    elements.login_password_ele(driver).send_keys(password)
    elements.login_button_ele(driver).click()
    incorrect_email_dialog = elements.incorrect_email_pass_dialog(driver)
    if len(incorrect_email_dialog) == 0:
        pytest.fail("Test Failed")


@pytest.mark.parametrize("username, password", get_invalid_data())
def test_invalid_login(username, password):
    elements.login_email_ele(driver).send_keys(username)
    elements.login_password_ele(driver).send_keys(password)
    elements.login_button_ele(driver).click()
    invalid_email_message = elements.invalid_email_message(driver)
    invalid_password_message = elements.invalid_password_message(driver)

    if len(invalid_password_message) > 0 or len(invalid_email_message) > 0:
        pytest.fail("Test Failed")

