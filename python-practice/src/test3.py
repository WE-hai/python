from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("F:\\比特\\java-code\\python\\python-practice\\html\\drop_down.html")
driver.get(file_path)

driver.find_element_by_xpath("//*[@value='8.34']")
# lists = driver.find_element_by_tag_name("option")
# for list in lists:
#     if list.get_ottribute('value') == "10.69" :
#         list.click()
# lists[5].click()

time.sleep(6)
driver.quit()
