from selenium.webdriver.common.by import By
class LoginPage_1:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()