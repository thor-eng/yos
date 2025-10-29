from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome browser
driver = webdriver.Chrome()

# Open the running Flask app
driver.get("http://127.0.0.1:5000")

# Wait for the page to load
time.sleep(1)

# Fill the form
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")

# Click the login button
driver.find_element(By.ID, "login-btn").click()

# Wait to see the result
time.sleep(3)

# Print the page content
print(driver.page_source)

# Close the browser
driver.quit()
