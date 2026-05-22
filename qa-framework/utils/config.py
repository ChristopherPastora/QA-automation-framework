import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://example.com")
    API_URL  = os.getenv("API_URL",  "https://jsonplaceholder.typicode.com")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT  = int(os.getenv("TIMEOUT", "10"))
