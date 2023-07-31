from pages.login_page import LogInPage


def test_login_without_email(driver):
    login_page = LogInPage(driver)
    login_page.open_page()
    login_page.enter_password(login_page.password)
    login_page.click_login_button()
    assert login_page.error.is_displayed()
    assert login_page.check_email_error_is_correct


def test_login_without_password(driver):
    login_page = LogInPage(driver)
    login_page.open_page()
    login_page.enter_email(login_page.email)
    login_page.click_login_button()
    assert login_page.error.is_displayed()
    assert login_page.check_password_error_is_correct


def test_login_with_incorrect_credentials(driver):
    login_page = LogInPage(driver)
    login_page.open_page()
    login_page.enter_email(login_page.email)
    login_page.enter_password('test123')
    login_page.click_login_button()
    assert login_page.invalid_credentials_error.is_displayed()
    assert login_page.check_invalid_credential_error_is_correct
    assert login_page.check_entered_email_remains
    assert login_page.check_password_field_clean


def test_login_with_correct_credentials(driver):
    login_page = LogInPage(driver)
    login_page.open_page()
    login_page.enter_email(login_page.email)
    login_page.enter_password(login_page.password)
    login_page.click_login_button()
    assert login_page.check_user_is_logged
