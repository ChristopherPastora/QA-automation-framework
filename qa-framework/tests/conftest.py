import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import Config

@pytest.fixture(scope="session")
def config():
    return Config()

@pytest.fixture(scope="function")
def driver(config):
    options = Options()
    if config.HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(config.TIMEOUT)
    yield driver
    driver.quit()
