import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

class WebDriver:
    def __init__(self, headless=True, disable_gpu=True, page_load_strategy="eager"):
        self._driver = None
        self._headless = headless
        self._disable_gpu = disable_gpu
        self._page_load_strategy = page_load_strategy
    
    def _build_options(self):
        opts = Options()
        if self._headless:
            opts.add_argument("--headless=new")
        if self._disable_gpu:
            opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.page_load_strategy = self._page_load_strategy
        return opts
    
    def create_webdriver(self):
        try:
            opts = self._build_options()
            self._driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
            logging.info("Successfully created webdriver")
            return self._driver
        except Exception as e:
            logging.exception(f"An error occurred creating webdriver {e}")
            raise
    