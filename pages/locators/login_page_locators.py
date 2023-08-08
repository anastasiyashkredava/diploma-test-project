from selenium.webdriver.common.by import By

email_loc = (By.ID, 'login_name')
passw_loc = (By.ID, 'login_password')
login_button = (By.CLASS_NAME, 'submit_sect')
welcome_loc = (By.CLASS_NAME, 'user-info')
signup_loc = (By.CLASS_NAME, 'signup')
error_loc = (By.XPATH, "//label[@class='error']")
invalid_credentials_error = (By.CLASS_NAME, 'alert-error')
login_remember = (By.ID, 'login_remember')
logout_loc = (By.XPATH, '(//div[@class="user-info"]/ul/li)[3]')
