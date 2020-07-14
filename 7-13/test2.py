from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("明星大侦探")
driver.find_element_by_id("su").submit()
driver.implicitly_wait(5)

#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)
#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)
#输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys("密室大逃脱 第二季")
driver.find_element_by_id("su").click()
time.sleep(3)

driver.find_element_by_id("kw").clear()
time.sleep(3)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(3)
driver.find_element_by_id("su").click()

driver.quit()