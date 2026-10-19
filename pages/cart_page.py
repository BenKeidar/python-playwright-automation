from playwright.sync_api import Page
from pages.checkout_page import CheckoutPage


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")
        self.cart_items = page.locator(".cart_item")

    def product_name(self, name: str):
        return self.page.locator(
            ".cart_item"
        ).get_by_text(name, exact=True)

    def checkout(self) -> CheckoutPage:
        self.checkout_button.click()
        return CheckoutPage(self.page)