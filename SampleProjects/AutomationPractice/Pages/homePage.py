from SampleProjects.AutomationPractice.Actions.selectionActions import SelectionActions
from SampleProjects.AutomationPractice.Locators.homePageLocators import HomePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage(SelectionActions):

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_id = HomePageLocators.search_textbox_id
        self.search_button_name = HomePageLocators.search_button_name
        self.sign_in_button_class = HomePageLocators.sign_in_button_class
        self.cart_dropdown_class = HomePageLocators.cart_dropdown_class
        self.check_out_button_id = HomePageLocators.check_out_button_id
        self.cart_dropdown_content_class = HomePageLocators.cart_dropdown_content_class

    def enter_search_term_and_click_search_button(self, search_term):
        SelectionActions.find_and_clear(self, By.ID, self.search_textbox_id)
        SelectionActions.find_and_send_keys(self, By.ID, self.search_textbox_id, search_term)
        SelectionActions.find_and_click(self, By.NAME, self.search_button_name)

    def enter_search_term_and_press_enter_key(self, search_term):
        SelectionActions.find_and_clear(self, By.ID, self.search_textbox_id)
        SelectionActions.find_and_send_keys(self, By.ID, self.search_textbox_id, search_term)
        SelectionActions.find_and_send_keys(self, By.ID, self.search_textbox_id, Keys.RETURN)

    def click_sign_in_button(self):
        SelectionActions.find_and_click(self, By.CLASS_NAME, self.sign_in_button_class)

    def hover_cart_dropdown_and_click_check_out_button(self):
        # SelectionActions.find_and_click(self, By.CSS_SELECTOR, 'http://automationpractice.com/index.php?controller=cart&amp;add=1&amp;id_product=3&amp;token=e817bb0705dd58da8db074c69f729fd8')
        # SelectionActions.find_and_click(self, By.CLASS_NAME, 'ajax_add_to_cart_button')
        # SelectionActions.find_and_click(self, By.CLASS_NAME, 'cross')
        SelectionActions.find_and_hover(self, By.CLASS_NAME, self.cart_dropdown_class)
        # SelectionActions.find_and_click(self, By.NAME, self.check_out_button_id)

    def check_cart_dropdown_is_visible(self):
        element = self.driver.find_element_by_class_name(self.cart_dropdown_content_class)
        if element.is_displayed():
            print("Element found")
        else:
            print("Element not found")