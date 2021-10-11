from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains # 事件链

# driver = webdriver.Chrome()
# driver.get("http://localhost:8080/HKR/")
# driver.maximize_window()
#
# #第一步  登录名  真实姓名  密码 确认密码  下一步
# driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()
# driver.find_element_by_xpath("//*[@id='loginname']").send_keys("天宫2号")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("李四")
# driver.find_element_by_xpath("//*[@id='pwd']").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()
# time.sleep(3)
# #第二步 年龄 性别  测试开发
# driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("18")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys("女")
# driver.find_element_by_xpath("//*[@id='classname']").send_keys("测试开发")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
# time.sleep(3)
# #第三步  邮箱 电话号码  居住地址  下一步
# driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys("11223344@qq.com")
# driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys("15837858336")
# driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("北京市昌平区")
# driver.find_element_by_xpath("//*[@id='btn_reg']").click()
# time.sleep(3)
# driver.quit()
#重新用注册过的账号进行登录
driver = webdriver.Chrome()
driver.get("http://localhost:8080/HKR/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("天宫2号")
driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='submit']").click()
#修改头像，上传头像
driver.find_element_by_xpath("//*[@id='img']").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='ul_pic']/li[3]/img").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='file1']").send_keys(r"C:\Users\admin\Desktop\python课程\自动化测试\th.jpg")
driver.find_element_by_xpath("//*[@id='pic_btn']").click()
time.sleep(1)

#修改个人信息    名片   地址   按钮
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").send_keys("你好，欢迎来到我的世界")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").send_keys("河南平原示范区")
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").clear()
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys("38")
driver.find_element_by_xpath("//*[@id='btn_modify']").click()

time.sleep(2)

#查询所有好友
driver.find_element_by_xpath("//*[@id='_easyui_tree_10']/span[4]/a").click()
time.sleep(2)
#退出本账号
driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
time.sleep(2)
#登录Jason教师账号
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='submit']").click()

driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("乔越洋")
driver.find_element_by_xpath("//*[@id='search_user']/span/span[1]").click()
driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[9]/div/a").click()
time.sleep(3)

#学生的姓名和电话号码查询，设置毕业和未毕业状态
driver.find_element_by_xpath("//*[@id='_easyui_tree_12']/span[4]/a").click()
driver.find_element_by_xpath("//*[@id='J-stu']").send_keys("张三")
driver.find_element_by_xpath("//*[@id='J-phone']").send_keys("13403736782")
driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()
driver.find_element_by_xpath("") #设置毕业状态按钮
time.sleep(3)

#课程管理中，添加以及取消课程
driver.find_element_by_xpath("//*[@id='_easyui_tree_13']/span[4]/a").click()
driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span/span[1]").click()
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").send_keys("数据结构")
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").send_keys("数据的结构")
driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[1]/span").click() #添加课程按钮
driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[2]/span/span[1]").click() #取消课程按钮
time.sleep(3)
#查询评价
driver.find_element_by_xpath("//*[@id='J-xl']").send_keys("2021-09-01")
driver.find_element_by_xpath("//*[@id='eva']/div/div/div[1]/table/tbody/tr/td[2]/a/span/span[1]").click()
driver.find_element_by_xpath("//*[@id='eva']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()#导出今日评价
driver.find_element_by_xpath("//*[@id='_easyui_tree_16']/span[4]/a")#点击评价报表
#历史日志
driver.find_element_by_xpath("//*[@id='_easyui_tree_18']/span[4]/a").click()






