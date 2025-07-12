import logging

from base_page import Base_page

class Home_page(Base_page): #am construit o clasa
    def open_home_page(self): #am scris o metoda
        self.chrome.get("https://magento.softwaretestingboard.com/") #am creat o comanda care sa deschida automat un site

    def click_consent_button(self):
        try:
            consent_button = self.chrome.find_element(*self.CONSENT_BTN)
            if consent_button:
                consent_button.click()
            else:
                raise AssertionError('Consent button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the consent button: {str(i)}")

    def sign_in_page(self): #am definit o metoda
        page_url = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/" # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {page_url}") #de verificare de tip assert

    def create_account_page(self): #am definit o metoda
        page_url = "https://magento.softwaretestingboard.com/customer/account/create/" # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {page_url}")  #de verificare de tip assert


    def account_page(self): #am definit o metoda
        page_url = "https://magento.softwaretestingboard.com/customer/account/" # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {page_url}") #de verificare de tip assert

    def catalog_page(self):
        page_url = "https://magento.softwaretestingboard.com/catalogsearch/result/?q=+Wayfarer+Messenger+Bag" # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {page_url}") #de verificare de tip assert"  # am definit o variabila

    def search_entire_here(self):
        self.chrome.find_element(*self.SEARCH_ENTIRE_HERE)

    def wayfarer_messenger_bag_search(self):
         self.chrome.find_element(*self.SEARCH)

    def wayfarer_messenger_bag_product(self):
        self.chrome.find_element(*self.WAYFARER_MESSENGER_BAG_PRODUCT)

    def checkout_page(self):
        page_url = "https://magento.softwaretestingboard.com/checkout/#shipping"  # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}",  # am scris o metoda
                                      f"Actual current_url {page_url}")  # de verificare de tip assert"  # am definit o variabila

   

