from selenium.webdriver.common.by import By

current_date_loc = (By.CLASS_NAME, 'currentdatelink')
month_button_loc = (By.CLASS_NAME, 'fc-button-month')
month_name_loc = (By.ID, 'dpMonth')
today_day_loc = (By.CLASS_NAME, 'fc-today')
next_loc = (By.CLASS_NAME, 'cal_next')
previous_loc = (By.CLASS_NAME, 'cal_prev')
month_dropdown = (By.CLASS_NAME, 'fc-header-title')
year_loc = (By.XPATH, '(//th[@class="switch"])[215]')
next_year_loc = (By.XPATH, '(//th[@class="next"])[215]')
prev_year_loc = (By.XPATH, '(//th[@class="prev"])[215]')
months_loc = (By.XPATH, '//div[@class="datepicker-months"]/table/tbody/tr/td/span')
years_loc = (By.XPATH, '//div[@class="datepicker-years"]/table/tbody/tr/td/span')

