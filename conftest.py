import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LogInPage


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('user-data-dir=finalsurge-test')
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def check_user_logged(driver):
    login = LogInPage(driver)
    if login.check_user_is_logged():
        pass
    else:
        login.enter_email(login.email)
        login.enter_password(login.password)
        login.click_login_button()
