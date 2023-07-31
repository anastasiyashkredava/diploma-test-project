from pages.base_page import BasePage
from pages.locators import login_page_locators as locs


class LogInPage(BasePage):
    page_url = '/login.cshtml'

    email_error_text = 'Please enter your e-mail address.'
    password_error_text = 'Please enter a password.'
    invalid_credentials_error_text = 'Invalid login credentials. Please try again.'

    def enter_email(self, email):
        self.find(locs.email_loc).send_keys(email)

    def enter_password(self, passw):
        self.find(locs.passw_loc).send_keys(passw)

    def click_login_button(self):
        self.find(locs.login_button).click()

    @property
    def check_user_is_logged(self):
        return self.find(locs.welcome_loc).is_displayed()

    @property
    def error(self):
        return self.find(locs.error_loc)

    @property
    def check_email_error_is_correct(self):
        return self.error.text == self.email_error_text

    @property
    def check_password_error_is_correct(self):
        return self.error.text == self.password_error_text

    @property
    def invalid_credentials_error(self):
        return self.find(locs.invalid_credentials_error)

    @property
    def check_invalid_credential_error_is_correct(self):
        return self.invalid_credentials_error.text == self.invalid_credentials_error_text

    @property
    def check_entered_email_remains(self):
        return self.find(locs.email_loc).get_attribute('value') == self.email

    @property
    def check_password_field_clean(self):
        return self.find(locs.passw_loc).get_attribute('value') == ''
