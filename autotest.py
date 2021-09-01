from selenium.webdriver.common.action_chains import ActionChains
from urllib import request
from selenium import webdriver
import cv2
import random
import time
import pyautogui

##京东非登录搜索
# driver = webdriver.Firefox()
# driver.get("https://www.jd.com")
# driver.maximize_window()
# driver.find_element_by_id('key').send_keys("口罩")
# driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div/div[2]/button/i').click()
# driver.quit()


##京东滑动登录
# 获取图片信息，返回最佳匹配位置
# def findPic(target="img1.jpg", template="img2.png"):
#     # 读取图片
#     target_rgb = cv2.imread(target)
#     # 图片灰度化
#     target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
#     # 读取模块图片
#     template_rgb = cv2.imread(template, 0)
#     # 匹配模块位置
#     res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
#     # 获取最佳匹配位置
#     value = cv2.minMaxLoc(res)
#     # 返回最佳X坐标
#     return value[2][0]
# # 打开FireFox浏览器
# driver = webdriver.Firefox()
# driver.get("https://passport.jd.com/new/login.aspx")
# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
# driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('123456')
# driver.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('123456')
# driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
#
# while True:
#     try:
#         # 从网页上获取组件
#         target = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div[2]/div[1]/img')
#         template = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[1]/div[2]/div[2]/img')
#         # 获取模块的url路径
#         src1 = target.get_attribute("src")
#         src2 = template.get_attribute("src")
#         # 下载图片
#         request.urlretrieve(src1,"img1.jpg")
#         request.urlretrieve(src2,"img2.png")
#         x = findPic()
#         w1 = cv2.imread('img1.jpg').shape[1]
#         w2 = target.size['width']
#         x = x / w1 * w2
#         # 按钮坐标
#         offset_x,offset_y = 875,466
#         # pyautogui库操作鼠标指针
#         pyautogui.moveTo(offset_x,offset_y,duration=0.1 + random.uniform(0,0.1 + random.randint(1,100) / 100))
#         pyautogui.mouseDown()
#         offset_y += random.randint(9,19)
#         pyautogui.moveTo(offset_x + int(x * random.randint(15,25) / 20),offset_y,duration=0.28)
#         offset_y += random.randint(-9,0)
#         pyautogui.moveTo(offset_x + int(x * random.randint(17,23) / 20),offset_y,
#                          duration=random.randint(20,31) / 100)
#         offset_y += random.randint(0,8)
#         pyautogui.moveTo(offset_x + int(x * random.randint(19,21) / 20),offset_y,
#                          duration=random.randint(20,40) / 100)
#         offset_y += random.randint(-3,3)
#         pyautogui.moveTo(x + offset_x + random.randint(-3,3),offset_y,duration=0.5 + random.randint(-10,10) / 100)
#         offset_y += random.randint(-2,2)
#         pyautogui.moveTo(x + offset_x + random.randint(-2,2),offset_y,duration=0.5 + random.randint(-3,3) / 100)
#         pyautogui.mouseUp()
#         time.sleep(1)
#         result = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[4]/div[2]/div').text
#         if '不匹配' in result:
#             print("账户名密码不匹配!", result)
#             break
#     except:
#         print("异常!")
#         break




##淘宝非登录搜索
# driver = webdriver.Firefox()
# driver.get("https://www.taobao.com")
# driver.maximize_window()
# driver.find_element_by_id('q').send_keys("口罩")
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/form/div[1]/button').click()
# time.sleep(3)
# driver.quit()


##淘宝登录
# driver.find_element_by_id('fm-login-id').send_keys('123456')
# driver.find_element_by_id('fm-login-password').click()
# driver.find_element_by_id('fm-login-password').send_keys('123456')
# time.sleep(2)
# iframe=driver.find_element_by_tag_name("iframe")
# driver.switch_to_frame(iframe)
# ac=ActionChains(driver)
# ele = driver.find_element_by_xpath("//span[@id='nc_1_n1z']")
# ac.click_and_hold(ele).move_by_offset(258,0).perform()
# time.sleep(1)
# ac.release()
# driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/form/div[4]/button')



##企查查滑动
# driver=webdriver.Firefox()
# driver.get('https://www.qcc.com')
# driver.maximize_window()
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/header/div/ul/li[10]/a/span').click()
# time.sleep(3)
# ac=ActionChains(driver)
# ele=driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
#
# ac.click_and_hold(ele).move_by_offset(308,0).perform()
# ac.release()
