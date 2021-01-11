import traceback

from selenium.common.exceptions import TimeoutException

from SampleProjects.AutomationPractice.Actions.actions import Actions
from SampleProjects.AutomationPractice.Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(Actions):

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_id = Locators.search_textbox_id
        self.search_button_name = Locators.search_button_name

    def enter_search_term(self, search_term):
        try:
            # WebDriverWait(self.driver, 2).until(
            #     EC.visibility_of_element_located((By.ID, self.search_textbox_id))
            # )
            # self.driver.find_element(By.ID, self.search_textbox_id).clear()
            # self.driver.find_element(By.ID, self.search_textbox_id).send_keys(search_term)

            Actions.find_by_id_and_enter_term(self, self.search_textbox_id, search_term)

            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.NAME, self.search_button_name))
            )
            self.driver.find_element(By.NAME, self.search_button_name).click()
        except Exception as e:
            # print(f"Test failed due to", {e})
            traceback.print_exc()
            raise e