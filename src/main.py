from Resources.base import base
from page_operation.logo_operation import Logo_operation
import Resources.base as bs
from page_operation.otp_operation import Otp_operation

caps_driver=bs.base()
driver=caps_driver.get_cap()
'''
Running Each method for automation operation
'''
#Logo Operation Initialized
operation_logo=Logo_operation()
operation_logo.operation(driver)

# #OTP Operation Initialized
operation_Otp=Otp_operation()

operation_Otp.insert_number(driver)
operation_Otp.clickGetOtp(driver)
operation_Otp.insert_otp(driver)
operation_Otp.clickOtpContinue(driver)