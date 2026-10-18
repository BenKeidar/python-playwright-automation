from playwright.sync_api import Page
from pages.inventory_page import InventoryPage


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> InventoryPage:
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

        return InventoryPage(self.page)

    def error_message(self):
        return self.page.locator("[data-test='error']")
