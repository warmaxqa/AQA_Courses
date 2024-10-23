from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.registration_button = (By.CSS_SELECTOR, "a[href='#signup']")  # ������ ���������
        self.login_button = (By.CSS_SELECTOR, "a[href='#login']")  # ������ �����
        self.profile_button = (By.CSS_SELECTOR, ".profile-btn")  # ������ ������� ���� �����������

    def click_registration_button(self):
        self.wait_for_element(self.registration_button).click()