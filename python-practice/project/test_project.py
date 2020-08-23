from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8081/ses/public/index.html")
driver.find_element_by_xpath("//*[@id='login_form']/div[2]/div/input").send_keys("abc")
driver.find_element_by_xpath("//*[@id='login_form']/div[3]/div/input").send_keys("123")
driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
driver.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='main_fail_modal_dialog']/div/div[3]/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='exam_record_tab']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_add']").click()

driver.quit()