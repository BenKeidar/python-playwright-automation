def test_homepage_title(page):
    page.goto("https://www.saucedemo.com/")

    assert page.title() == "Swag Labs"
