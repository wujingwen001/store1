
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
#点击登录链接
time.sleep(5)

driver.find_element_by_css_selector('#kw').clear()
driver.find_element_by_css_selector('#kw').send_keys('www.jd.com')


driver.find_element_by_xpath("//*[@id='su']").click()


time.sleep(3)
driver.close()