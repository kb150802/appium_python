import time
from appium.webdriver.common.appiumby import AppiumBy

idEmailId = 'email.titan_internal:id/emailView'
idPassword = 'email.titan_internal:id/password_toggle'
idLoginButton = 'email.titan_internal:id/appCompatButton'
idAllowButton = 'com.android.permissioncontroller:id/permission_allow_button'


def login(driver, email, password):
    driver.find_element(by=AppiumBy.ID,value=idEmailId).send_keys(email)
    driver.find_element(by=AppiumBy.ID,value=idPassword).send_keys(password)
    driver.find_element(by=AppiumBy.ID,value=idLoginButton).click()
    time.sleep(5)
    allow_button = driver.find_elements(by=AppiumBy.ID,value=idAllowButton)
    if len(allow_button) > 0:
        allow_button[0].click()
        time.sleep(10)
        return True
    else:
        return False


