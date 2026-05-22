from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.logger.info(f"Click en: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.logger.info(f"Escribiendo en: {locator}")
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        return self.find(locator).text
