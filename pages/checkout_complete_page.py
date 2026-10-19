from playwright.sync_api import Page


class CheckoutCompletePage:
    URL = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page: Page):
        self.page = page
        self.success_message = page.locator(
            "[data-test='complete-header']"
        )

    def order_confirmation(self):
        return self.success_message
