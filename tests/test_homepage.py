import allure
from playwright.sync_api import expect


@allure.title("Verify login page browser title")
@allure.description(
    "Verify that the SauceDemo login page has the browser title 'Swag Labs'."
)
@allure.severity(allure.severity_level.MINOR)
def test_homepage_title(page):
    with allure.step("Navigate to SauceDemo login page"):
        page.goto("https://www.saucedemo.com/")

    with allure.step("Verify browser title is Swag Labs"):
        expect(page).to_have_title("Swag Labs")
