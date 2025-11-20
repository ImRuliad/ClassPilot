import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urljoin

ANCHOR_TAG = "a"
HREF_ELEMENT = "href"

def _navigate_to_semester_url(webdriver: WebDriver, semester_url: str):
    webdriver.get(semester_url)
    logging.info(f"Successfully navigated to {semester_url}")

def _get_div_elements(webdriver: WebDriver):
    wait_time = 5
    wait = WebDriverWait(webdriver, wait_time)
    section_div = "//section//div"
    try:
        section_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, section_div)))
        logging.info("Successfully located div elements")
        return section_element
    except Exception as e:
        logging.info(f"Unable to locate div elements {e}")
        raise
        
def _extract_outer_html_from_div_elements(divs) -> list[str]:
    div_htmls = []
    div_element = divs
    try:
        for element in div_element:
            outer_html = element.get_attribute("outerHTML")
            div_htmls.append(outer_html)
        if div_htmls:
            logging.info("Successfully populated div htmls")
            return div_htmls
        else:
            logging.warning("div htmls is empty.")
    except Exception as e:
        logging.error(f"An error occurred finding div htmls {e}")
        raise
        
def _join_div_html_to_string(div_htmls) -> str:
    html_string = "".join(div_htmls)
    return html_string

def _parse_major_url_from_html(html_string, semester_url) -> dict[str: str]:
    major_urls = {}
    try:
        soup = BeautifulSoup(html_string, "html.parser")
        for item in soup.find_all(ANCHOR_TAG):
            major_name = item.text.strip()
            relative_path = item.get(HREF_ELEMENT)
            major_url = urljoin(semester_url, relative_path)
            major_urls[major_name] = major_url
        logging.info("Successfully parsed major urls from html elements")
        return major_urls
    except Exception as e:
        logging.error(f"An error occurred parsing major urls from html elements {e}")
        raise

def get_major_urls(webdriver: WebDriver, semester_url: str):
    _navigate_to_semester_url(webdriver, semester_url)
    divs = _get_div_elements(webdriver)
    div_html = _extract_outer_html_from_div_elements(divs)
    html_string = _join_div_html_to_string(div_html)
    major_urls = _parse_major_url_from_html(html_string, semester_url)
    return major_urls

    
