import time
from datetime import datetime

from appium.webdriver.common.appiumby import AppiumBy

from AppiumTests import elements
from AppiumTests.Login import login
from creatingSession import newSession
from appium.webdriver.common.touch_action import TouchAction


def pickDate(toSetDate, toSetMonth, toSetYear, toSetHours, toSetMinutes, toSet_AM_PM):
    driver = newSession()
    actions = TouchAction(driver)
    login(driver)

    elements.new_mail_ele(driver).click()
    time.sleep(10)

    elements.followup_dateAndTime_ele(driver).click()
    elements.pickFollowup_date_time_ele(driver).click()
    elements.pickFolloup_date_ele(driver).click()

    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    numberOfPush = (toSetYear - currentYear)*12 + toSetMonth - currentMonth

    while numberOfPush:
        elements.nextMonth_button_ele(driver).click()
        numberOfPush = numberOfPush - 1

    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("' + str(toSetDate) + '")').click()
    elements.set_followupDate_ele(driver).click()

    elements.pickFollowup_time_ele(driver).click()

    elements.enterFollowup_hours_ele(driver).send_keys(toSetHours)
    elements.enterFollowup_minutes_ele(driver).send_keys(toSetMinutes)
    elements.choose_AMPM_ele(driver).click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("'+toSet_AM_PM+'")').click()

    elements.set_followupTime_ele(driver).click()
    elements.set_followupButton_ele(driver).click()
    driver.terminate_app('email.titan_internal')
    driver.activate_app('email.titan_internal')


pickDate(10,10,2024,8,13,'PM')