import time
import unittest
import sys
import os

from SampleProjects.AutomationPractice.Pages.homePage import HomePage
from SampleProjects.AutomationPractice.Tests.TestSetup import TestSetup

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class SearchTest(TestSetup):

    def test_perform_search(self):
        driver = self.driver

        driver.get("http://automationpractice.com")

        home = HomePage(driver)
        home.enter_search_term('test')

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()