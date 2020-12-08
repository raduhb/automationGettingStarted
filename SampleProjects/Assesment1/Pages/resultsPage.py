from SampleProjects.Assesment1.Locators.locators import Locators


class ResultsPage():

    def __init__(self, driver):
        self.driver = driver

        self.expected_first_result_url = Locators.expected_first_result_url

    def check_first_result(self):
        first_result = self.driver.find_element_by_id("rso").find_element_by_css_selector(":first-child div.rc a")
        first_result_url = first_result.get_attribute("href")
        assert first_result_url == self.expected_first_result_url

    def click_first_result(self):
        self.driver.find_element_by_id("rso").find_element_by_css_selector(":first-child div.rc a").click()

