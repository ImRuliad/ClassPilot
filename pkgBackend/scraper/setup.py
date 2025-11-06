import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebDriver:
    def __init__(self, headless=True, disable_gpu=True, page_load_strategy=True):
        self._driver = None
        self._headless = headless
        self._disable_gpu = disable_gpu
        self._page_load_strategy = page_load_strategy
    
    def create_webdriver(self):
        try:
            service = Service(ChromeDriverManager().install())
            self._driver = webdriver.Chrome(service=service)
            logging.info("Successfully created webdriver")
            return self._driver
        except Exception as e:
            logging.error(f"Error occurred creating webdriver {e}")
    