
from playwright.sync_api import Page


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page

        self.products_heading = page.get_by_text(
            "Products", exact=True
        )

        self.cart_badge = page.locator(
            "[data-test='shopping-cart-badge']"
        )

    def products_title(self):
        return self.products_heading

    def get_product(self, product_name: str):
        return self.page.locator(".inventory_item").filter(
            has=self.page.get_by_text(product_name, exact=True)
        )

    def add_product_to_cart(self, product_name: str):
        product = self.get_product(product_name)

        product.get_by_role(
            "button", name="Add to cart", exact=True
        ).click()

    def remove_button(self, product_name: str):
        product = self.get_product(product_name)

        return product.get_by_role(
            "button", name="Remove", exact=True
        )

    def cart_item_count(self):
        return self.cart_badge