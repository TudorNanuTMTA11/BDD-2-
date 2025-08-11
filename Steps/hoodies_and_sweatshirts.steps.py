from behave import *



@when('I click the list button')
def step_impl(context):
    context.hoodies_and_sweatshirts.list_button()

@then('the products are arranged in list')
def step_impl(context):
    context.hoodies_and_sweatshirts.list_page()

@when('I click the grid button')
def step_impl(context):
    context.hoodies_and_sweatshirts.grid_button()

@then('the products are arranged in grid')
def step_impl(context):
    context.circe_hooded_ice.circe_hooded_ice_page()

