from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 事件链

driver = webdriver.Chrome()

driver.get("https://www.taobao.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='q']").send_keys("牛仔裤")
driver.find_element_by_xpath("//*[@id='J_TSearchForm']/div[1]/button").click()

time.sleep(3)
driver.find_element_by_xpath("//*[@id='login']/div[2]/div/div[1]/a[1]").click()
driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("15837858336")
driver.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("824109@")
driver.find_element_by_xpath("//*[@id='login-form']/div[4]/button").click()


ac = ActionChains(driver)
ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")

ac.click_and_hold(ele).move_by_offset(42,0).perform() # perform执行

ac.release() # 释放
time.sleep(2)
