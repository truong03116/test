from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from utils.config_reader import ConfigReader
from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
    assert login_page.get_dashboard_header()
    sleep(5)