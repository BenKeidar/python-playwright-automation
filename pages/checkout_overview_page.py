from playwright.sync_api import Page
from pages.checkout_complete_page import CheckoutCompletePage


class CheckoutOverviewPage:
    URL = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.locator("[data-test='finish']")

    def finish_order(self):
        self.finish_button.click()
        return CheckoutCompletePage(self.page)
