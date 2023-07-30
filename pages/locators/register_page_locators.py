from selenium.webdriver.common.by import By


first_name_loc = (By.ID, "create_first")
last_name_loc = (By.ID, "create_last")
e_mail_loc = (By.ID, "create_email")
timezone_loc = (By.ID, "create_timezone")
passw_loc = (By.ID, "password_meter")
confirm_passw_loc = (By.ID, "create_passwordmatch")
create_button_loc = (By.CLASS_NAME, "btn-beoro-1")
password_error_loc = (By.CLASS_NAME, "alert-error")
missing_error_loc = (By.XPATH, "//label[@class='error']")
bar_loc = (By.CLASS_NAME, 'bar')
bar_text_loc = (By.CLASS_NAME, 'pwdText')
