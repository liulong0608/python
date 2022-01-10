# 自动化测试注册163邮箱
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# class REGISTER:
#     def __init__(self, user, pwd, phonenum):
#         self.user = user
#         self.pwd = pwd
#         self.phonenum = phonenum
#
#     def run(self):
#         driver = webdriver.Chrome()
#         driver.get("https://mail.163.com/register/index.htm?from=163mail&utm_source=163mail")
#
#         # 窗口最大化
#         # driver.maximize_window()
#         # driver.find_element(By.LINK_TEXT,"注册网易邮箱")
#         # driver.switch_to.window(driver.window_handles[-1])
#
#         driver.find_element(By.ID, "username").send_keys(self.user)
#         driver.find_element(By.ID, "password").send_keys(self.pwd)
#         driver.find_element(By.ID, "phone").send_keys("19198756208\n")
#
#         # checkbox = driver.find_element(By.XPATH, "//input[@id='service']").click()
#         # driver.find_element(By.CSS_SELECTOR,"div[class='custom-checkbox']").click()
#         driver.find_element(By.CSS_SELECTOR,"input#service").click()
#         # if checkbox.is_selected():
#         #     print("yes")
#         # else:
#         #     print("no")
#         driver.implicitly_wait(2)
#         # driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[4]/span").click()
#
#
# REGISTER(user='llong1130', pwd='system.0608', phonenum='19198756208').run()
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")

driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div/ul/li[7]/a[2]").click()

driver.find_element(By.ID, "username").send_keys("llong1130")
driver.find_element(By.ID, "password").send_keys("system.0608")
driver.find_element(By.ID, "phone").send_keys("19198756208")
driver.find_element().click
