import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import Base_page

class Create_account(Base_page):

    def click_create_an_account_option(self):
        try:
            create_an_account_option = self.chrome.find_element(*self.CREATE_AN_ACCOUNT_OPT)
            if create_an_account_option:
                create_an_account_option.click()
            else:
                raise AssertionError('Create an account option element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the create an account option : {str(i)}")
    def the_first_name_is_inserted(self, first_name):
        try:
            self.chrome.find_element(*self.FIRST_NAME).send_keys(first_name)
            logging.info('The first name is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the first name : {str(t)}')

    def the_last_name_is_inserted(self, last_name):
        try:
            self.chrome.find_element(*self.LAST_NAME).send_keys(last_name)
            logging.info('The last name is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the last name : {str(t)}')



    def the_password_is_confirmed(self,password):
        try:
            self.chrome.find_element(*self.PASSWORD_CONFIRMATION).send_keys(password)
            logging.info('The password is confirmed')
        except Exception as t:
            logging.error(f'An error occurred while using the last name : {str(t)}')

    def click_create_an_account_button(self):
        try:
            create_an_account_button = self.chrome.find_element(*self.CREATE_AN_ACCOUNT_BTN)
            if create_an_account_button:
                create_an_account_button.click()
            else:
                raise AssertionError('Create an account button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the create an account button : {str(i)}")
