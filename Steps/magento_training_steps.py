from behave import *
@when('I click on Training option')
def step_impl(context):
    context.training.training_option()

@when('I am redirected on training page')
def step_impl(context):
    context.home_page.training_page()

@when('I click on a particular image')
def step_impl(context):
    context.training.training_image()

@then('I arrive on erin recommends page')
def step_impl(context):
    context.home_page.erin_recommends()

@when('I click on Video Download option')
def step_impl(context):
    context.training.video_download_option()

@when('I am redirected on video download page')
def step_impl(context):
    context.home_page.video_download_page()

@then('I see a message info')
def step_impl(context):
    context.training.video_download()

