from appium import webdriver
from pathlib import Path
from appium.options.android import UiAutomator2Options
import time

def newSession():
    desired_caps = dict(
        platformName='Android',
        app=str(Path().absolute().parent) + '\\app\\titan.apk',
        automationName='UIAutomator2',
        appWaitPackage='email.titan_internal',
        appWaitActivity='to.go.cassie.login.LoginActivity',
        platformVersion='14',
        ensureWebViewsHavePages="true",
        # appiumDeviceName='emulator-5554'
    )

    capability_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capability_options)
    time.sleep(5)
    return driver
