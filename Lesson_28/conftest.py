import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)