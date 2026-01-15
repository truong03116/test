from selenium import webdriver
import pytest
import csv
from selenium.webdriver.common.by import By
from time import sleep 
from selenium.webdriver.common.keys import Keys
class TestWiki:
    def read_data_from_file(file_path):
        with open(file_path,mode='r') as file:
            csv_reader = csv.DictReader(file)
            keywords = []
            for row in csv_reader:
                keywords.append(row['keyword'])
            return keywords
    testdata = read_data_from_file('data.csv')
    @pytest.mark.parametrize('keyword',testdata)
    def test_search_wiki(self,driver,keyword):
        search_box = driver.find_element(By.ID,"searchInput")
        search_box.click()
        search_box.send_keys(keyword + Keys.ENTER)

        sleep(3)
