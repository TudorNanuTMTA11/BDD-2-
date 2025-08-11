from behave import *



@when('I click on Price option')
def step_impl(context):
    context.tops.sort_products_position_product_name_price()

@when('I click on descending arrow')
def step_impl(context):
    context.tops.sort_products_desc_direction()

@when('I click on ascending arrow')
def step_impl(context):
    context.tops.sort_products_asc_direction()

@then('I have the products arranged as I wanted')
def step_impl(context):
    context.tops.tops_page()