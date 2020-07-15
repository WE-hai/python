from selenium import webdriver
import time
import os
dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('F:/比特/java-code/python/7-13/checkbox.html')
dr.get(file_path)
# 选择页面上所有的input，然后从中过滤出所有的checkbox 并勾选之
inputs = dr.find_elements_by_tag_name('input')
for input in inputs:
  if input.get_attribute('type') == 'checkbox':
     input.click()
time.sleep(2)
dr.quit()