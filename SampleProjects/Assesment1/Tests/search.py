from selenium import webdriver
import time
import unittest
import sys
import os

from SampleProjects.Assesment1.Pages.firstResultPage import FirstResultPage
from SampleProjects.Assesment1.Pages.resultsPage import ResultsPage
from SampleProjects.Assesment1.Pages.searchPage import SearchPage

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/radu.haidet/PycharmProjects/pythonProject/drivers"
                                                      "/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_perform_search(self):
        driver = self.driver

        driver.get("https://google.com")

        search = SearchPage(driver)
        search.click_agree_cookies()
        search.enter_search_term('selenium python')

        check = ResultsPage(driver)
        check.check_first_result()
        check.click_first_result()

        result = FirstResultPage(driver)
        result.check_first_result_url()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main()