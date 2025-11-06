from pkgBackend.scraper.setup import WebDriver



if __name__ == "__main__":
    webdriver_instance = WebDriver()
    driver = webdriver_instance.create_webdriver()
    if driver:
        print("Webdriver created successfully.")
        driver.quit()