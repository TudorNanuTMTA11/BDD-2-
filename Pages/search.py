from base_page import Base_page





class Search(Base_page):
  def keyword_is_present_in_the_title_of_the_products_returned_by_the_search_web(self, product_name):
    product_list = self.chrome.find_elements(*self.PRODUCT_ITEM_LINK)
    product_name_in_product_title = True
    for i in range(len(product_list) -1):
        if product_name not in product_list[i].text:
          product_name_in_product_title = False
    assert product_name_in_product_title == True




