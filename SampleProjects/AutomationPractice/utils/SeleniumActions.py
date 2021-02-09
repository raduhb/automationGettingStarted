import traceback

from SampleProjects.AutomationPractice.utils.BaseSetup import BaseSetup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


TIMEOUT = 2


class SeleniumActions(BaseSetup):

    def get_url(self, url):
        page = self.driver.get(url)
        return page

    def get_element(self, locator):
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def find_and_clear(self, locator):
        try:
            WebDriverWait(self.driver, TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
            self.driver.find_element(locator).clear()
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

    def click_element(self, locator):
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, search_term):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(search_term)

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

    def find_element(self, selection_type, locator):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((selection_type, locator))
            )
            self.driver.find_element(selection_type, locator)
        except Exception as e:
            # print(f"Test failed due to", {e})
            traceback.print_exc()
            raise e

