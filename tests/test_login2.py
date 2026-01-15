from pages.login_page import LoginPage_1
from selenium import webdriver
import pytest
from time import sleep

class TestLogin_1:
    def test_login_pass(self,driver):
        login_page = LoginPage_1(driver)
        login_page.do_login("Admin","admin123")
        sleep(5)
        