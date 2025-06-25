from browser import Browser
from base_page import Base_page
from Pages.create_account import Create_account
from Pages.home_page import Home_page
from Pages.sign_in_page import Sign_in_page

def before_all(context):
    context.browser = Browser()
    context.browser.maximise_windows()
    context.base_page = Base_page()
    context.create_account = Create_account()
    context.home_page = Home_page()
    context.sign_in_page = Sign_in_page()

def after_all(context):
    context.browser.close_browser()