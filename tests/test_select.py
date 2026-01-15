from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import pytest
from time import sleep


def test_select_option(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_visible_text("Option 1")
    sleep(3)
    select.select_by_value("2")
    sleep(3)
def test_select_thu(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.find_element(By.ID, "dropdown").click()
    driver.find_element(By.XPATH, "//option[@value='1']").click()
    sleep(3)