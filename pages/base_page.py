from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv


class BasePage:
    base_url = 'https://log.finalsurge.com'
    page_url = None
    pix = None
    load_dotenv()
    email = os.getenv('email')
    password = os.getenv('password')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            NotImplementedError('Page can not be opened by URL')

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def scroll(self, pix):
        if not self.pix:
            return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            return self.driver.execute_script(f"window.scrollTo(0, {pix})")

    def wait_until_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
