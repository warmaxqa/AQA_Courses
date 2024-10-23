import pytest

@pytest.mark.usefixtures("home_page", "registration_page")
def test_user_registration(home_page, registration_page):

    home_page.click_registration_button()


    registration_page.fill_registration_form(
        first_name="Test",
        last_name="User",
        email="testuser@example.com",
        password="TestPassword123"

    registration_page.submit_registration()

    assert home_page.wait_for_element(home_page.profile_button), "User not registered"