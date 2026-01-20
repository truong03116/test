import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utilies.api_helper import APIHelper
from utils.config_reader import ConfigReader

@pytest.mark.api
class TestAPI:
    def test_get_endpoint(self):
        self.api_helper = APIHelper(ConfigReader.get_api_url())
        response = self.api_helper.get("api/users",params={"page":2}
        print)

