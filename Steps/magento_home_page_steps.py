from behave import *



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




