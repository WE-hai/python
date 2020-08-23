from selenium import webdriver
import time
import os

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("F:\\比特\\java-code\\python\\python-practice\\html\\level_locate.html")
driver.get(file_path)
driver.find_element_by_link_text("Link1").click()
elem = driver.find_element_by_link_text("Another action")
ActionChains(driver).move_to_element(elem).perform()
time.sleep(8)

driver.quit()