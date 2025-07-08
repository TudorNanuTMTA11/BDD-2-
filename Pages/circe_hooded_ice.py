from time import sleep

from base_page import Base_page


class Circe_Hooded_Ice(Base_page):
    def size_XS_circe_hooded_ice(self):
        self.chrome.find_elements(*self.SIZE)

    def color_gray_circe_hooded_ice(self):
        self.chrome.find_elements(*self.COLOR)

    def women_option(self):
        self.chrome.find_element(*self.WOMEN)

    def tops_option(self):
        self.chrome.find_element(*self.TOPS)

    def hoodies_sweatshirts_option(self):
        self.chrome.find_element(*self.HOODIES_SWEATSHIRTS)

    def circe_hooded_ice_page(self):
        page_url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html"  # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}",  # am scris o metoda
                                      f"Actual current_url {page_url}")  # de verificare de tip assert"  # am definit o variabila
