from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver1 = driver
        
    def enter_username(self,username):
        self.driver1.find_element(By.NAME,"username").send_keys(username)

    def enter_password(self,password):
        self.driver1.find_element(By.NAME,"password").send_keys(password)

    def click_login(self):
        self.driver1.find_element(By.XPATH, "//button[@type='submit']").click()

    def get_dashboard_header(self):
        return self.driver1.find_element(By.CSS_SELECTOR, ".oxd-text--h6").text=="Dashboard"

    def get_error_message(self):
        return self.driver1.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text").text=="Invalid credentials"
    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()