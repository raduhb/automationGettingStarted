import time
import unittest
import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
# import export

# export PYTHONPATH="${PYTHONPATH}:~/.PycharmProjects/pythonProject/SampleProjects/AutomationPractice/"
# sys.path.append("~/.PycharmProjects/pythonProject/SampleProjects/AutomationPractice/")
from SampleProjects.AutomationPractice.Pages.homePage import HomePage
from SampleProjects.AutomationPractice.Pages.signInPage import SignInPage
from SampleProjects.AutomationPractice.Tests.TestSetup import TestSetup

os.environ["PYTHONPATH"].split(os.pathsep)

class SearchTest(TestSetup):

    def test_perform_search_by_clicking_search_button(self):
        driver = self.driver

        driver.get("http://automationpractice.com")

        home = HomePage(driver)
        home.enter_search_term_and_click_search_button('test')

        time.sleep(5)

    def test_perform_search_by_pressing_enter_key(self):
        driver = self.driver

        driver.get("http://automationpractice.com")

        home = HomePage(driver)
        home.enter_search_term_and_press_enter_key('test')

        time.sleep(5)

    def test_load_sign_in_page_when_clicking_button(self):
        driver = self.driver

        driver.get("http://automationpractice.com")

        home = HomePage(driver)
        home.click_sign_in_button()

        sign_in = SignInPage(driver)
        sign_in.check_sign_in_url()

        time.sleep(5)

    def test_click_check_out_with_no_products(self):
        driver = self.driver

        driver.get("http://automationpractice.com")

        home = HomePage(driver)
        home.hover_cart_dropdown_and_click_check_out_button()
        home.check_cart_dropdown_is_visible()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()