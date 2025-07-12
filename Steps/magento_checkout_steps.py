from behave import *

@given('I am on the Magento homepage and I want to complete the purchase product process')
def step_impl(context):
    context.home_page.checkout_page()

@when('I introduce the company "{company}"')
def step_impl(context,company):
    context.checkout.the_company_is_inserted(company)

@when('I introduce the street address "{street_address}"')
def step_impl(context, street_address):
    context.checkout.the_street_address_is_inserted(street_address)

@when('I introduce the city "{city}"')
def step_impl(context, city):
    context.checkout.the_city_is_inserted(city)

@when('I introduce the state "{state}"')
def step_impl(context, state):
    context.checkout.the_state_is_selected(state)

@when('I introuce the postal code "{postal_code}"')
def step_impl(context, postal_code):
    context.checkout.the_postal_code_is_inserted(postal_code)

@when('I introduce the country "{country}"')
def step_impl(context, country):
    context.checkout.the_country_is_selected(country)

@when('I introduce the phone number "{phone_number}"')
def step_impl(context, phone_number):
    context.checkout.the_postal_code_is_inserted(phone_number)

@when('I select the price')
def step_impl(context):
    context.checkout.the_price_is_selected()

@when('I click Next button')
def step_impl(context):
    context.checkout.next_button()

@when('I click Place Order button')
def step_impl(context):
    context.checkout.place_order_button()

@when('I click Continue Shopping button')
def step_impl(context):
    context.checkout.continue_shopping_button()

@then('I am redirected to the home page')
def step_impl(context):
    context.home_page.open_home_page()

@then('It appears the message "This is a required field"')
def step_impl(context):
    context.checkout.this_is_a_required_field()

@then('It appears the message "The shipping method is missing. Select the shipping method and try again."')
def step_impl(context):
    context.checkout.error_validation_message()

@when('I am on checkout page')
def step_impl(context):
    context.home_page.checkout_page()

@when('I click the sign in option')
def step_impl(context):
    context.checkout.sign_in_option_2()

@when('I insert the email "{email}"')
def step_impl(context,email):
    context.checkout.the_email_is_inserted_2(email)

@when('I insert the password "{password}"')
def step_impl(context,password):
    context.checkout.the_password_is_inserted_2(password)

@when('I click the sign in button')
def step_impl(context):
    context.checkout.sign_in_button_2()

@when('I see the shipping address saved')
def step_impl(context):
    context.checkout.shipping_address_item()
