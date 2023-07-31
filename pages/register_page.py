from pages.base_page import BasePage
from pages.locators import register_page_locators as locs
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.color import Color


class RegisterPage(BasePage):
    page_url = '/register.cshtml'

    missing_error_text = 'This field is required.'
    invalid_password_error_text = 'Error: *Please enter a Password value with at least one number, ' \
                                  'lower-case letter, and upper-case letter between 7 and 15 characters in length.'
    confirmation_error_text = 'Error: The passwords you entered did not match.'
    associated_error_text = 'Error: There is already a user account associated with this Email Address.' \
                            '  Please retrieve your password or create an account with a different address.'

    very_weak_passw = {'password': 'test', 'hex': '#dd514c', 'width': '16%;', 'text': 'VERY WEAK'}
    weak_passw = {'password': '123', 'hex': '#dd514c', 'width': '33%;', 'text': 'WEAK'}
    medium_passw = {'password': 'Test123', 'hex': '#faa732', 'width': '50%;', 'text': 'MEDIUM'}
    strong_passw = {'password': 'Test123!', 'hex': '#5eb95e', 'width': '75%;', 'text': 'STRONG'}
    very_strong_passw = {'password': 'Test123!test@', 'hex': '#5eb95e', 'width': '100%;', 'text': 'VERY STRONG'}

    def enter_first_name(self, firstname):
        self.find(locs.first_name_loc).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.find(locs.last_name_loc).send_keys(lastname)

    def enter_email(self, email):
        self.find(locs.e_mail_loc).send_keys(email)

    def enter_password(self, password):
        self.find(locs.passw_loc).send_keys(password)

    def select_timezone(self, timezone_index):
        time_zone = self.find(locs.timezone_loc)
        Select(time_zone).select_by_index(timezone_index)

    def confirm_password(self, confirm_password):
        self.find(locs.confirm_passw_loc).send_keys(confirm_password)

    def click_create_an_account_button(self):
        self.find(locs.create_button_loc).click()

    @property
    def confirmation_error(self):
        return self.find(locs.password_error_loc).get

    @property
    def missing_error(self):
        return self.find(locs.missing_error_loc)

    @property
    def missing_error_is_correct(self):
        return self.find(locs.missing_error_loc).text == self.missing_error_text

    @property
    def password_error(self):
        return self.find(locs.password_error_loc)

    @property
    def invalid_password_error_is_correct(self):
        return self.find(locs.password_error_loc).text == self.invalid_password_error_text

    @property
    def password_confirmation_error_is_correct(self):
        return self.find(locs.password_error_loc).text == self.confirmation_error_text

    @property
    def associated_email_error(self):
        return self.find(locs.password_error_loc)

    @property
    def associated_email_error_is_correct(self):
        return self.associated_email_error.text.split() == self.associated_error_text.split()

    def check_password_bar_color(self, password):
        rgba = self.find(locs.bar_loc).value_of_css_property('background-color')
        hex_vw = Color.from_string(rgba).hex
        if password == self.very_weak_passw['password'] or password == self.weak_passw['password']:
            return True if hex_vw == self.weak_passw['hex'] else False
        elif password == self.medium_passw['password']:
            return True if hex_vw == self.medium_passw['hex'] else False
        elif password == self.strong_passw['password'] or password == self.very_strong_passw['password']:
            return True if hex_vw == self.strong_passw['hex'] else False

    def check_password_bar_width(self, password):
        width = self.find(locs.bar_loc).get_attribute('style').split()[1]
        if password == self.very_weak_passw['password']:
            return True if width == self.very_weak_passw['width'] else False
        elif password == self.weak_passw['password']:
            return True if width == self.weak_passw['width'] else False
        elif password == self.medium_passw['password']:
            return True if width == self.medium_passw['width'] else False
        elif password == self.strong_passw['password']:
            return True if width == self.strong_passw['width'] else False
        elif password == self.very_strong_passw['password']:
            return True if width == self.very_strong_passw['width'] else False

    def check_password_bar_text(self, password):
        bar_text = self.find(locs.bar_text_loc).text
        if password == self.very_weak_passw['password']:
            return True if bar_text == self.very_weak_passw['text'] else False
        elif password == self.weak_passw['password']:
            return True if bar_text == self.weak_passw['text'] else False
        elif password == self.medium_passw['password']:
            return True if bar_text == self.medium_passw['text'] else False
        elif password == self.strong_passw['password']:
            return True if bar_text == self.strong_passw['text'] else False
        elif password == self.very_strong_passw['password']:
            return True if bar_text == self.very_strong_passw['text'] else False
