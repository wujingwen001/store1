from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 事件链

driver = webdriver.Chrome()

driver.get("https://www.jd.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("thinkpad  e580")


driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()

time.sleep(3)


driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]").click()



# 切换窗口
# 获取浏览器所有的窗口句柄
data = driver.window_handles # ["s001","s002"]

# 切换具体窗口
driver.switch_to.window(data[1])
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()

#登录账户
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("15837858336")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("wjw240826")
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()

ac = ActionChains(driver)
# ele = driver.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
#
# ac.click_and_hold(ele).move_by_offset(198,0).perform() # perform执行
#
# ac.release() # 释放
# time.sleep(2)
#
# driver.quit()
# element = driver.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
# ActionChains(driver).click_and_hold(on_element=element).perform()
# ActionChains(driver).move_to_element_with_offset(to_element=element,yoffset=0).perform()
# ActionChains(driver).release(on_element=element).perform()
# time.sleep(3)
s2 = r'//div/div[@class="JDJRV-bigimg"]/img'# 用于找到登录图片的大图
s3 = r'//div/div[@class="JDJRV-smallimg"]/img'# 用来找到登录图片的小滑块
bigimg = driver.find_element_by_xpath(s2).get_attribute("src")
smallimg = driver.find_element_by_xpath(s3).get_attribute("src")
# print(smallimg + '\n')
# print(bigimg)
# 背景大图命名
backimg = "backimg.png"
# 滑块命名
slideimg = "slideimg.png"
# 下载背景大图保存到本地
request.urlretrieve(bigimg, backimg)
# 下载滑块保存到本地
request.urlretrieve(smallimg, slideimg)
# 获取图片并灰度化
block = cv2.imread(slideimg, 0)
template = cv2.imread(backimg, 0)
# 二值化后的图片名称
blockName = "block.jpg"
templateName = "template.jpg"
# 将二值化后的图片进行保存
cv2.imwrite(blockName, block)
cv2.imwrite(templateName, template)
block = cv2.imread(blockName)
block = cv2.cvtColor(block, cv2.COLOR_RGB2GRAY)
block = abs(255 - block)
cv2.imwrite(blockName, block)
block = cv2.imread(blockName)
template = cv2.imread(templateName)
# 获取偏移量
result = cv2.matchTemplate(block, template, cv2.TM_CCOEFF_NORMED)  # 查找block在template中的位置，返回result是一个矩阵，是每个点的匹配结果
x, y = np.unravel_index(result.argmax(), result.shape)
# print("x方向的偏移", int(y * 0.4 + 18), 'x:', x, 'y:', y)
# 获取滑块
element = brower.find_element_by_xpath(s3)
ActionChains(brower).click_and_hold(on_element=element).perform()
ActionChains(brower).move_to_element_with_offset(to_element=element, xoffset=y, yoffset=0).perform()
ActionChains(brower).release(on_element=element).perform()
time.sleep(3)









