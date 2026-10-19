from playwright.sync_api import Page

from data.sort_options import SortOption
from pages.cart_page import CartPage


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
        self.sort_dropdown = page.locator(
            "[data-test='product-sort-container']"
        )

        self.product_prices = page.locator(
            "[data-test='inventory-item-price']"
        )

        self.product_names = page.locator(
            "[data-test='inventory-item-name']"
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

    def remove_product_from_cart(self, product_name: str):
        self.remove_button(product_name).click()

    def open_cart(self) -> CartPage:
        self.page.locator("[data-test='shopping-cart-link']").click()
        return CartPage(self.page)

    def sort_products(self, sort_option: SortOption):
        self.sort_dropdown.select_option(sort_option.value)

    def get_product_prices(self) -> list[float]:
        prices_text = self.product_prices.all_text_contents()

        return [
            float(price.replace("$", ""))
            for price in prices_text
        ]

    def get_product_names(self) -> list[str]:
        return self.product_names.all_text_contents()
