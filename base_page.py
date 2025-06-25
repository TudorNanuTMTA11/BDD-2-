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


    def check_error_message(self, by, selector, expected_error_message):
                        # metoda presence_of_element_located primeste doi parametrii: tipul selectorului si valoarea selectorului
                        error_message_web_element = WebDriverWait(self.chrome, 20).until(
                                EC.presence_of_element_located((by, selector)))
                        actual_error_message_text = error_message_web_element.text
                        assert expected_error_message == actual_error_message_text, f"Error, the message is incorrect. Expected: {expected_error_message}, actual: {actual_error_message_text}"
