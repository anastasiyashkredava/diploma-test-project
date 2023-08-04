import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.calendar_page import CalendarPage
from pages.login_page import LogInPage
from pages.locators import login_page_locators as login_locs
from pages.locators import calendar_page_locators as cal_locs


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument(r"user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\surge")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def check_user_is_logged(driver):
    login = LogInPage(driver)
    base = CalendarPage(driver)
    base.open_page()
    welcome_message = login.find_all(login_locs.welcome_loc)
    if len(welcome_message) > 0:
        pass
    else:
        login.enter_email(login.email)
        login.enter_password(login.password)
        login.find(login_locs.login_remember).click()
        login.click_login_button()


@pytest.fixture()
def delete_workouts(driver):
    calendar_page = CalendarPage(driver)
    while True:
        workouts = calendar_page.find_all(cal_locs.workout_in_calendar_2)
        if len(workouts) > 0:
            calendar_page.find(cal_locs.workout_in_calendar_2).click()
            calendar_page.find_all(cal_locs.workout_menu)[7].click()
            calendar_page.wait_until_visibility(cal_locs.delete_ok)
            calendar_page.find(cal_locs.delete_ok).click()
            driver.refresh()
        else:
            break
    yield
    calendar_page.open_page()
    calendar_page.delete_a_workout()
