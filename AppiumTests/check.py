from appium.webdriver.common.appiumby import AppiumBy

from AppiumTests.Login import login
from AppiumTests.logout import logout
from creatingSession import newSession

driver = newSession()
login(driver)

# logs = driver.get_log('logcat')
# log_messages = list(map(lambda log: log['message'], logs))
# print(log_messages)


import elements
elements.new_mail_ele(driver).click()
elements.attachment_btn_ele(driver).click()
driver.find_element(AppiumBy.ID, 'com.android.documentsui:id/icon_thumb').click()
driver.find_element(AppiumBy.ID, 'email.titan_internal:id/toContacts').send_keys("sachinp@titan.email\n")
driver.find_element(AppiumBy.ID, 'email.titan_internal:id/subjectText').send_keys("Hii\n")
driver.find_element(AppiumBy.ID, 'email.titan_internal:id/send_action').click()
driver.find_element(AppiumBy.ID, 'android:id/button2').click()


# driver.terminate_app('email.titan_internal')
# driver.activate_app('email.titan_internal')

# logout(driver)

