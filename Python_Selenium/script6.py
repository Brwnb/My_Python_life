
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.implicitly_wait(11)##  ATÉ determinado
browser.maximize_window()

browser.get("https://chercher.tech/practice/implicit-wait-example")
checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
assert checkbox.is_displayed()