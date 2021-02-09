from selenium import webdriver
import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class BaseSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=sys.path[0]+"/drivers/chromedriver")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed")
