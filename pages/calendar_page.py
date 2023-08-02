from pages.base_page import BasePage
from pages.locators import calendar_page_locators as locs
import datetime
import calendar


class CalendarPage(BasePage):
    page_url = '/Calendar.cshtml'
    today = datetime.date.today()
    day_of_m_today = int(today.strftime('%d'))
    day_of_w_today = today.strftime('%A')
    month_today = today.strftime('%B')
    year_today = today.strftime('%Y')

    def check_current_date_on_top_bar(self):
        current_date = self.find(locs.current_date_loc).text
        return current_date == f'{self.day_of_w_today}, {self.month_today} {self.day_of_m_today}, {self.year_today}'

    def click_month_button(self):
        self.find(locs.month_dropdown).click()

    def check_current_month_name_in_calendar(self):
        return self.find(locs.month_name_loc).text == f'{self.month_today} {self.year_today}'

    def check_current_day_in_calendar(self):
        return int(self.find(locs.today_day_loc).get_attribute('data-day')) == self.day_of_m_today

    def switch_to_the_next_month(self):
        self.find(locs.next_loc).click()

    def switch_to_the_previous_month(self):
        self.find(locs.previous_loc).click()

    @property
    def check_next_month_is_displayed(self):
        last_day = self.today.replace(day=28)
        next_month = (last_day + datetime.timedelta(days=4)).strftime('%B')
        next_year = (last_day + datetime.timedelta(days=4)).strftime('%Y')
        return self.find(locs.month_name_loc).text == f'{next_month} {next_year}'

    @property
    def check_previous_month_is_displayed(self):
        first_day = self.today.replace(day=1)
        next_month = (first_day - datetime.timedelta(days=1)).strftime('%B')
        next_year = (first_day - datetime.timedelta(days=1)).strftime('%Y')
        return self.find(locs.month_name_loc).text == f'{next_month} {next_year}'

    def check(self):
        year = self.find(locs.year_loc)
        year.click()

    def click_month(self, month: int):
        months_list = self.find_all(locs.months_current_year_loc)[852:864]
        months_list[month - 1].click()

    def check_correct_month_is_displayed(self, month):
        months_list = list(calendar.month_name)
        return self.find(locs.month_name_loc).text == f'{months_list[month]} {self.year_today}'
