from playwright.sync_api import expect
import pytest


#Login with a valid user and ensure it is logged in.
def test_valid_login(login_page):
    inventory_page = login_page.login("standard_user", "secret_sauce")

    expect(inventory_page.page).to_have_url(inventory_page.URL)
    expect(inventory_page.products_title()).to_be_visible()


#Login with a few invalid users and ensure they get an error.
@pytest.mark.parametrize(
    "username,password",
    [
        ("invalid_user", "wrong_password"),
        ("standard_user", "wrong_password"),
        ("invalid_user", "secret_sauce"),
    ],
)
def test_invalid_login(login_page, username, password):
    login_page.login(username, password)

    expect(login_page.error_message()).to_be_visible()
    expect(login_page.error_message()).to_contain_text(
        "Username and password do not match"
    )
