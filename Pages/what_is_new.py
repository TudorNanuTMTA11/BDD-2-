import logging



from base_page import Base_page

class What_is_new(Base_page):
    def what_is_new_page(self): #am definit o metoda
        page_url = "https://magento.softwaretestingboard.com/what-is-new.html" # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {page_url}") #de verificare de tip assert

    def add_to_cart_wayfarer_messenger_bag_button(self):
        try:
            add_to_cart_wayfarer_messenger_bag_button = self.chrome.find_element(*self.ADD_TO_CART_WAYFARER_MESSENGER_BAG)
            if add_to_cart_wayfarer_messenger_bag_button:
                add_to_cart_wayfarer_messenger_bag_button.click()
            else:
                raise AssertionError('Add to cart button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the add to cart button: {str(i)}")

    def action_showcart_wayfarer_messenger_bag_button(self):
        try:
            action_showcart_wayfarer_messenger_bag_button = self.chrome.find_element(*self.ACTION_SHOWCART_WAYFARER_MESSENGER_BAG)
            if action_showcart_wayfarer_messenger_bag_button:
                action_showcart_wayfarer_messenger_bag_button.click()
            else:
                raise AssertionError('Action showcart button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the action showcart button: {str(i)}")

    def proceed_to_checkout_button(self):
        try:
            proceed_to_checkout_button = self.chrome.find_element(*self.PROCEED_TO_CHECKOUT)
            if proceed_to_checkout_button:
                proceed_to_checkout_button.click()
            else:
                raise AssertionError('Proceed to checkout button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the proceed to checkout button: {str(i)}")



