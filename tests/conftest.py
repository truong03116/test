from selenium import webdriver
import pytest
import os
from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement

# Screenshot wrapper (OK – giữ lại)
if not hasattr(RemoteWebElement, "_screenshot_wrapped"):
    _orig_screenshot = RemoteWebElement.screenshot

    def _screenshot_with_images(self, filename):
        os.makedirs("images", exist_ok=True)
        if not ("/" in filename or "\\" in filename):
            filename = os.path.join("images", filename)
        return _orig_screenshot(self, filename)

    RemoteWebElement.screenshot = _screenshot_with_images
    RemoteWebElement._screenshot_wrapped = True


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()

    is_ci = os.getenv("CI") == "true"

    if is_ci:
        # ✅ GitHub Actions
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
    else:
        # ✅ Local
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.wikipedia.org/")
    yield driver
    driver.quit()
