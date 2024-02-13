from AppiumTests import elements


def logout(driver):
    elements.profile_ele(driver).click()
    elements.manage_account_ele(driver).click()
    elements.account_logot_ele(driver).click()
    elements.confirm_logout_ele(driver).click()


