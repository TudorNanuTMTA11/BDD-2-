

from base_page import Base_page

class Tops(Base_page):
    def tops_page(self):
        page_url = "https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html?product_list_dir=desc"  # am definit o variabila
        assert page_url == page_url, (f"An error occurred. Expected page_url {page_url}",  # am scris o metoda
                                      f"Actual current_url {page_url}")  # de verificare de tip assert"  # am definit o variabila

    def sort_products_desc_direction(self):
        self.chrome.find_elements(*self.SET_DESCENDING_DIRECTION)

    def sort_products_asc_direction(self):
        self.chrome.find_elements(*self.SET_ASCENDING_DIRECTION)

    def sort_products_position_product_name_price(self):
        self.chrome.find_elements(*self.SORTER)