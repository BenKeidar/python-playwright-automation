import pytest
import allure
from data import test_data
from playwright.sync_api import expect

from data.sort_options import SortOption


@pytest.mark.parametrize(
    "product_name",
    [
        test_data.BACKPACK,
        test_data.BIKE_LIGHT,
        test_data.BOLT_TSHIRT,
    ],
)
@allure.title("Verify adding {product_name} to cart")
@allure.description(
    "Verify that a logged-in user can add a product to the shopping cart, "
    "that the Remove button becomes visible, "
    "and that the cart badge displays 1 item."
)
@allure.severity(allure.severity_level.NORMAL)
def test_add_product_to_cart(logged_in_inventory, product_name):

    inventory_page = logged_in_inventory

    with allure.step(f"Add {product_name} to cart"):
        inventory_page.add_product_to_cart(product_name)

    with allure.step(f"Verify Remove button is visible for {product_name}"):
        expect(
            inventory_page.remove_button(product_name)
        ).to_be_visible()

    with allure.step("Verify cart badge shows 1 item"):
        expect(
            inventory_page.cart_item_count()
        ).to_have_text("1")


@allure.title("Verify adding two products to cart")
@allure.description(
    "Verify that adding two different products "
    "updates the shopping cart badge to 2."
)
@allure.severity(allure.severity_level.NORMAL)
def test_add_two_products_to_cart(logged_in_inventory):

    inventory_page = logged_in_inventory

    with allure.step("Add Backpack to cart"):
        inventory_page.add_product_to_cart(
            test_data.BACKPACK
        )

    with allure.step("Add Bike Light to cart"):
        inventory_page.add_product_to_cart(
            test_data.BIKE_LIGHT
        )

    with allure.step("Verify both products have Remove buttons"):
        expect(
            inventory_page.remove_button(test_data.BACKPACK)
        ).to_be_visible()

        expect(
            inventory_page.remove_button(test_data.BIKE_LIGHT)
        ).to_be_visible()

    with allure.step("Verify cart contains 2 items"):
        expect(
            inventory_page.cart_item_count()
        ).to_have_text("2")


@allure.title("Verify removing a product updates cart badge")
@allure.description(
    "Verify that removing one of two products "
    "updates the shopping cart badge from 2 to 1."
)
@allure.severity(allure.severity_level.NORMAL)
def test_remove_product_from_cart(logged_in_inventory):

    inventory_page = logged_in_inventory

    with allure.step("Add two products to cart"):
        inventory_page.add_product_to_cart(test_data.BACKPACK)
        inventory_page.add_product_to_cart(test_data.BIKE_LIGHT)

    with allure.step("Verify cart badge shows 2 items"):
        expect(inventory_page.cart_item_count()).to_have_text("2")

    with allure.step("Remove Backpack from cart"):
        inventory_page.remove_product_from_cart(test_data.BACKPACK)

    with allure.step("Verify cart badge shows 1 item"):
        expect(inventory_page.cart_item_count()).to_have_text("1")

    with allure.step("Verify Bike Light remains in cart"):
        expect(
            inventory_page.remove_button(test_data.BIKE_LIGHT)
        ).to_be_visible()



@allure.title("Verify products appear in shopping cart")
@allure.description(
    "Verify that two products added from Inventory "
    "are displayed in the shopping cart."
)
@allure.severity(allure.severity_level.NORMAL)
def test_products_appear_in_cart(logged_in_inventory):

    inventory_page = logged_in_inventory

    with allure.step("Add two products"):
        inventory_page.add_product_to_cart(test_data.BACKPACK)
        inventory_page.add_product_to_cart(test_data.BIKE_LIGHT)

    with allure.step("Navigate to shopping cart"):
        cart_page = inventory_page.open_cart()

    with allure.step("Verify shopping cart URL"):
        expect(cart_page.page).to_have_url(cart_page.URL)

    with allure.step("Verify both products appear in cart"):
        expect(
            cart_page.product_name(test_data.BACKPACK)
        ).to_be_visible()

        expect(
            cart_page.product_name(test_data.BIKE_LIGHT)
        ).to_be_visible()


@allure.title("Verify navigation to checkout information page")
@allure.description(
    "Verify that a logged-in user can add a product "
    "and navigate to the checkout information form."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_navigate_to_checkout(logged_in_inventory):

    inventory_page = logged_in_inventory

    with allure.step("Add a product to cart"):
        inventory_page.add_product_to_cart(test_data.BACKPACK)

    with allure.step("Open shopping cart"):
        cart_page = inventory_page.open_cart()

    with allure.step("Proceed to checkout"):
        checkout_page = cart_page.checkout()

    with allure.step("Verify checkout information page"):
        expect(checkout_page.page).to_have_url(checkout_page.URL)
        expect(checkout_page.first_name_input()).to_be_visible()
        expect(checkout_page.last_name_input()).to_be_visible()
        expect(checkout_page.postal_code_input()).to_be_visible()


@allure.title("Verify checkout information can be submitted")
@allure.description(
    "Verify that a customer can enter valid checkout "
    "information and proceed to the order overview page."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_checkout_customer_information(logged_in_inventory):

    inventory_page = logged_in_inventory

    with allure.step("Add product to cart"):
        inventory_page.add_product_to_cart(test_data.BACKPACK)

    with allure.step("Open cart and proceed to checkout"):
        cart_page = inventory_page.open_cart()
        checkout_page = cart_page.checkout()

    with allure.step("Fill customer information"):
        overview_page = checkout_page.fill_customer_information(
            test_data.FIRST_NAME,
            test_data.LAST_NAME,
            test_data.POSTAL_CODE
        )

    with allure.step("Verify navigation to order overview"):
        expect(overview_page.page).to_have_url(
            overview_page.URL
        )


@allure.title("Verify successful end-to-end purchase")
@allure.description(
    "Verify that a user can complete a purchase "
    "from login through order confirmation."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_complete_purchase(logged_in_inventory):

    inventory_page = logged_in_inventory

    with allure.step("Add product to cart"):
        inventory_page.add_product_to_cart(test_data.BACKPACK)

    with allure.step("Open cart and proceed to checkout"):
        cart_page = inventory_page.open_cart()
        checkout_page = cart_page.checkout()

    with allure.step("Fill checkout information"):
        overview_page = checkout_page.fill_customer_information(
            test_data.FIRST_NAME,
            test_data.LAST_NAME,
            test_data.POSTAL_CODE
        )

    with allure.step("Finish order"):
        complete_page = overview_page.finish_order()

    with allure.step("Verify successful purchase"):
        expect(complete_page.page).to_have_url(
            complete_page.URL
        )
        expect(
            complete_page.order_confirmation()
        ).to_have_text("Thank you for your order!")


@pytest.mark.parametrize(
    "first_name,last_name,postal_code,expected_error",
    [
        (
                "",
                test_data.LAST_NAME,
                test_data.POSTAL_CODE,
                "Error: First Name is required"
        ),
        (
                test_data.FIRST_NAME,
                "",
                test_data.POSTAL_CODE,
                "Error: Last Name is required"
        ),
        (
                test_data.FIRST_NAME,
                test_data.LAST_NAME,
                "",
                "Error: Postal Code is required"
        )
    ],
    ids=[
        "missing-first-name",
        "missing-last-name",
        "missing-postal-code"
    ]
)
@allure.title("Verify checkout required fields: {param_id}")
@allure.description(
    "Verify that checkout displays the correct validation "
    "message when a required customer field is missing."
)
@allure.severity(allure.severity_level.NORMAL)
def test_checkout_required_fields(
        logged_in_inventory,
        first_name,
        last_name,
        postal_code,
        expected_error
):
    inventory_page = logged_in_inventory

    with allure.step("Navigate to checkout"):
        inventory_page.add_product_to_cart(test_data.BACKPACK)
        cart_page = inventory_page.open_cart()
        checkout_page = cart_page.checkout()

    with allure.step("Fill customer fields"):
        checkout_page.fill_customer_fields(
            first_name,
            last_name,
            postal_code
        )

    with allure.step("Submit checkout information"):
        checkout_page.submit_customer_information()

    with allure.step("Verify correct validation error"):
        expect(checkout_page.error_message()).to_have_text(
            expected_error
        )

        expect(checkout_page.page).to_have_url(
            checkout_page.URL
        )


@pytest.mark.parametrize(
    "sort_option,data_type,descending",
    [
        (SortOption.PRICE_LOW_TO_HIGH, "price", False),
        (SortOption.PRICE_HIGH_TO_LOW, "price", True),
        (SortOption.NAME_A_TO_Z, "name", False),
        (SortOption.NAME_Z_TO_A, "name", True),
    ],
    ids=[
        "price-low-to-high",
        "price-high-to-low",
        "name-a-to-z",
        "name-z-to-a",
    ]
)
@allure.title("Verify product sorting: {param_id}")
@allure.description(
    "Verify that products are displayed in the correct "
    "order according to the selected sorting option."
)
@allure.severity(allure.severity_level.NORMAL)
def test_product_sorting(
        logged_in_inventory,
        sort_option,
        data_type,
        descending
):
    inventory_page = logged_in_inventory

    with allure.step(f"Select sorting option: {sort_option}"):
        inventory_page.sort_products(sort_option)

    with allure.step("Get displayed product data"):
        if data_type == "price":
            actual_values = inventory_page.get_product_prices()
        else:
            actual_values = inventory_page.get_product_names()

    with allure.step("Verify products were found"):
        assert actual_values, "No products were found"

    with allure.step("Verify correct sorting order"):
        expected_values = sorted(
            actual_values,
            reverse=descending
        )

        assert actual_values == expected_values


@allure.title("Verify cart is empty before adding products")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_is_empty_by_default(logged_in_inventory):
    inventory_page = logged_in_inventory

    with allure.step("Open cart without adding products"):
        cart_page = inventory_page.open_cart()

    with allure.step("Verify cart contains no products"):
        expect(cart_page.cart_items).to_have_count(0)


@allure.title("Verify cart becomes empty after removing a product")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_empty_after_removing_product(logged_in_inventory):
    inventory_page = logged_in_inventory

    with allure.step("Add backpack to cart"):
        inventory_page.add_product_to_cart(test_data.BACKPACK)

    with allure.step("Verify cart badge shows one product"):
        expect(inventory_page.cart_badge).to_have_text("1")

    with allure.step("Remove backpack from cart"):
        inventory_page.remove_product_from_cart(test_data.BACKPACK)

    with allure.step("Verify cart badge disappears"):
        expect(inventory_page.cart_badge).to_have_count(0)

    with allure.step("Open cart"):
        cart_page = inventory_page.open_cart()

    with allure.step("Verify cart is empty"):
        expect(cart_page.cart_items).to_have_count(0)


@allure.title("Verify checkout behavior with empty cart")
@allure.severity(allure.severity_level.NORMAL)
def test_checkout_with_empty_cart(logged_in_inventory):
    inventory_page = logged_in_inventory

    with allure.step("Open empty cart"):
        cart_page = inventory_page.open_cart()

    with allure.step("Verify cart is empty"):
        expect(cart_page.cart_items).to_have_count(0)

    with allure.step("Verify checkout button is visible"):
        expect(cart_page.checkout_button).to_be_visible()