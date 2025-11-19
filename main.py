import logging
from pkgBackend.scraper.fetch_semester_urls import get_semester_urls
from pkgBackend.scraper.fetch_major_urls import get_major_urls
from pkgBackend.scraper.fetch_courses import get_courses_data
from pkgBackend.scraper.formatter import get_name_from_sem_url
from pkgBackend.scraper.setup import Browser



if __name__ == "__main__":
    base_url = "https://www.csus.edu/class-schedule/"
    logging.basicConfig(level=logging.INFO)
    headless = True
    page_load_strategy = "eager"
    
    webdriver = Browser(headless=headless, page_load_strategy=page_load_strategy)
    driver = webdriver.create_webdriver()
    
    #contains a list of semester url links
    semester_urls: list [str] = get_semester_urls(driver, base_url)
    
    #contains a nested dictionary (key = semester name, value = {major: major url})
    major_urls: dict[str, dict[str: str]] = { 
        get_name_from_sem_url(sem_url): get_major_urls(driver, sem_url) 
        for sem_url in semester_urls}
    
    for semester_name, majors in major_urls.items():
        logging.info(f"Fetching courses for {semester_name}")
        get_courses_data(driver, majors, semester_name)
    