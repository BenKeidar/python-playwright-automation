import pytest
from playwright.sync_api import expect


#Login with a valid user, add an item to the cart and ensure its was added correctly.
@pytest.mark.parametrize(
    "product_name",
    [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
    ],
)
def test_add_product_to_cart(login_page, product_name):
    inventory_page = login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    expect(inventory_page.remove_button("Sauce Labs Backpack")).to_be_visible()

    expect(
        inventory_page.cart_item_count()
    ).to_have_text("1")
