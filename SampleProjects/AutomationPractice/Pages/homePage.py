from utils.SeleniumActions import SeleniumActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage(SeleniumActions):

    def __init__(self, driver, page_url):
        
        self.driver = driver
        self.driver.get(page_url)

    search_textbox_id = (By.ID, "search_query_top")
    search_button_name = (By.NAME, "submit_search")
    sign_in_button_class = "login"
    cart_dropdown_class = "shopping_cart"
    cart_dropdown_content_class = "cart_block"
    check_out_button_id = "button_order_cart"
    cart_button_xpath_href = "//a[@href = 'http://automationpractice.com/index.php?controller=order']"

    def enter_search_term_and_click_search_button(self, search_term):
        self.enter_text(self.search_textbox_id, search_term)
        self.click_element(self.search_button_name)

    # def enter_search_term_and_press_enter_key(self, search_term):
    #     SeleniumActions.find_and_clear(self, By.ID, self.search_textbox_id)
    #     SeleniumActions.find_and_send_keys(self, By.ID, self.search_textbox_id, search_term)
    #     SeleniumActions.find_and_send_keys(self, By.ID, self.search_textbox_id, Keys.RETURN)
    #
    # def click_sign_in_button(self):
    #     SeleniumActions.find_and_click(self, By.CLASS_NAME, self.sign_in_button_class)
    #
    # def hover_cart_dropdown_and_click_check_out_button(self):
    #     SeleniumActions.find_and_hover(self, By.CLASS_NAME, self.cart_dropdown_class)
    #
    # def check_cart_dropdown_is_visible(self):
    #     element = self.driver.find_element_by_class_name(self.cart_dropdown_content_class)
    #     # element = SeleniumActions.find_element(self, By.CLASS_NAME, self.cart_dropdown_content_class)
    #
    #     if element.is_displayed():
    #         print("Element found")
    #     else:
    #         print("Element not found")
    #
    # def click_shopping_cart_button(self):
    #     SeleniumActions.find_and_click(self, By.XPATH, self.cart_button_xpath_href)