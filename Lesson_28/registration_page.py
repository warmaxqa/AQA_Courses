from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.confirm_password_input = (By.ID, "confirmPassword")
        self.registration_submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_registration_form(self, first_name, last_name, email, password):
        self.wait_for_element(self.first_name_input).send_keys(first_name)
        self.wait_for_element(self.last_name_input).send_keys(last_name)
        self.wait_for_element(self.email_input).send_keys(email)
        self.wait_for_element(self.password_input).send_keys(password)
        self.wait_for_element(self.confirm_password_input).send_keys(password)

    def submit_registration(self):
        self.wait_for_element(self.registration_submit_button).click()