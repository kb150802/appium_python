from appium.webdriver.common.touch_action import TouchAction


def long_press(element,driver):
    actions = TouchAction(driver)
    actions.long_press(element, None, None, 3000).perform()
    return

