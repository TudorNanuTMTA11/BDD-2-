from behave import *

@given('I am on the Magento homepage and I want to initiate the searching products process')
def step_impl(context):
    context.home_page.open_home_page()

@when('I type "Wayfarer Messenger Bag" in the search tab')
def step_impl(context):
    context.home_page.search_entire_here()



@when('I am redirected to the catalog page')
def step_impl(context):
    context.home_page.catalog_page()

@then('I see the product shown on the page')
def step_impl(context):
    context.home_page.wayfarer_messenger_bag_product()