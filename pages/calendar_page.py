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

    def click_year(self):
        self.find(locs.year_loc).click()

    def switch_to_the_next_year(self):
        self.find(locs.next_year_loc).click()

    def switch_to_the_previous_year(self):
        self.find(locs.prev_year_loc).click()

    @property
    def check_next_year_is_displayed(self):
        next_year = int(self.year_today) + 1
        return self.find(locs.month_name_loc).text.split()[1] == str(next_year)

    @property
    def check_previous_year_is_displayed(self):
        prev_year = int(self.year_today) - 1
        return self.find(locs.month_name_loc).text.split()[1] == str(prev_year)

    def select_month(self, month: int):
        months_list = self.find_all(locs.months_loc)[852:864]
        months_list[month - 1].click()

    def check_correct_month_is_displayed(self, month: int):
        months_list = list(calendar.month_name)
        return self.find(locs.month_name_loc).text == f'{months_list[month]} {self.year_today}'

    def select_year(self, year):
        list_of_years_in_calendar = self.find_all(locs.years_loc)[853:863]
        list_of_years = list(range(2020, 2030))
        years_dict = {}
        for num in range(len(list_of_years)):
            years_dict[f'{list_of_years[num]}'] = list_of_years_in_calendar[num]
        return years_dict[f'{year}'].click()

    def check_correct_year_is_displayed(self, year):
        return self.find(locs.month_name_loc).text.split()[1] == str(year)
