from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from SampleProjects.Assesment1.Locators.locators import Locators


class SearchPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_title = Locators.search_textbox_title
        self.cookies_agree_link_text = Locators.cookies_agree_link_text
        self.iframe_src = "https://consent.google.com?hl=en&origin=https://www.google.com&continue=https://www.google.com/&if=1&m=0&pc=s&wp=-1&gl=RO"

    def click_agree_cookies(self):
        # self.driver.switch_to.alert
        # element = self.driver.switch_to_active_element()
        # time.sleep(3)
        # print(f'{element.text}')
        size = self.driver.find_elements_by_tag_name("iframe")
        print(f'{len(size)}')

        # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='introAgreeButton']"))).click()
        # new_frame = WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@src='"+self.iframe_src+"']")))
        # print(f'{new_frame}')
        self.driver.switch_to_frame(0)
        # self.driver.find_element_by_id("yDmH0d").accept()
        # WebDriverWait(self.driver, 50).until(EC.alert_is_present()).accept()
        # WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "cui-csn-data"))).accept()
        self.driver.find_element_by_xpath("//*[@id='introAgreeButton']").click()

    def enter_search_term(self, search_term):
        self.driver.find_element_by_xpath("//*[@title=" + self.search_textbox_title + "]").clear()
        self.driver.find_element_by_xpath("//*[@title=" + self.search_textbox_title + "]").send_keys(search_term)

