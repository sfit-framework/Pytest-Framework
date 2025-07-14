# from selenium.webdriver.common.by import By
# class LoginLocator:
#     Login_button_lo=By.xpath,'//span[text()="Login"]'
#     verify_btn_clicked_loc=By.xpath,'//button[text()="Request OTP"]'

from selenium.webdriver.common.by import By

class LoginLocator:
    Login_button_lo = (By.XPATH, '//span[text()="Login"]')
    verify_btn_clicked_loc = (By.XPATH, '//button[text()="Request OTP"]')
