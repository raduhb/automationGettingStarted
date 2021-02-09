import time

from Pages.homePage import HomePage
from Pages.signInPage import SignInPage
from Pages.checkoutPage import CheckoutPage
from utils.BaseSetup import BaseSetup
import unittest


# os.environ["PYTHONPATH"].split(os.pathsep)

class TestSearchHomePage(BaseSetup):

    page_url = "http://automationpractice.com"

    # Test user is able to perform a search by clicking the search button
    def test_perform_search_by_clicking_search_button(self):
        home = HomePage(self.driver, self.page_url)
        home.enter_search_term_and_click_search_button('test')

        time.sleep(5)

    # # Test user is able to perform a search by pressing 'enter' key
    # def test_perform_search_by_pressing_enter_key(self):
    #     driver = self.driver
    #
    #     driver.get("http://automationpractice.com")
    #
    #     home = HomePage(driver)
    #     home.enter_search_term_and_press_enter_key('test')
    #
    #     time.sleep(5)
    #
    # # Test User is redirected to 'Sign in' page after clicking button
    # def test_load_sign_in_page_when_clicking_button(self):
    #     driver = self.driver
    #
    #     driver.get("http://automationpractice.com")
    #
    #     home = HomePage(driver)
    #     home.click_sign_in_button()
    #
    #     sign_in = SignInPage(driver)
    #     sign_in.check_sign_in_url()
    #
    #     time.sleep(5)
    #
    # # Test cart dropdown is visible when hovering with no products
    # # TODO: should change naming or test since the dropdown is NOT visible ?
    # def test_click_check_out_with_no_products(self):
    #     driver = self.driver
    #
    #     driver.get("http://automationpractice.com")
    #
    #     home = HomePage(driver)
    #     home.hover_cart_dropdown_and_click_check_out_button()
    #     home.check_cart_dropdown_is_visible()
    #
    #     time.sleep(5)
    #
    # # Test User is redirected to 'Checkout' page after clicking button
    # def test_load_checkout_page_when_clicking_button(self):
    #     driver = self.driver
    #
    #     driver.get("http://automationpractice.com")
    #
    #     home = HomePage(driver)
    #     home.click_shopping_cart_button()
    #
    #     checkout = CheckoutPage(driver)
    #     checkout.check_checkout_page_url()
    #
    #     time.sleep(5)
