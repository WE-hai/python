from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("密室大逃脱")
driver.find_element_by_id("su").click()
# context = driver.find_element_by_link_text("新闻").text
# print(context)
# driver.back()

js = "var q=document.documentElement.scrollTop=1000"
driver.execute_script(js)
time.sleep(5)
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)

time.sleep(3)

driver.quit()