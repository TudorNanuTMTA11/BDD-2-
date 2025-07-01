from behave import *

@given('I am on the Magento homepage and I want to initiate the purchase product process')
def step_impl(context):
    context.home_page.open_home_page()

@when('I click on What is New option')
def step_impl(context):
    context.what_is_new.what_is_new_page()

@when('I click Add to Cart button on Wayfarer Messenger Bag product')
def step_impl(context):
    context.what_is_new.add_to_cart_wayfarer_messenger_bag_button()

@when('I click on action showcart icon')
def step_impl(context):
    context.what_is_new.action_showcart_wayfarer_messenger_bag_button()

@when('I click on Proceed to Checkout button')
def step_impl(context):
    context.what_is_new.proceed_to_checkout_button()

@then('I am redirected to the checkout page')
def step_impl(context):
    context.home_page.checkout_page()