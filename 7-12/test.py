from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()

# driver.find_element_by_partial_link_text("新").click()

# driver.find_element_by_xpath("//*[@id='kw']").send_keys("密室大逃脱第二季")
# driver.find_element_by_xpath("//*[@id='su']").click()

# driver.find_element_by_id("kw").send_keys("密室大逃脱")
# driver.find_element_by_id("su").click()

driver.find_element_by_css_selector("#kw").send_keys("明星大侦探")
driver.find_element_by_css_selector("#su").click()

time.sleep(10)

driver.quit()