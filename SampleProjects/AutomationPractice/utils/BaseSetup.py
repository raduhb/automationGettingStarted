from selenium import webdriver
import unittest
import sys
import os


class BaseSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed")