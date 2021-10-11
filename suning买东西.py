from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 事件链

driver = webdriver.Chrome()

driver.get("https://www.suning.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("电饭煲")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

driver.find_element_by_xpath("//*[@id='美的Midea']/a/img")
time.sleep(1)

# 切换窗口
# 获取浏览器所有的窗口句柄
# data = driver.window_handles # ["s001","s002"]
#
# # 切换具体窗口
# driver.switch_to.window(data[1])
driver.find_element_by_xpath("//*[@id='0000000000-140381082']/div/div/div[3]/a[3]").click()
driver.find_element_by_xpath("/html/body/div[16]/div[2]/div[1]/div[2]/a/div/div/span[1]").click()
driver.find_element_by_xpath("//*[@id='myCart']/div[3]/div/a").click()
driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/a[1]").click()
driver.find_element_by_xpath("//*[@id='showErrorUsernameDiv']/label").send_keys("15837858336")
driver.find_element_by_xpath("//*[@id='showErrorPwdDiv']/label").send_keys("924u353552")


ac = ActionChains(driver)
ele = driver.find_element_by_xpath("//*[@id='dt_notice']")

ac.click_and_hold(ele).move_by_offset(330,0).perform() # perform执行

ac.release() # 释放
time.sleep(2)
#







ac = ActionChains(driver)
ele = driver.find_element_by_xpath("//*[@id='nc_1_n1z']")

ac.click_and_hold(ele).move_by_offset(42,0).perform() # perform执行

ac.release() # 释放
time.sleep(2)
