from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.wallashops.co.il/login?rurl=8"

    def open(self):
        self.driver.get(self.url)

    def click_login_button(self):
        button = self.driver.find_element(By.CLASS_NAME, "mobile-login-btn")
        if button.get_attribute("aria-expanded") == "false":
            button.click()

    def login(self, username, password):
        self.click_login_button()
        email_field = self.driver.find_element(By.ID, "login-form-email")
        password_field = self.driver.find_element(By.ID, "login-form-password")
        email_field.send_keys(username)
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'כניסה לוואלה!שופס')]")
        login_button.click()
        return True


   