import logging
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def _set_webdriver_url(webdriver: WebDriver, major_url: str) -> None:
    try:
        webdriver.get(major_url)
    except Exception:
        logging.error(f"Unable to set webdriver url for {major_url}")
        raise

def _wait_for_html_element(webdriver: WebDriver):
    wait_time = 5
    WebDriverWait(webdriver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.table")))

def _get_soup(webdriver: WebDriver):
    html = webdriver.page_source
    return BeautifulSoup(html, "html.parser")

def get_courses_data(webdriver, major_urls, semester_name):
    for major, url in major_urls.items():
        logging.info(f"Fetching courses for {major} at {url}")
        _set_webdriver_url(webdriver, url)
        _wait_for_html_element(webdriver)
        soup = _get_soup(webdriver)

        table_divs = soup.select("div.table")

        for div in table_divs:
            h2_tag = div.find("h2")
            raw_title = h2_tag.get_text(strip=True)
            match = re.match(r'^(.*?) - (.*?) - (\d+) Units$', raw_title)
            if match:
                course_code = match.group(1)
                course_title = match.group(2)
                course_units = match.group(3)
                print(course_code, course_title, course_units)
            else:
                logging.error(f"Unable to parse course title: {raw_title}")

