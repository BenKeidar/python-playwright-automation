import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    login = LoginPage(page)

    print("\nSETUP: Opening login page")
    login.open()

    yield login

    print("\nTEARDOWN: Test finished")
