import time

from selenium.webdriver.support.ui import Select
from locators.login_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login_page:

    def __init__(self, driver):
        self.driver = driver

    def click_on_login_btn(self):
        wait=WebDriverWait(self.driver,15)
        wait.until(EC.visibility_of_element_located(LoginLocator.Login_button_lo))
        self.driver.find_element(*LoginLocator.Login_button_lo).click()
        wait.until(EC.visibility_of_element_located(LoginLocator.verify_btn_clicked_loc))

        element=self.driver.find_element(*LoginLocator.verify_btn_clicked_loc)
        text=element.text

        assert text=="Request OTP","Element not found"