import pytest
import allure
from data import test_data
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    login = LoginPage(page)

    print("\nSETUP: Opening login page")
    login.open()

    yield login

    print("\nTEARDOWN: Test finished")


@pytest.fixture
def logged_in_inventory(login_page) -> InventoryPage:
    inventory_page = login_page.login(
        test_data.VALID_USERNAME,
        test_data.VALID_PASSWORD
    )

    return inventory_page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page is not None and not page.is_closed():
            screenshot = page.screenshot(full_page=True)

            allure.attach(
                screenshot,
                name="Screenshot on Failure",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.hookimpl(trylast=True)
def pytest_runtest_teardown(item, nextitem):
    pass
