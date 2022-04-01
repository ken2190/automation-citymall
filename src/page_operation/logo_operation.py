
from appium.webdriver.common.appiumby import AppiumBy
from page_object.logo_object import get_logoXpath

class Logo_operation:

    def operation(self,driver):
        # # Press continue button at the beginning
        driver.find_element(AppiumBy.XPATH,get_logoXpath()).click()
        driver.implicitly_wait(60)