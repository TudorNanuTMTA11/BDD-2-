from browser import Browser
from base_page import Base_page
from Pages.create_account import Create_account
from Pages.home_page import Home_page
from Pages.sign_in_page import Sign_in_page
from Pages.what_is_new import What_is_new
from Pages.checkout import Checkout
from Pages.circe_hooded_ice import Circe_Hooded_Ice
from Pages.tops import Tops
from Pages.sign_in_page import Search

def before_all(context):
    context.browser = Browser()
    context.browser.maximise_windows()
    context.base_page = Base_page()
    context.create_account = Create_account()
    context.home_page = Home_page()
    context.sign_in_page = Sign_in_page()
    context.what_is_new = What_is_new()
    context.checkout = Checkout()
    context.circe_hooded_ice = Circe_Hooded_Ice()
    context.tops = Tops()
    context.search = Search()

def after_all(context):
    context.browser.close_browser()