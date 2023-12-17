

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.saucedemo.com/")

#username = browser.find_element(By.ID, "user-name")
#password = browser.find_element(By.ID, "password")

#username.send_keys("standard_user")
#password.send_keys("secret_sauce")
auth_fields = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")
auth_fields.send_keys
time.sleep(5)
browser.quit()