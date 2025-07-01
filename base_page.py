from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import logging

from browser import Browser
from selectors_list import Selectors_List


class Base_page(Browser, Selectors_List):
    def the_email_is_inserted(self,email):
        try:
            self.chrome.find_element(*self.EMAIL).send_keys(email)
            logging.info('The email address is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the last name : {str(t)}')

    def the_password_is_inserted(self,password):
        try:
            self.chrome.find_element(*self.PASSWORD).send_keys(password)
            logging.info('The password is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the last name : {str(t)}')


