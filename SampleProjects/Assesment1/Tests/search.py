from selenium import webdriver
import time
import unittest
import sys
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SampleProjects.Assesment1.Pages.searchPage import SearchPage

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/radu.haidet/PycharmProjects/pythonProject/drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_perform_search(self):
        driver = self.driver

        driver.get("https://google.com")

        search = SearchPage(driver)
        # time.sleep(3)
        # WebDriverWait(driver, 50).until(EC.alert_is_present).accept()
        search.click_agree_cookies()
        search.enter_search_term('python')

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main()