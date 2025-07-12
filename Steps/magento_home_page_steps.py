from behave import *

@given('I am on the Magento homepage and I want to initiate the searching products process')
def step_impl(context):
    context.home_page.open_home_page()

@when('I type "Wayfarer Messenger Bag" in the search tab')
def step_impl(context):
    context.home_page.search_entire_here()

@when('I click on the search tab to generate the results')
def step_impl(context):
    context.home_page.wayfarer_messenger_bag_search()

@when('I am redirected to the catalog page')
def step_impl(context):
    context.home_page.catalog_page()

@then('I see the product shown on the page')
def step_impl(context):
    context.home_page.wayfarer_messenger_bag_product()

@then('I see the word "Wayfarer" in the title of the products returned by the search web')
def step_impl(context):
    context.base_page.wayfarer_keyword_is_present_in_the_title_of_the_products_returned_by_the_search_web()



