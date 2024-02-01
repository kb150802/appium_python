import time
from appium.webdriver.common.appiumby import AppiumBy

profileaccesiblityid = 'Switch account'
manageaccoundxpath = '//android.widget.TextView[@text="Manage accounts on this device"]'
logoutid = 'email.titan_internal:id/deleteIcon'
confirmlogoutid = 'android:id/button1'
idLoginButton = 'email.titan_internal:id/appCompatButton'


def logout(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, profileaccesiblityid).click()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH, manageaccoundxpath).click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID, logoutid).click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID,confirmlogoutid).click()


