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
    options = webdriver.ChromeOptions()
    # Tắt headless mode để nhìn thấy reCAPTCHA
    # options.add_argument("--headless")  # Comment out để thấy browser
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()

    # ✅ BẮT BUỘC CHO GITHUB ACTIONS
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.wikipedia.org/")
    yield driver
    driver.quit()
