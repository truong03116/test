from selenium import webdriver
import pytest
from time import sleep
from selenium.webdriver.common.by import By

def test_hidden(driver):
    driver.get("https://www.letskodeit.com/practice")
    hidden_button = driver.find_element(By.ID, "hide-textbox")
    hidden_button.click()
    sleep(2)

    display_text = driver.find_element(By.ID, "displayed-text")
    driver.execute_script("arguments[0].value = 'Hello World'", display_text)

    driver.find_element(By.ID, "show-textbox").click()
    hidden_button.screenshot('hidden_button2.png')

    sleep(3)