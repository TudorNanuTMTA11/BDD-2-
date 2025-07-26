from behave import *

@given('I am on the Magento homepage and I want to access the content behind the images')
def step_impl(context):
    context.home_page.open_home_page()

@when('I click on Sale option')
def step_impl(context):
    context.sale.sale_option()

@when('I am redirected on sale page')
def step_impl(context):
    context.home_page.sale_page()


@then('I arrive on sales promotion page')
def step_impl(context):
    context.home_page.sale_promotions_page()
