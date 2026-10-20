import pytest
from playwright.sync_api import Page, expect
from utils.visual_comparison import compare_screenshots


@pytest.mark.visual
def test_login_visual_regression(page: Page):
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("https://www.saucedemo.com/")

    expect(page.get_by_role("button", name="Login")).to_be_visible()

    compare_screenshots(page, "login_page")


@pytest.mark.visual
def test_inventory_visual_regression(logged_in_inventory):
    inventory = logged_in_inventory

    inventory.page.set_viewport_size({
        "width": 1280,
        "height": 720
    })

    expect(inventory.products_heading).to_be_visible()

    inventory.page.wait_for_function("""
        () => Array.from(document.images).every(
            img => img.complete && img.naturalWidth > 0
        )
    """)

    compare_screenshots(
        inventory.page,
        "inventory_page"
    )


@pytest.mark.visual
def test_cart_visual_regression(logged_in_inventory):
    inventory = logged_in_inventory

    inventory.page.set_viewport_size({
        "width": 1280,
        "height": 720
    })

    inventory.add_product_to_cart("Sauce Labs Backpack")

    cart = inventory.open_cart()

    expect(cart.product_name("Sauce Labs Backpack")).to_be_visible()

    cart.page.wait_for_function("""
                                () => Array.from(document.images).every(
                                    img => img.complete && img.naturalWidth > 0
                                )
                                """)

    compare_screenshots(cart.page, "cart_page")
