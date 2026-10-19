import allure
from data import test_data
from playwright.sync_api import expect
import pytest


@allure.title("Verify successful login works")
@allure.description(
    "Login with username: standard_user & password: secret_sauce,"
    " and ensure it is logged in"
)
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(login_page):
    with allure.step("Log in"):
        inventory_page = login_page.login(test_data.VALID_USERNAME, test_data.VALID_PASSWORD)

    with allure.step("Verify navigation to Inventory page"):
        expect(inventory_page.page).to_have_url(inventory_page.URL)

    with allure.step("Verify Products heading is visible"):
        expect(inventory_page.products_title()).to_be_visible()


#Login with a few invalid users and ensure they get an error.
@pytest.mark.parametrize(
    "username,password",
    [
        (test_data.INVALID_USERNAME, test_data.INVALID_PASSWORD),
        (test_data.VALID_USERNAME, test_data.INVALID_PASSWORD),
        (test_data.INVALID_USERNAME, test_data.VALID_PASSWORD),
    ],
)
@allure.title("Verify login fails for username: {username}")
@allure.description(
    "Verify that login with invalid credentials is rejected "
    "and the appropriate error message is displayed."
)
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_login(login_page, username, password):
    with allure.step("Log in"):
        login_page.login(username, password)

    with allure.step("Ensure error message appears"):
        expect(login_page.error_message()).to_be_visible()
    with allure.step("Ensure error message is: Username and password do not match"):
        expect(login_page.error_message()).to_contain_text(
        "Username and password do not match"
    )


@allure.title("Verify locked out user cannot log in")
@allure.severity(allure.severity_level.CRITICAL)
def test_locked_out_user_cannot_login(login_page):
    with allure.step("Attempt login with locked out user"):
        login_page.login(
            test_data.LOCKED_OUT_USERNAME,
            test_data.VALID_PASSWORD
        )

    with allure.step("Verify locked out error message"):
        expect(login_page.error_message()).to_contain_text(
            "Sorry, this user has been locked out."
        )


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("", test_data.VALID_PASSWORD, "Username is required"),
        (test_data.VALID_USERNAME, "", "Password is required"),
        ("", "", "Username is required"),
    ],
    ids=["empty-username", "empty-password", "both-fields-empty"]
)
@allure.title("Verify required login fields: {param_id}")
@allure.severity(allure.severity_level.NORMAL)
def test_login_required_fields(
        login_page,
        username,
        password,
        expected_error
):
    with allure.step("Attempt login with missing field"):
        login_page.login(username, password)

    with allure.step("Verify required field error"):
        expect(login_page.error_message()).to_contain_text(
            expected_error
        )
