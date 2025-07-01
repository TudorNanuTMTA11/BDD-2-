from behave import *



@given('I am on the Magento homepage and I want to purchase a product with a particular size and color I want')
def step_impl(context):
    context.circe_hooded_ice.circe_hooded_ice_page()

@when('I click on Women option')
def step_impl(context):
    context.circe_hooded_ice.women_option()

@when('I click on Tops option')
def step_impl(context):
    context.circe_hooded_ice.tops_option()

@when('I click on Hoodies & Sweatshirts option')
def step_impl(context):
    context.circe_hooded_ice.hoodies_sweatshirts_option()

@when('I select XS size on Circe Hooded Ice')
def step_impl(context):
    context.circe_hooded_ice.size_XS_circe_hooded_ice()

@when('I select Gray color on Circe Hooded Ice')
def step_impl(context):
    context.circe_hooded_ice.color_gray_circe_hooded_ice()