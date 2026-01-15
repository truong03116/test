from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By

def test_forward_navigation(driver):
    driver.get("https://google.com")
    sleep(3)
    driver.back()
    sleep(3)
    driver.forward()
    sleep(3)
    assert driver.find_element(By.XPATH, "//img[@class='lnXdpd']").is_displayed()