


import logging



from base_page import Base_page

class Checkout(Base_page):
    def the_company_is_inserted(self, company):
        try:
            self.chrome.find_element(*self.COMPANY).send_keys(company)
            logging.info('The company is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the company : {str(t)}')

    def the_street_address_is_inserted(self, street_address):
        try:
            self.chrome.find_element(*self.STREET_ADDRESS).send_keys(street_address)
            logging.info('The street address is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the street address : {str(t)}')

    def the_city_is_inserted(self, city):
        try:
            self.chrome.find_element(*self.CITY).send_keys(city)
            logging.info('The city is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the city : {str(t)}')

    def the_state_is_selected(self, state):
        try:
            self.chrome.find_element(*self.STATE).is_selected(state)
            logging.info('The state is selected')
        except Exception as t:
            logging.error(f'An error occurred while selecting the state : {str(t)}')

    def the_country_is_selected(self, country):
        try:
            self.chrome.find_element(*self.COUNTRY_ID).is_selected(country)
            logging.info('The country is selected')
        except Exception as t:
            logging.error(f'An error occurred while selecting the country : {str(t)}')

    def the_postal_code_is_inserted(self,postal_code):
        try:
            self.chrome.find_element(*self.POSTCODE).send_keys(postal_code)
            logging.info('The postal code is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the postal code : {str(t)}')

    def the_phone_is_inserted(self, phone_number):
        try:
            self.chrome.find_element(*self.PHONE_NUMBER).send_keys(phone_number)
            logging.info('The phone number is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the phone number : {str(t)}')

    def the_price_is_selected(self):
        try:
            select_price_button = self.chrome.find_element(*self.SELECT_PRICE)
            if select_price_button:
                select_price_button.click()
            else:
                raise AssertionError('Select price button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the select price button : {str(i)}")

    def next_button(self):
        try:
            next_button = self.chrome.find_element(*self.NEXT_BTN)
            if next_button:
                next_button.click()
            else:
                raise AssertionError('Next button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the next button : { str(i)}")

    def place_order_button(self):
        try:
            place_order_button = self.chrome.find_element(*self.PLACE_ORDER_BTN)
            if place_order_button:
                place_order_button.click()
            else:
                raise AssertionError('Place order button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the place order button : { str(i)}")

    def continue_shopping_button(self):
        try:
            continue_shopping_button = self.chrome.find_element(*self.CONTINUE_SHOPPING_BTN)
            if continue_shopping_button:
                continue_shopping_button.click()
            else:
                raise AssertionError('Continue shopping button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the continue shopping button : { str(i)}")

    def this_is_a_required_field(self):
        self.chrome.find_elements(*self.THIS_IS_A_REQUIRED_FIELD)

    def error_validation_message(self):
        self.chrome.find_elements(*self.ERROR_VALIDATION_MESSAGE)

    def sign_in_option_2(self):
        try:
            sign_in_option_2 = self.chrome.find_element(*self.SIGN_IN_OPT_2)
            if sign_in_option_2:
                sign_in_option_2.click()
            else:
                raise AssertionError('Sign in option element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the sign in option : { str(i)}")

    def sign_in_button_2(self):
        try:
            sign_in_button_2 = self.chrome.find_element(*self.SIGN_IN_BTN_2)
            if sign_in_button_2:
                sign_in_button_2.click()
            else:
                raise AssertionError('Sign in option element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the sign in option : { str(i)}")

    def the_email_is_inserted_2(self,email):
        try:
            self.chrome.find_element(*self.LOGIN_EMAIL).send_keys(email)
            logging.info('The email address is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the email : {str(t)}')

    def the_password_is_inserted_2(self,password):
        try:
            self.chrome.find_element(*self.LOGIN_PASSWORD).send_keys(password)
            logging.info('The password is inserted')
        except Exception as t:
            logging.error(f'An error occurred while using the last name : {str(t)}')

    def shipping_address_item(self):
        self.chrome.find_elements(*self.SHIPPING_ADDRESS_ITEM)

    def new_address_button(self):
        try:
            new_address_button = self.chrome.find_element(*self.NEW_ADDRESS)
            if new_address_button:
                new_address_button.click()
            else:
                raise AssertionError('New address button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the new address button : { str(i)}")

    def ship_here_button(self):
        try:
            ship_here_button = self.chrome.find_element(*self.SHIP_HERE)
            if ship_here_button:
                ship_here_button.click()
            else:
                raise AssertionError('Ship here button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the ship here button : {str(i)}")
