from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from SampleProjects.Assesment1.Locators.locators import Locators


class SearchPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_title = Locators.search_textbox_title
        self.cookies_agree_link_text = Locators.cookies_agree_link_text

    def click_agree_cookies(self):
        # self.driver.switch_to.alert
        element = self.driver.switch_to_active_element()
        print(f'{element.text}')
        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='introAgreeButton']"))).click()
        WebDriverWait(self.driver, 50).until(EC.alert_is_present).accept()
        self.driver.find_element_by_link_text(self.cookies_agree_link_text).click()

    def enter_search_term(self, search_term):
        self.driver.find_element_by_xpath("//*[@title=" + self.search_textbox_title + "]").clear()
        self.driver.find_element_by_xpath("//*[@title=" + self.search_textbox_title + "]").send_keys(search_term)

