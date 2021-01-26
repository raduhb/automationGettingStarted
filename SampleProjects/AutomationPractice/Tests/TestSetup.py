from selenium import webdriver
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class TestSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=sys.path[1]+"/drivers/chromedriver")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")