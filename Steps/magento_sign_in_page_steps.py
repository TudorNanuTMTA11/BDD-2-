from behave import *

@given('I am on the Magento homepage and I want to initiate the sign in process')
def step_impl(context):
    context.home_page.open_home_page()

@when('I click "Sign in" option')
def step_impl(context):
    context.home_page.sign_in_page()

@when('I click the "Sign in" button')
def step_impl(context):
    context.sign_in_page.sign_in_button()

@then('I receive the message "This is a required field"')
def step_impl(context,email):
    context.sign_in_page.forget_inserting_email_error(email)


@when('I click the button "Forgot your Password?"')
def step_impl(context):
    context.sign_in_page.forget_password_button()

@when('I click the button "Reset My Password"')
def step_impl(context):
    context.sign_in_page.reset_my_password_button()

@then('I receive a confirmation message')
def step_impl(context):
    context.sign_in_page.confirmation_message()



