import allure
import pytest
from pages.calendar_page import CalendarPage


@allure.feature('Navigation in the Calendar')
class TestNavigationInCalendar:

    def test_current_date(self, driver, check_user_is_logged):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        assert calendar_page.check_current_date_on_top_bar()

    def test_month_mode_of_calendar(self, driver, check_user_is_logged):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_month_button()
        assert calendar_page.check_current_month_name_in_calendar()
        assert calendar_page.check_current_day_in_calendar()

    def test_switching_to_the_next_month_using_arrow(self, driver, check_user_is_logged):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_month_button()
        calendar_page.switch_to_the_next_month()
        assert calendar_page.check_next_month_is_displayed

    def test_switching_to_the_previous_month_using_arrow(self, driver, check_user_is_logged):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_month_button()
        calendar_page.switch_to_the_previous_month()
        assert calendar_page.check_previous_month_is_displayed

    @allure.story('Switching to the necessary month selecting in in the calendar')
    @pytest.mark.parametrize(
        'month',
        range(1, 13)
    )
    def test_switching_month_using_name(self, driver, check_user_is_logged, month):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_month_button()
        calendar_page.select_month(month)
        assert calendar_page.check_correct_month_is_displayed(month)

    def test_switching_to_the_next_year_using_arrow(self, driver, check_user_is_logged):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_month_button()
        calendar_page.switch_to_the_next_year()
        calendar_page.select_month(1)
        assert calendar_page.check_next_year_is_displayed

    def test_switching_to_the_previous_year_using_arrow(self, driver, check_user_is_logged):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_month_button()
        calendar_page.switch_to_the_previous_year()
        calendar_page.select_month(1)
        assert calendar_page.check_previous_year_is_displayed

    @allure.story('Switching to the necessary year selecting it in the calendar')
    @pytest.mark.parametrize(
        'year',
        list(range(2020, 2030))
    )
    def test_switching_year_using_name(self, driver, check_user_is_logged, year):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_month_button()
        calendar_page.click_year()
        calendar_page.select_year(year)
        calendar_page.select_month(1)
        assert calendar_page.check_correct_year_is_displayed(year)


@allure.feature('Adding Workout using Quick Add')
class TestWorkoutQuickAdd:

    def test_filling_workout_quick_add_form(self, driver, check_user_is_logged, delete_workouts):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.fill_in_the_date_field(calendar_page.date_field_data)
        calendar_page.fill_in_the_time_field(calendar_page.time_field_data)
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.fill_in_the_workout_name_field(calendar_page.workout_name_data)
        calendar_page.fill_in_the_workout_description_field(calendar_page.workout_desc_data)
        calendar_page.fill_in_the_distance_field(calendar_page.distance)
        calendar_page.select_distance_type(0)
        calendar_page.fill_in_the_duration_field(calendar_page.duration)
        calendar_page.select_how_felt(calendar_page.how_felt)
        calendar_page.select_perceived_effort(calendar_page.perceived_effort)
        calendar_page.fill_in_the_post_notes(calendar_page.post_notes)
        calendar_page.click_add_workout_button()
        assert calendar_page.check_workout_is_created
        calendar_page.view_workout_details()
        assert calendar_page.check_workout_date_is_correct
        assert calendar_page.check_workout_time_start_is_correct
        assert calendar_page.check_activity_type_data_is_correct
        assert calendar_page.check_workout_name_is_correct
        assert calendar_page.check_workout_description_is_correct
        assert calendar_page.check_workout_distance_is_correct(0)
        assert calendar_page.check_workout_duration_is_correct
        assert calendar_page.check_workout_pace_is_correct
        assert calendar_page.check_workout_how_felt_is_correct
        assert calendar_page.check_workout_perceived_effort

    def test_show_planned_distance_duration_option(self, driver, check_user_is_logged, delete_workouts):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_distance(calendar_page.planned_distance)
        calendar_page.select_planned_distance_type(0)
        calendar_page.fill_in_the_planned_duration(calendar_page.planned_duration)
        calendar_page.click_add_workout_button()
        calendar_page.view_workout_details()
        assert calendar_page.check_planned_distance_and_duration_correct(0)

    def test_mark_as_race_option(self, driver, check_user_is_logged, delete_workouts):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_as_race()
        calendar_page.fill_in_the_overall_place_field(calendar_page.overall_place)
        calendar_page.fill_in_the_age_group_place_field(calendar_page.group_place)
        calendar_page.click_add_workout_button()
        calendar_page.view_workout_details()
        assert calendar_page.check_race_results

    def test_save_to_library_option(self, driver, check_user_is_logged, delete_workouts):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.fill_in_the_workout_name_field(calendar_page.workout_name_data)
        calendar_page.mark_save_to_lib_option()
        calendar_page.click_add_workout_button()
        assert calendar_page.save_to_lib_success_alert.is_displayed()

    def test_save_to_library_option_without_filling_required_data(self, driver, check_user_is_logged):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_save_to_lib_option()
        calendar_page.click_add_workout_button()
        assert calendar_page.error.is_displayed()


@allure.feature('Completion Option')
class TestCompletionOption:

    @allure.story('Workout color with default completion settings')
    @pytest.mark.parametrize(
        'planned_duration, duration',
        [('30', '24'), ('30', '36')]
    )
    def test_default_green_completion(self, driver, check_user_is_logged, delete_workouts, planned_duration, duration):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_duration(planned_duration)
        calendar_page.fill_in_the_duration_field(duration)
        calendar_page.click_add_workout_button()
        calendar_page.set_completion_settings(calendar_page.completion_default_settings)
        calendar_page.update_workout_completion()
        assert calendar_page.check_completion_is_green

    @allure.story('Workout color with default completion settings')
    @pytest.mark.parametrize(
        'planned_duration, duration',
        [('30', '14'), ('30', '46')]
    )
    def test_default_red_completion(self, driver, check_user_is_logged, delete_workouts, planned_duration, duration):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_duration(planned_duration)
        calendar_page.fill_in_the_duration_field(duration)
        calendar_page.click_add_workout_button()
        calendar_page.set_completion_settings(calendar_page.completion_default_settings)
        calendar_page.update_workout_completion()
        assert calendar_page.check_completion_is_red

    @allure.story('Workout color with default completion settings')
    @pytest.mark.parametrize(
        'planned_duration, duration',
        [('30', '15'), ('30', '23'), ('30', '37'), ('30', '45')]
    )
    def test_default_yellow_completion(self, driver, check_user_is_logged, delete_workouts, planned_duration, duration):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_duration(planned_duration)
        calendar_page.fill_in_the_duration_field(duration)
        calendar_page.click_add_workout_button()
        calendar_page.set_completion_settings(calendar_page.completion_default_settings)
        calendar_page.update_workout_completion()
        assert calendar_page.check_completion_is_yellow

    @allure.story('Workout color with default completion settings')
    def test_grey_completion(self, driver, check_user_is_logged, delete_workouts):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.click_add_workout_button()
        assert calendar_page.check_completion_is_grey

    def test_completion_when_duration_and_distance_are_filled(self, driver, check_user_is_logged, delete_workouts):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_duration('50')
        calendar_page.fill_in_the_duration_field('50')
        calendar_page.fill_in_the_planned_distance('50')
        calendar_page.fill_in_the_distance_field('10')
        calendar_page.click_add_workout_button()
        calendar_page.set_completion_settings(calendar_page.completion_default_settings)
        calendar_page.update_workout_completion()
        assert calendar_page.check_completion_is_green

    def test_completion_when_distance_is_filled(self, driver, check_user_is_logged, delete_workouts):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_distance('50')
        calendar_page.fill_in_the_distance_field('10')
        calendar_page.click_add_workout_button()
        calendar_page.set_completion_settings(calendar_page.completion_default_settings)
        calendar_page.update_workout_completion()
        assert calendar_page.check_completion_is_red

    @allure.story('Workout color with user completion settings')
    @pytest.mark.parametrize(
        'planned_duration, duration',
        [('30', '27'), ('30', '33')]
    )
    def test_user_green_completion(self, driver, check_user_is_logged, delete_workouts, planned_duration, duration):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_duration(planned_duration)
        calendar_page.fill_in_the_duration_field(duration)
        calendar_page.click_add_workout_button()
        calendar_page.set_completion_settings(calendar_page.completion_user_settings)
        assert calendar_page.check_yellow_range_was_changed(calendar_page.completion_user_settings)
        calendar_page.update_workout_completion()
        assert calendar_page.check_completion_is_green

    @allure.story('Workout color with user completion settings')
    @pytest.mark.parametrize(
        'planned_duration, duration',
        [('30', '24'), ('30', '26'), ('30', '34'), ('30', '60')]
    )
    def test_user_yellow_completion(self, driver, check_user_is_logged, delete_workouts, planned_duration, duration):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_duration(planned_duration)
        calendar_page.fill_in_the_duration_field(duration)
        calendar_page.click_add_workout_button()
        calendar_page.set_completion_settings(calendar_page.completion_user_settings)
        assert calendar_page.check_red_range_was_changed(calendar_page.completion_user_settings)
        calendar_page.update_workout_completion()
        assert calendar_page.check_completion_is_yellow

    @allure.story('Workout color with user completion settings')
    @pytest.mark.parametrize(
        'planned_duration, duration',
        [('30', '23'), ('30', '61')]
    )
    def test_user_red_completion(self, driver, check_user_is_logged, delete_workouts, planned_duration, duration):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.turn_on_completion_option()
        calendar_page.click_quick_add_button()
        calendar_page.wait_add_form_is_loaded()
        calendar_page.select_activity_type(calendar_page.activity_data)
        calendar_page.mark_show_planned_distance_checkbox()
        calendar_page.fill_in_the_planned_duration(planned_duration)
        calendar_page.fill_in_the_duration_field(duration)
        calendar_page.click_add_workout_button()
        calendar_page.set_completion_settings(calendar_page.completion_user_settings)
        calendar_page.update_workout_completion()
        assert calendar_page.check_completion_is_red
