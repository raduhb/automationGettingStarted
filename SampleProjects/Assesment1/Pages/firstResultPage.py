from SampleProjects.Assesment1.Locators.locators import Locators


class FirstResultPage():

    def __init__(self, driver):
        self.driver = driver

        self.expected_browser_url = Locators.expected_browser_url

    def check_first_result_url(self):
        browser_url = self.driver.current_url
        assert browser_url == self.expected_browser_url


