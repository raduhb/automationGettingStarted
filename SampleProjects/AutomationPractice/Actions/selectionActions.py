import traceback

from SampleProjects.AutomationPractice.Tests.TestSetup import TestSetup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SelectionActions(TestSetup):

    def find_and_clear(self, selection_type, locator):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((selection_type, locator))
            )
            self.driver.find_element(selection_type, locator).clear()
        except Exception as e:
            print(f"Test failed due to", {e})
            traceback.print_exc()
            raise e

    def find_and_send_keys(self, selection_type, locator, term):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((selection_type, locator))
            )
            self.driver.find_element(selection_type, locator).send_keys(term)
        except Exception as e:
            # print(f"Test failed due to", {e})
            traceback.print_exc()
            raise e

    def find_and_click(self, selection_type, locator):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((selection_type, locator))
            )
            self.driver.find_element(selection_type, locator).click()
        except Exception as e:
            # print(f"Test failed due to", {e})
            traceback.print_exc()
            raise e

    def find_and_hover(self, selection_type, locator):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((selection_type, locator))
            )
            element = self.driver.find_element(selection_type, locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except Exception as e:
            # print(f"Test failed due to", {e})
            traceback.print_exc()
            raise e

