import time
import unittest
import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
import export

# export PYTHONPATH="${PYTHONPATH}:~/.PycharmProjects/pythonProject/SampleProjects/AutomationPractice/"
sys.path.append("~/.PycharmProjects/pythonProject/SampleProjects/AutomationPractice/")
from SampleProjects.AutomationPractice.Pages.homePage import HomePage
from SampleProjects.AutomationPractice.Tests.TestSetup import TestSetup



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


if __name__ == '__main__':
    unittest.main()