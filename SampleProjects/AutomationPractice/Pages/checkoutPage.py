from SampleProjects.AutomationPractice.Actions.selectionActions import SelectionActions
from SampleProjects.AutomationPractice.Locators.checkoutPageLocators import CheckoutPageLocators


class CheckoutPage(SelectionActions):

    def __init__(self, driver):
        self.driver = driver

        self.checkout_page_url = CheckoutPageLocators.checkout_page_url

    def check_checkout_page_url(self):
        browser_url = self.driver.current_url

        assert browser_url == self.driver.current_url
