from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class NovaPoshtaTracking:
    def __init__(self, driver_path):

        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.maximize_window()

    def get_status(self, tracking_number):

        self.driver.get("https://tracking.novaposhta.ua/#/uk")


        input_field = self.driver.find_element(By.XPATH, "//input[@placeholder='¬вед≥ть номер']")


        input_field.send_keys(tracking_number)
        input_field.send_keys(Keys.RETURN)

        time.sleep(5)


        try:
            status_element = self.driver.find_element(By.CSS_SELECTOR, "div.header__status-text")
            status = status_element.text
        except Exception as e:
            status = None
            print(f"Failed to get status. Error: {e}")


        self.driver.quit()

        return status


class TestNovaPoshtaTracking():

    def setUp(self):

        self.tracker = NovaPoshtaTracking(
            driver_path='/path/to/chromedriver')

    def test_tracking_status(self):
        tracking_number = "20400012345678"
        expected_status = "Parcel received"


        actual_status = self.tracker.get_status(tracking_number)


        self.assertEqual(actual_status, expected_status,
                         f"Expected status '{expected_status}', but got '{actual_status}'")

    def tearDown(self):
        pass


