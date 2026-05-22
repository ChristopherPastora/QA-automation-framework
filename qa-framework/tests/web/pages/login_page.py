from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT   = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR    = (By.CLASS_NAME, "error-message")

    def open(self, base_url: str):
        self.driver.get(f"{base_url}{self.URL}")

    def login(self, username: str, password: str):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error(self) -> str:
        return self.get_text(self.ERROR)
