from utils.SeleniumActions import SeleniumActions


class SignInPage(SeleniumActions):

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_page_url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"

    def check_sign_in_url(self):
        browser_url = self.driver.current_url
        assert browser_url == self.sign_in_page_url
