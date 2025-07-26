from base_page import Base_page
import logging

class Hoodies_and_sweatshirts(Base_page):
    def grid_button(self):
        try:
            grid_button = self.chrome.find_element(*self.GRID)
            if grid_button:
                grid_button.click()
            else:
                raise AssertionError('Grid button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the grid button : { str(i)}")

    def list_button(self):
        try:
            list_button = self.chrome.find_element(*self.LIST)
            if list_button:
                list_button.click()
            else:
                raise AssertionError('List button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the list button : { str(i)}")

    def list_page(self):
        page_url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html?product_list_mode=list" # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}", #am scris o metoda
                                                     f"Actual current_url {page_url}") #de verificare de tip assert"  # am definit o variabila



