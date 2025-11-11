import logging
from pkgBackend.scraper.fetch_semester_urls import get_semester_urls
from pkgBackend.scraper.setup import WebDriver




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    headless = True
    page_load_strategy = "eager"
    
    webdriver = WebDriver(headless=headless, page_load_strategy=page_load_strategy)
    driver = webdriver.create_webdriver()
    
    base_url = "https://www.csus.edu/class-schedule/"
    semester_urls = get_semester_urls(driver, base_url)
    print(semester_urls)