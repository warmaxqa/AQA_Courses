from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome()

try:

    driver.get("http://localhost:8000/dz.html")

    driver.switch_to.frame(driver.find_element(By.ID, "Frame1"))


    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")


    button1 = driver.find_element(By.XPATH, "//button[contains(text(), 'Check')]")
    button1.click()

    #
    alert = Alert(driver)
    time.sleep(3)
    assert "Verification success!" in alert.text, "The verification text did not match for frame 1!"
    alert.accept()


    driver.switch_to.default_content()


    driver.switch_to.frame(driver.find_element(By.ID, "Frame2"))


    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")


    button2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Check')]")
    button2.click()


    alert = Alert(driver)
    time.sleep(3)
    assert "Verification success!" in alert.text, "The verification text did not match for frame 2!"
    alert.accept()

finally:

    driver.quit()