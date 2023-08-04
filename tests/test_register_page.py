import pytest
from pages.register_page import RegisterPage


def test_first_name_missing(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.enter_last_name(register_page.first_name)
    register_page.enter_email(register_page.last_name)
    register_page.select_timezone(2)
    register_page.enter_password(register_page.password)
    register_page.confirm_password(register_page.password)
    register_page.click_create_an_account_button()
    assert register_page.missing_error.is_displayed()
    assert register_page.missing_error_is_correct


def test_last_name_missing(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.enter_first_name(register_page.first_name)
    register_page.enter_email(register_page.last_name)
    register_page.select_timezone(2)
    register_page.enter_password(register_page.password)
    register_page.confirm_password(register_page.password)
    register_page.click_create_an_account_button()
    assert register_page.missing_error.is_displayed()
    assert register_page.missing_error_is_correct


def test_email_missing(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.enter_first_name(register_page.first_name)
    register_page.enter_last_name(register_page.last_name)
    register_page.select_timezone(2)
    register_page.enter_password(register_page.password)
    register_page.confirm_password(register_page.password)
    register_page.click_create_an_account_button()
    assert register_page.missing_error.is_displayed()
    assert register_page.missing_error_is_correct


def test_timezone_not_selected(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.enter_first_name(register_page.first_name)
    register_page.enter_last_name(register_page.last_name)
    register_page.enter_email(register_page.email)
    register_page.select_timezone(0)
    register_page.enter_password(register_page.password)
    register_page.confirm_password(register_page.password)
    register_page.click_create_an_account_button()
    assert register_page.missing_error.is_displayed()
    assert register_page.missing_error_is_correct


@pytest.mark.parametrize(
    'password',
    ['a' * 6, 'a' * 16, 'testtest', 'TESTTEST', 'testTEST', '1234567', 'test123', 'TEST123']
)
def test_invalid_password(driver, password):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.enter_first_name(register_page.first_name)
    register_page.enter_last_name(register_page.last_name)
    register_page.select_timezone(2)
    register_page.enter_email(register_page.email)
    register_page.enter_password(password)
    register_page.confirm_password(password)
    register_page.click_create_an_account_button()
    assert register_page.password_error.is_displayed()
    assert register_page.invalid_password_error_is_correct


def test_password_confirmation(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.enter_first_name(register_page.first_name)
    register_page.enter_last_name(register_page.last_name)
    register_page.enter_email(register_page.email)
    register_page.select_timezone(2)
    register_page.enter_password(register_page.password)
    register_page.confirm_password(register_page.different_password)
    register_page.click_create_an_account_button()
    assert register_page.password_error.is_displayed()
    assert register_page.password_confirmation_error_is_correct


def test_very_weak_password(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    very_weak_password = register_page.very_weak_passw['password']
    register_page.enter_password(very_weak_password)
    assert register_page.check_password_bar_color(very_weak_password)
    assert register_page.check_password_bar_width(very_weak_password)
    assert register_page.check_password_bar_text(very_weak_password)


def test_weak_password(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    weak_password = register_page.weak_passw['password']
    register_page.enter_password(weak_password)
    assert register_page.check_password_bar_color(weak_password)
    assert register_page.check_password_bar_width(weak_password)
    assert register_page.check_password_bar_text(weak_password)


def test_medium_password(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    medium_password = register_page.medium_passw['password']
    register_page.enter_password(medium_password)
    assert register_page.check_password_bar_color(medium_password)
    assert register_page.check_password_bar_width(medium_password)
    assert register_page.check_password_bar_text(medium_password)


def test_strong_password(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    strong_password = register_page.strong_passw['password']
    register_page.enter_password(strong_password)
    assert register_page.check_password_bar_color(strong_password)
    assert register_page.check_password_bar_width(strong_password)
    assert register_page.check_password_bar_text(strong_password)


def test_very_strong_password(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    very_strong_password = register_page.very_strong_passw['password']
    register_page.enter_password(very_strong_password)
    assert register_page.check_password_bar_color(very_strong_password)
    assert register_page.check_password_bar_width(very_strong_password)
    assert register_page.check_password_bar_text(very_strong_password)


def test_register_with_registered_email(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.enter_first_name(register_page.first_name)
    register_page.enter_last_name(register_page.last_name)
    register_page.select_timezone(2)
    register_page.enter_email(register_page.email)
    register_page.enter_password(register_page.password)
    register_page.confirm_password(register_page.password)
    register_page.click_create_an_account_button()
    assert register_page.associated_email_error.is_displayed()
    assert register_page.associated_email_error_is_correct
