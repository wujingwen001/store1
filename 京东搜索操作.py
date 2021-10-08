'''
    任务：
        1：把所有页面操作使用自动化来做。
        2：自动化实现在京东搜索一个商品。
        3：在百度中做搜索操作。
'''

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# 导入驱动webdriver，即浏览器控制器
from selenium import webdriver
# 判断一个元素是否存在，如何判断alert弹窗出来了，如何判断动态的元素等等一系列的判断，
# 在selenium的expected_conditions模块收集了一系列的场景判断方法
from selenium.webdriver.support import expected_conditions as EC
# By是selenium中内置的一个class，在这个class中有各种方法来定位元素
from selenium.webdriver.common.by import By
# 设置浏览器驱动休眠等待，避免频繁操作封ip
from selenium.webdriver.support.ui import WebDriverWait

# 实例化一个用于控制Chrome的控制器(selenium还可以控制其他浏览器)
driver = webdriver.Chrome()
# 访问该网站
driver.get('https://www.jd.com')
# 窗口最大化，防止小弹窗阻挡
driver.maximize_window()

# 获取搜索输入框和搜索确认框
search_input = driver.find_element_by_id("key")
search_btn = driver.find_element_by_css_selector("#search button.button")

# 向搜索输入框内键入搜索内容，这里我们搜索“程序员”相关商品
search_input.send_keys("程序员")
# 点击搜索确认按钮
search_btn.click()


wait = WebDriverWait(driver, 10)
driver.close()








