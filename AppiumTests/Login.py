
from AppiumTests import elements
from AppiumTests import scroller


def login(driver, email, password):
    login_email = elements.login_email_ele(driver)
    if not login_email:
        return
    elements.login_email_ele(driver).send_keys(email)
    scroller.Scroller.scrollToText('Enter Your Password', driver)
    elements.login_password_ele(driver).send_keys(password)
    driver.press_keycode(66)
    scroller.Scroller.scrollToText('Login', driver)
    elements.login_button_ele(driver).click()
    allow_button = elements.allow_button_ele(driver)
    if len(allow_button) > 0:
        allow_button[0].click()
        return True
    else:
        return False
