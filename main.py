import logging
from pkgBackend.scraper.fetch_semester_urls import get_semester_urls
from pkgBackend.scraper.fetch_major_urls import get_major_urls
from pkgBackend.scraper.setup import Browser




if __name__ == "__main__":
    base_url = "https://www.csus.edu/class-schedule/"
    logging.basicConfig(level=logging.INFO)
    headless = True
    page_load_strategy = "eager"
    
    webdriver = Browser(headless=headless, page_load_strategy=page_load_strategy)
    driver = webdriver.create_webdriver()
    
    semester_urls = get_semester_urls(driver, base_url)
    if semester_urls:
        major_urls = get_major_urls(driver, semester_urls[0])
        print(major_urls)