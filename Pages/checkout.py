



from base_page import Base_page

class Checkout(Base_page):
    def the_company_is_inserted(self, company):
       self.chrome.find_element(*self.COMPANY).send_keys(company)

    def the_street_address_is_inserted(self, street_address):
        self.chrome.find_element(*self.STREET_ADDRESS).send_keys(street_address)

    def the_city_is_inserted(self, city):
        self.chrome.find_element(*self.CITY).send_keys(city)

    def the_state_is_selected(self, state):
        self.chrome.find_element(*self.STATE).is_selected(state)


    def the_country_is_selected(self, country):
        self.chrome.find_element(*self.COUNTRY_ID).is_selected(country)


    def the_postal_code_is_inserted(self,postal_code):
        self.chrome.find_element(*self.POSTCODE).send_keys(postal_code)


    def the_phone_is_inserted(self, phone_number):
       self.chrome.find_element(*self.PHONE_NUMBER).send_keys(phone_number)

    def the_price_is_selected(self):
        select_price_button = self.chrome.find_element(*self.SELECT_PRICE)
        select_price_button.click()

    def next_button(self):
        next_button = self.chrome.find_element(*self.NEXT_BTN)
        next_button.click()

    def place_order_button(self):
        place_order_button = self.chrome.find_element(*self.PLACE_ORDER_BTN)
        place_order_button.click()

    def continue_shopping_button(self):
        continue_shopping_button = self.chrome.find_element(*self.CONTINUE_SHOPPING_BTN)
        continue_shopping_button.click()


    def this_is_a_required_field(self):
        self.chrome.find_elements(*self.THIS_IS_A_REQUIRED_FIELD)

    def error_validation_message(self):
        self.chrome.find_elements(*self.ERROR_VALIDATION_MESSAGE)

    def sign_in_option_2(self):
        sign_in_option_2 = self.chrome.find_element(*self.SIGN_IN_OPT_2)
        sign_in_option_2.click()



    def sign_in_button_2(self):
        sign_in_button_2 = self.chrome.find_element(*self.SIGN_IN_BTN_2)
        sign_in_button_2.click()


    def the_email_is_inserted_2(self,email):
        self.chrome.find_element(*self.LOGIN_EMAIL).send_keys(email)


    def the_password_is_inserted_2(self,password):
        self.chrome.find_element(*self.LOGIN_PASSWORD).send_keys(password)

    def shipping_address_item(self):
        self.chrome.find_elements(*self.SHIPPING_ADDRESS_ITEM)

    def new_address_button(self):
        new_address_button = self.chrome.find_element(*self.NEW_ADDRESS)
        new_address_button.click()



    def ship_here_button(self):
        ship_here_button = self.chrome.find_element(*self.SHIP_HERE)
        ship_here_button.click()

    def add_to_cart_radiant_tee_button(self,product_name):
        add_to_cart_radiant_tee_button = self.chrome.find_element(*self.ADD_TO_CART_RADIANT_TEE)
        add_to_cart_radiant_tee_button.click(product_name)

    def size_XS_radiant_tee(self):
        self.chrome.find_elements(*self.SIZE)

    def color_blue_radiant_tee(self):
        self.chrome.find_elements(*self.COLOR)

