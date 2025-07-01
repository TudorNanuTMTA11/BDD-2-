from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By


import logging

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from base_page import Base_page

class Sign_in_page(Base_page):
    def sign_in_option(self):
        try:
            sign_in_option = self.chrome.find_element(*self.SIGN_IN_OPT)
            if sign_in_option:
                sign_in_option.click()
            else:
                raise AssertionError('Sign in option element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the sign in option : {str(i)}")

    def sign_in_button(self):
        try:
            sign_in_button = self.chrome.find_element(*self.SIGN_IN_BTN)
            if sign_in_button:
                sign_in_button.click()
            else:
                raise AssertionError('Sign in button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the sign in button : {str(i)}")

    def forget_password_button(self):
        try:
            forget_password_button = self.chrome.find_element(*self.FORGET_YOUR_PASSWORD_BTN)
            if forget_password_button:
                forget_password_button.click()
            else:
                raise AssertionError('Forget password button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the forget password button : {str(i)}")

    def forget_inserting_email_error(self):
        self.chrome.find_element(*self.EMAIL_ERROR)

    def forget_inserting_password_error(self):
        self.chrome.find_element(*self.PASSWORD_ERROR)

    def reset_my_password_button(self):
        try:
            reset_my_password_button = self.chrome.find_element(*self.FORGET_YOUR_PASSWORD_BTN)
            if reset_my_password_button:
                reset_my_password_button.click()
            else:
                raise AssertionError('Reset my password button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the reset my password button : { str(i)}")

    def confirmation_message(self):
        try:
            confirmation_message = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.CONFIRMATION_MESSAGE))
            assert confirmation_message.is_displayed()
            logging.info('The confirmation message is displayed')
        except Exception as l:
            logging.error(f"An error occurred while displaying the confirmation message"
                          f" website : {str(l)}")
















