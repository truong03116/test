from selenium import webdriver
from pages.login_page_update import LoginPage
import pytest
from time import sleep

class TestLogin:
    @pytest.mark.smoke
    def test_login_pass(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
        sleep(5)
        assert login_page.get_dashboard_header()