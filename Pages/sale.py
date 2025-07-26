import logging

from base_page import Base_page

class Sale(Base_page): #am construit o clasa
    def sale_image(self):
        try:
            sale_image = self.chrome.find_element(*self.SALE_IMAGE)
            if sale_image:
                sale_image.click()
            else:
                raise AssertionError('Sale image element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the sale image: { str(i)}")

    def sale_option(self):
        try:
            sale_option = self.chrome.find_element(*self.SALE_OPTION)
            if sale_option:
                sale_option.click()
            else:
                raise AssertionError('Sale option element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the sale option: {str(i)}")