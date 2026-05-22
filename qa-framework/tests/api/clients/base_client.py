import requests
from utils.logger import get_logger

class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.logger = get_logger(self.__class__.__name__)

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET {url}")
        return self.session.get(url, **kwargs)

    def post(self, endpoint: str, payload: dict, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST {url} | body: {payload}")
        return self.session.post(url, json=payload, **kwargs)

    def put(self, endpoint: str, payload: dict, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"PUT {url} | body: {payload}")
        return self.session.put(url, json=payload, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE {url}")
        return self.session.delete(url, **kwargs)
