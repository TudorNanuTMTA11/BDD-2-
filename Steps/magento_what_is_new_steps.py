from behave import *



@when('I click on What is New option')
def step_impl(context):
    context.what_is_new.what_is_new_page()



@when('I click on action showcart icon')
def step_impl(context):
    context.what_is_new.action_showcart_wayfarer_messenger_bag_button()

@when('I click on Proceed to Checkout button')
def step_impl(context):
    context.what_is_new.proceed_to_checkout_button()

@then('I am redirected to the checkout page')
def step_impl(context):
    context.home_page.checkout_page()