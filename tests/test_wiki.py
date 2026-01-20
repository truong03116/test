import os
import csv
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def read_data_from_file(filename):
    base_dir = os.path.dirname(__file__)      # thư mục tests
    file_path = os.path.join(base_dir, filename)

    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        return [row['keyword'] for row in csv_reader]

class TestWiki:

    @pytest.mark.parametrize('keyword', read_data_from_file('data.csv'))
    def test_search_wiki(self, driver, keyword):
        search_box = driver.find_element(By.ID, "searchInput")
        search_box.click()
        search_box.send_keys(keyword + Keys.ENTER)
        sleep(3)
