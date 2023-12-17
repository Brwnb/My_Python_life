from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://demo.applitools.com/")

username = browser.find_element(By.ID, "username")
checkbox_remember_me = browser.find_element(By.XPATH, "//*[@type='checkbox']")

print(username.is_displayed())
assert username.is_displayed()

print(username.is_enabled())
assert username.is_enabled()

print(not checkbox_remember_me.is_selected())
assert not checkbox_remember_me.is_selected()
time.sleep(2)
checkbox_remember_me.click()

print(checkbox_remember_me.is_selected())
assert checkbox_remember_me.is_selected()

time.sleep(5)
browser.quit()