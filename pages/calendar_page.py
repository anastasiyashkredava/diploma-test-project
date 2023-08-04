from selenium.webdriver.support.select import Select
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

    date_field_data = f'{int(today.strftime("%m"))}/{day_of_m_today}/{year_today}'
    time_field_data = '12:15 PM'
    activity_data = 'Run'
    workout_name_data = 'Marathon'
    workout_desc_data = 'My first marathon'
    distance = '13.00'
    distance_units = ['mi', 'km', 'm', 'yd']
    duration = '01:58:00'
    pace = '9:04 min/mi'
    how_felt = 'Great'
    perceived_effort = '7 (Hard)'
    post_notes = 'Well done'

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

    def click_quick_add_button(self):
        self.find(locs.quick_add_loc).click()

    def wait_add_form_is_loaded(self):
        return self.wait_until_visibility(locs.date_field_loc)

    def fill_in_the_date_field(self, date):
        date_field = self.find(locs.date_field_loc)
        date_field.clear()
        date_field.click()
        date_field.send_keys(date)

    def fill_in_the_time_field(self, time):
        self.find(locs.time_field_loc).send_keys(time)

    def select_activity_type(self, activity_type):
        Select(self.find(locs.activity_type_loc)).select_by_visible_text(activity_type)

    def fill_in_the_workout_name_field(self, workout_name):
        self.find(locs.workout_name_loc).send_keys(workout_name)

    def fill_in_the_workout_description_field(self, workout_desc):
        self.find(locs.workout_desc_loc).send_keys(workout_desc)

    def fill_in_the_distance_field(self, distance):
        self.find(locs.distance_loc).send_keys(distance)

    def select_distance_type(self, number):
        Select(self.find(locs.distance_type_loc)).select_by_value(self.distance_units[number])

    def fill_in_the_duration_field(self, duration):
        self.find(locs.duration_loc).send_keys(duration)

    def select_how_felt(self, how_felt):
        Select(self.find(locs.how_feel_loc)).select_by_visible_text(how_felt)

    def select_perceived_effort(self, per_effort):
        Select(self.find(locs.perceived_effort_loc)).select_by_visible_text(per_effort)

    def fill_in_the_post_notes(self, post_note):
        self.find(locs.post_workout_notes).send_keys(post_note)

    def click_add_workout_button(self):
        self.find(locs.add_workout_button_loc).click()

    @property
    def check_workout_is_created(self):
        return self.find(locs.activity_type_loc).is_displayed()

    def view_workout_details(self):
        self.find(locs.workout_in_calendar_2).click()
        self.find_all(locs.workout_menu)[0].click()

    def delete_a_workout(self):
        self.find(locs.workout_in_calendar_2).click()
        self.find_all(locs.workout_menu)[7].click()
        self.wait_until_visibility(locs.delete_ok)
        self.find(locs.delete_ok).click()

    @property
    def check_activity_type_data_is_correct(self):
        return self.find(locs.details_activity_type).text == self.activity_data

    @property
    def check_workout_name_is_correct(self):
        return self.find(locs.details_workout_name_loc).text == self.workout_name_data

    @property
    def check_workout_date_is_correct(self):
        return self.find(locs.details_time_loc).text.split(' - ')[0] \
               == f'{self.day_of_w_today}, {self.month_today} {self.day_of_m_today}, {self.year_today}'

    @property
    def check_workout_time_start_is_correct(self):
        return self.find(locs.details_time_loc).text.split(' - ')[1] == self.time_field_data

    @property
    def check_workout_description_is_correct(self):
        return self.find(locs.details_workout_desc_loc).text.split('\n')[1] == self.workout_desc_data

    def check_workout_distance_is_correct(self, number):
        return self.find(locs.details_distance_duration_loc).text.split(' ~ ')[0]\
               == f'{self.distance} {self.distance_units[number]}'

    @property
    def check_workout_duration_is_correct(self):
        duration = self.duration.split(':')
        return self.find(locs.details_distance_duration_loc).text.split(' ~ ')[1]\
               == f'{int(duration[0])}:{duration[1]}:{duration[2]}'

    @property
    def check_workout_pace_is_correct(self):
        return self.find(locs.details_pace_loc).text == self.pace

    @property
    def check_workout_how_felt_is_correct(self):
        return self.find(locs.details_felt_loc).text == self.how_felt

    @property
    def check_workout_perceived_effort(self):
        return self.find(locs.details_per_effort_loc).text.split('Effort ')[1] == f'{self.perceived_effort}'
