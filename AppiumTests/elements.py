from appium.webdriver.common.appiumby import AppiumBy

def login_email_ele(driver):
    eles =  driver.find_elements(AppiumBy.ID, 'email.titan_internal:id/emailView')
    if len(eles) > 0:
        return eles[0]
    return False

def login_password_ele(driver):
    return driver.find_element(AppiumBy.ID, 'email.titan_internal:id/password_toggle')


def login_button_ele(driver):
    return  driver.find_element(AppiumBy.ID, 'email.titan_internal:id/appCompatButton')


def allow_button_ele(driver):
    return driver.find_elements(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')


def profile_ele(driver):
    return driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Switch account')


def manage_account_ele(driver):
    return driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Manage accounts on this device"]')


def account_logot_ele(driver):
    return driver.find_element(AppiumBy.ID, 'email.titan_internal:id/deleteIcon')


def confirm_logout_ele(driver):
    return driver.find_element(AppiumBy.ID, 'android:id/button1')


def new_mail_ele(driver):
    return driver.find_element(AppiumBy.ID,'email.titan_internal:id/compose_button')


def followup_dateAndTime_ele(driver):
    return driver.find_element(AppiumBy.ID,'email.titan_internal:id/followupReminder')


def pickFollowup_date_time_ele(driver):
    return driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Pick a date and time"]')


def pickFolloup_date_ele(driver):
    return driver.find_element(AppiumBy.ID, 'email.titan_internal:id/customDate')


def nextMonth_button_ele(driver):
    return driver.find_element(AppiumBy.ID, 'android:id/next')


def set_followupDate_ele(driver):
    return driver.find_element(AppiumBy.ID, 'android:id/button1')


def pickFollowup_time_ele(driver):
    return driver.find_element(AppiumBy.XPATH,'//android.widget.ImageButton[@content-desc="Switch to text input mode '
                                              'for the time input."]')


def enterFollowup_hours_ele(driver):
    return driver.find_element(AppiumBy.ID,'android:id/input_hour')


def enterFollowup_minutes_ele(driver):
    return driver.find_element(AppiumBy.ID,'android:id/input_minute')


def choose_AMPM_ele(driver):
    return driver.find_element(AppiumBy.XPATH,
                               "//android.widget.Spinner[@resource-id=\"android:id/am_pm_spinner\"]")

def set_followupTime_ele(driver):
    return driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK")')


def set_followupButton_ele(driver):
    return driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SET")')


def attachment_btn_ele(driver):
    return driver.find_element(AppiumBy.ID, 'email.titan_internal:id/attachmentButton')



def incorrect_email_pass_dialog(driver):
    return driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Incorrect '
                                                                                'Email or Password")')


def invalid_email_message(driver):
    return driver.find_elements(AppiumBy.ID, '00000000-0000-000c-ffff-ffff0000002e')


def invalid_password_message(driver):
    return driver.find_elements(AppiumBy.ID, '00000000-0000-000c-ffff-ffff00000031')


def menu_ele(driver):
    return driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Navigate up')