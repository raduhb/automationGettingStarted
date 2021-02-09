from utils.SeleniumActions import SeleniumActions


class CheckoutPage(SeleniumActions):

    def __init__(self, driver):
        self.driver = driver

        self.checkout_page_url = "http://automationpractice.com/index.php?controller=order"

    def check_checkout_page_url(self):
        browser_url = self.driver.current_url

        assert browser_url == self.driver.current_url
