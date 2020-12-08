from SampleProjects.Assesment1.Locators.locators import Locators


class SearchPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_class = Locators.search_textbox_class
        self.cookies_button_agree_id = Locators.cookies_button_agree_id

    def click_agree_cookies(self):
        self.driver.switch_to_frame(0)
        self.driver.find_element_by_xpath("//*[@id='" + self.cookies_button_agree_id + "']").click()
        self.driver.switch_to.default_content()

    def enter_search_term(self, search_term):
        self.driver.find_element_by_css_selector("input." + self.search_textbox_class).clear()
        self.driver.find_element_by_css_selector("input." + self.search_textbox_class).send_keys(search_term)
        self.driver.find_element_by_css_selector("input.gNO89b").click()

