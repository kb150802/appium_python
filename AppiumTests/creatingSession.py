from appium import webdriver
from pathlib import Path
from appium.options.android import UiAutomator2Options
import time

desired_caps = dict(
        platformName='Android',
        app=str(Path().absolute().parent) + '\\app\\titan.apk',
        automationName='UIAutomator2',
        appWaitPackage='email.titan_internal',
        appWaitActivity='to.go.cassie.login.LoginActivity',
        platformVersion='9',
        # orientation='LANDSCAPE'
        # ensureWebViewsHavePages="true",
        # appiumDeviceName='emulator-5554'
    )
PORT_URL = 'http://127.0.0.1:4723'


def newSession():

    capability_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote(PORT_URL, options=capability_options)
    driver.implicitly_wait(10)
    driver.set_network_connection(2)
    return driver

#
# +--------------------+------+------+---------------+
#             | Value (Alias)      | Data | Wifi | Airplane Mode |
#             +====================+======+======+===============+
#             | 0 (None)           | 0    | 0    | 0             |
#             +--------------------+------+------+---------------+
#             | 1 (Airplane Mode)  | 0    | 0    | 1             |
#             +--------------------+------+------+---------------+
#             | 2 (Wifi only)      | 0    | 1    | 0             |
#             +--------------------+------+------+---------------+
#             | 4 (Data only)      | 1    | 0    | 0             |
#             +--------------------+------+------+---------------+
#             | 6 (All network on) | 1    | 1    | 0             |
#             +--------------------+------+------+---------------+
