from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By

import logging

from base_page import Base_page

class Home_page(Base_page): #am construit o clasa
    def open_home_page(self): #am scris o metoda
        self.chrome.get("https://magento.softwaretestingboard.com/") #am creat o comanda care sa deschida automat un site

    def sign_in_page(self): #am definit o metoda
        page_url = "https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/" # am definit o variabila
        assert self.chrome.current_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {self.chrome.current_url}") #de verificare de tip assert

    def create_account_page(self): #am definit o metoda
        page_url = "https://magento.softwaretestingboard.com/customer/account/create/" # am definit o variabila
        assert self.chrome.current_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {self.chrome.current_url}")  #de verificare de tip assert

    def account_page(self): #am definit o metoda
        page_url = "https://magento.softwaretestingboard.com/customer/account/" # am definit o variabila
        assert self.chrome.current_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {self.chrome.current_url}") #de verificare de tip assert



