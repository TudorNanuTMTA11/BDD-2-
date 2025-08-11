from behave import *



@then('I see the word {product_name} in the title of the products returned by the search web')
def step_impl(context,product_name):
    context.search.keyword_is_present_in_the_title_of_the_products_returned_by_the_search_web(product_name)

