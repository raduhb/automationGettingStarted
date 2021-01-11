from SampleProjects.AutomationPractice.Tests.TestSetup import TestSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions(TestSetup):
    def find_by_id_and_enter_term(self, identifier, term):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.ID, identifier))
        )
        self.driver.find_element(By.ID, identifier).clear()
        self.driver.find_element(By.ID, identifier).send_keys(term)