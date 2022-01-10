# test.py
# @effect：逆向输出字符串
# @Author：刘龙
# @Class：软件20-6班


# 自动化测试注册163邮箱
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://mail.163.com/register/index.htm?from=163mail&utm_source=163mail")

# 窗口最大化
 # driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"注册网易邮箱")
# driver.switch_to.window(driver.window_handles[-1])

driver.find_element(By.ID, "username").send_keys('llong10333')
driver.find_element(By.ID, "password").send_keys("qwertyui.3320")
driver.find_element(By.ID, "phone").send_keys("19198756208")

checkbox = driver.find_element(By.TAG_NAME,"span > i").click()
if checkbox.is_selected():
    print("yes")
else:
    print("no")


























# for i in range (计数值)
#     表达式
# for i in range(0,3):
#     print(i)
# n = 10
# for n in range(10,101):
#
#     print(n,end=" ")
#     n = n + 3

# file1 = open('data.txt','w')    #打开文件
# print(123,"456","hello",file=file1) #file参数指定输出
# file1.close()   #关闭文件


# x,y=36,6
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y)
# print(divmod(5,2))