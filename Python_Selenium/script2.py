from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://www.saucedemo.com/")

print("The title of page is: ", browser.title)
print("The URL is: ", browser.current_url)
print("The Page source code is: ", browser.page_source)
browser.quit()