from selenium import webdriver
import pytest
import os

from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement

# Ensure element.screenshot saves into `images/` when a bare filename is provided.
if not hasattr(RemoteWebElement, "_screenshot_wrapped"):
    _orig_screenshot = RemoteWebElement.screenshot

    def _screenshot_with_images(self, filename):
        os.makedirs('images', exist_ok=True)
        # If filename has no directory component, prepend images/
        if not ("/" in filename or "\\" in filename):
            filename = os.path.join('images', filename)
        return _orig_screenshot(self, filename)

    RemoteWebElement.screenshot = _screenshot_with_images
    RemoteWebElement._screenshot_wrapped = True




@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    url = "https://opensource-demo.orangehrmlive.com/"
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


