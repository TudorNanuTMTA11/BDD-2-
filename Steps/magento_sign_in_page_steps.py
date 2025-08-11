from behave import *



@when('I click "Sign in" option')
def step_impl(context):
    context.home_page.sign_in_page()

@when('I click the "Sign in" button')
def step_impl(context):
    context.sign_in_page.sign_in_button()

@then('I receive the error "This is a required field" for not inserting credentials')
def step_impl(context):
    context.sign_in_page.forget_inserting_email_error()

@then('I receive the error: "This is a required field" for not inserting password')
def step_impl(context):
    context.sign_in_page.forget_inserting_password_error()

@then('I receive "{error_type}" error "{error_message}"')
def step_impl(context, error_type, error_message):
    if error_type == "invalid_password":
        context.sign_in_page.error_message_invalid_password_is_displayed(error_message)
@when('I click the button "Forgot your Password?"')
def step_impl(context):
    context.sign_in_page.forget_password_button()

@when('I click the button "Reset My Password"')
def step_impl(context):
    context.sign_in_page.reset_my_password_button()

@then('I receive a confirmation message')
def step_impl(context):
    context.sign_in_page.confirmation_message()

@when('I enter password "{password}"')
def step_impl(context,password):
    context.base_page.the_password_is_inserted(password)

@when('I click sign in button')
def step_impl(context):
    context.sign_in_page.sign_in_button()

@when('I enter email "{email}"')
def step_impl(context, email):
    context.base_page.the_email_is_inserted(email)


