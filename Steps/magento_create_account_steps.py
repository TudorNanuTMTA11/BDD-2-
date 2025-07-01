from behave import *

@given('I am on the Magento homepage and I want to initiate the create account process')
def step_impl(context):
    context.home_page.open_home_page()

@when('I click "Consent" on incognito window')
def step_impl(context):
    context.home_page.click_consent_button()

@when('I click "Create an Account" option')
def step_impl(context):
    context.home_page.create_account_page()

@when('I introduce the first name "{first_name}"')
def step_impl(context,first_name):
    context.create_account.the_first_name_is_inserted(first_name)

@when('I introduce the last name "{last_name}"')
def step_impl(context,last_name):
    context.create_account.the_last_name_is_inserted(last_name)

@when('I introduce the email "{email}"')
def step_impl(context, email):
    context.create_account.the_email_is_inserted(email)

@when('I introduce the password "{password}"')
def step_impl(context, password):
    context.create_account.the_password_is_inserted(password)

@when('I confirm the password "{password}"')
def step_impl(context, password):
    context.create_account.the_password_is_inserted(password)

@when('I click the "Create an Account" button')
def step_impl(context):
    context.create_account.click_create_an_account_button()

@then('I am redirected to "My Account" page')
def step_impl(context):
    context.home_page.account_page()


