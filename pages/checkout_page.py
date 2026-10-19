from playwright.sync_api import Page
from pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage:
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page):
        self.page = page

        self.first_name_field = page.locator("[data-test='firstName']")
        self.last_name_field = page.locator("[data-test='lastName']")
        self.postal_code_field = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.error = page.locator("[data-test='error']")

    def first_name_input(self):
        return self.first_name_field

    def last_name_input(self):
        return self.last_name_field

    def postal_code_input(self):
        return self.postal_code_field

    def fill_customer_information(
            self,
            first_name: str,
            last_name: str,
            postal_code: str
    ):
        self.fill_customer_fields(first_name, last_name, postal_code)
        self.continue_button.click()

        return CheckoutOverviewPage(self.page)

    def fill_customer_fields(
            self,
            first_name: str,
            last_name: str,
            postal_code: str
    ):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)

    def submit_customer_information(self):
        self.continue_button.click()

    def error_message(self):
        return self.error