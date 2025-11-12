import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def _navigate_to_base_url(webdriver: WebDriver, base_url: str):
    try:
        webdriver.get(base_url)
        logging.info(f"successfully navigated to {base_url}")
    except Exception as e:
        logging.error(f"Unable to navigate to {base_url} {e}")
        return

def _fetch_semester_links(webdriver: WebDriver):
    semester_link_element = '[aria-labelledby="article-head"] li a'
    wait_time = 5
    try:
        wait = WebDriverWait(webdriver, wait_time)
        semester_link_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, semester_link_element)))
        return semester_link_elements
    except Exception as e:
        logging.error(f"Unable to find semester link elements {e}")
        return []
    
def extract_hrefs_from_semester_link_elements(semester_link_elements):
    sem_urls = []
    for html_element in semester_link_elements:
        semester_url = html_element.get_attribute("href")
        sem_urls.append(semester_url)
    return sem_urls

#maybe add semester urls to a database..
def get_semester_urls(webdriver: WebDriver, base_url: str):
    _navigate_to_base_url(webdriver, base_url)
    semester_link_elements = _fetch_semester_links(webdriver)
    semester_urls = extract_hrefs_from_semester_link_elements(semester_link_elements)
    return semester_urls
        
    