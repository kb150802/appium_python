import time
from AppiumTests.Login import login
from creatingSession import newSession


driver = newSession()
login(driver)

driver.activate_app('com.google.android.apps.messaging')
time.sleep(5)
driver.activate_app('email.titan_internal')
time.sleep(5)