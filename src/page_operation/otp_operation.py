
from appium.webdriver.common.appiumby import AppiumBy
import Resources.base as bs
from page_object.otp_object import inputNumberXpath,input_number,getOtpXpath,inputOTP,OtpContinue


class Otp_operation:

    def insert_number(self,driver):
        '''
        Inserts Number to get OTP 
        '''
        driver.find_element(AppiumBy.XPATH,inputNumberXpath()).send_keys(input_number())
        driver.implicitly_wait(15)
    
    def clickGetOtp(self,driver):
        '''
        Click Get OTP button 
        '''
        driver.find_element(AppiumBy.XPATH,getOtpXpath()).click()
        driver.implicitly_wait(20000)
    
    def insert_otp(self,driver):
        '''
        Inserts OTP 
        '''
        otp_digit_xpath=inputOTP()

        #1st box
        driver.find_element(AppiumBy.XPATH,
                            otp_digit_xpath[0]).send_keys('7')
        driver.implicitly_wait(20)

        #2st box
        driver.find_element(AppiumBy.XPATH,
                            otp_digit_xpath[1]).send_keys('6')
        driver.implicitly_wait(20)

        #3rd box
        driver.find_element(AppiumBy.XPATH,
                            otp_digit_xpath[2]).send_keys('5')
        driver.implicitly_wait(20)

        #4th box
        driver.find_element(AppiumBy.XPATH,
                            otp_digit_xpath[3]).send_keys('6')
        driver.implicitly_wait(50)
    
    def clickOtpContinue(self,driver):
        
        driver.find_element(AppiumBy.XPATH,
                            OtpContinue()).click()
        driver.implicitly_wait(2000)