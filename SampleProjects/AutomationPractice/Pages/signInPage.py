from SampleProjects.AutomationPractice.Actions.selectionActions import SelectionActions
from SampleProjects.AutomationPractice.Locators.signInPageLocators import SignInPageLocators


class SignInPage(SelectionActions):

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_page_url = SignInPageLocators.sign_in_page_url

    def check_sign_in_url(self):
        browser_url = self.driver.current_url
        assert browser_url == self.sign_in_page_url
