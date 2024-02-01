import time

import swipe_operations
from scroller import Scroller
from Login import login
from creatingSession import newSession
from appium.webdriver.common.touch_action import TouchAction

from logout import logout
from appium.webdriver.common.appiumby import AppiumBy
#
# newmailid = 'email.titan_internal:id/compose_button'
# recepientid = 'email.titan_internal:id/toContacts'
# subjectid = 'email.titan_internal:id/subjectText'
# bodyid = 'edit-box'
# sendbuttonid = 'email.titan_internal:id/send_action'

mail_x_path = '//androidx.recyclerview.widget.RecyclerView[@resource-id="email.titan_internal:id/threadList"]/android.view.ViewGroup[2]'

driver = newSession()
actions = TouchAction(driver)

login(driver, 'kushagra@titan.email', '')
time.sleep(5)

first_mail = driver.find_element(AppiumBy.XPATH, mail_x_path)
swipe_operations.swipe_left(first_mail,driver)

# logout(driver)
