from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_hide(driver):
    driver.get("https://www.letskodeit.com/practice")
    sleep(3)
    driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()
    display_text = driver.find_element(By.ID,"displayed-text")
    driver.execute_script("arguments[0].value = 'Hello'", display_text)
    driver.find_element(By.ID,"show-textbox").click()
    sleep(3)
def test_img(driver):
    driver.get("https://www.letskodeit.com/practice")
    sleep(3)
    hide_button = driver.find_element(By.XPATH,"//input[@id='disabled-button']")
    hide_button.click()
    hide_button.screenshot("anh.png")
    sleep(3)
    