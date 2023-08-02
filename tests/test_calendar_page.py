import pytest
from pages.calendar_page import CalendarPage
from time import sleep


def test_current_date_on_top_bar(driver, check_user_is_logged):
    calendar_page = CalendarPage(driver)
    calendar_page.open_page()
    assert calendar_page.check_current_date_on_top_bar()


class TestNavigationInCalendar:

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

    @pytest.mark.parametrize(
        'month',
        range(1, 13)
    )
    def test_switching_month_using_name(self, driver, check_user_is_logged, month):
        calendar_page = CalendarPage(driver)
        calendar_page.open_page()
        calendar_page.click_month_button()
        calendar_page.click_month(month)
        return calendar_page.check_current_month_name_in_calendar()
