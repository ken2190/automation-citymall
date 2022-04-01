from appium import webdriver

class base:
    def get_cap(self):

        desired_cap = {"platformName": "Android",
                    "noReset": "false",
                    "fullReset": "false",
                    "newCommandTimeout": "600000",
                    # "enforceAppInstall":"false",
                    # "autoLaunch":"false",
                    "appium:appPackage": "live.citymall.customer.prod",
                    "appium:appActivity": "live.citymall.customer.MainActivity",
                    # "appium:app": "C:\\Users\\admin\\Downloads\\live.citymall.customer.prod_2022-02-10.apk",
                    # "appium:deviceName": "",
                    "automationName": "UiAutomator2"}

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        driver.implicitly_wait(60)
        return driver
