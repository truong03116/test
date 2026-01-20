import pytest
from pages.login_page_update import LoginPage

class TestLogin:

    @pytest.mark.smoke
    def test_login_pass(self, driver):
        # ✅ BẮT BUỘC
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
