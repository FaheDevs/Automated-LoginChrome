from selenium import webdriver

# create a new Chrome browser instance
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)

# navigate to the login page
driver.get("http://example.com/login")

# locate the email and password fields by their name attribute
email_field = driver.find_element_by_name("email")
password_field = driver.find_element_by_name("password")

# enter your email and password
email_field.send_keys("your_email@example.com")
password_field.send_keys("your_password")

# locate the login button and click it
login_button = driver.find_element_by_name("login_button")
login_button.click()

# close browser
driver.quit()


