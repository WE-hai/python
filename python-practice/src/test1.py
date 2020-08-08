from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("F:\\比特\\java-code\\python\\python-practice\\html\\frame.html")
driver.get(file_path)
time.sleep(10)
# 先找到
driver.switch_to.frame("f1")

driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("密室大逃脱")
driver.find_element_by_id("su").click()
time.sleep(10)

driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
time.sleep(10)

driver.quit()