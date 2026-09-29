from pages.login_page import LoginPage

def test_valid_login(driver):
    driver.get("https://example.com/login")
    page = LoginPage(driver)
    page.login("demo@example.com", "Password123")
    assert "Dashboard" in driver.title
