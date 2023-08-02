import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.calendar_page import CalendarPage
from pages.login_page import LogInPage
from pages.locators import login_page_locators as locs


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument(r"user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\finalsurge")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def check_user_is_logged(driver):
    login = LogInPage(driver)
    base = CalendarPage(driver)
    base.open_page()
    welcome_message = login.find_all(locs.welcome_loc)
    if len(welcome_message) > 0:
        pass
    else:
        login.enter_email(login.email)
        login.enter_password(login.password)
        login.find(locs.login_remember).click()
        login.click_login_button()
