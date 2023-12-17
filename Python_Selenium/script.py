from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("https://google.com")
browser.maximize_window()
time.sleep(2)
browser.refresh()
time.sleep(2)
browser.get("https://www.saucedemo.com/")
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
browser.switch_to.new_window("tab")
time.sleep(2)
#browser.close()
#time.sleep(2)
browser.switch_to.new_window("tab")
time.sleep(2)
browser.quit()