import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 登录
driver = webdriver.Chrome()
driver.get("http://192.168.31.245/ciircrm")
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(3)  # 等待时长3秒
driver.find_element(By.NAME, "name").send_keys("admins")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
# 获取登录提示信息
msg=driver.find_element(By.CSS_SELECTOR,"body > div.container > div > div.span4 > div > form > fieldset > div").text
print('msg:',msg)
# 断言
assert msg == "用户名或密码错误!"
# 关闭提示框
driver.find_element(By.CSS_SELECTOR,"body > div.container > div > div.span4 > div > form > fieldset > div > button").click()

# 关闭浏览器
time.sleep(5)
driver.quit()


















# 自动化后台管理系统
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/ul[2]/li[7]/a").click()  # 点击系统
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/ul[2]/li[7]/ul/li[4]/a").click()  # 个人资料
# driver.find_element(By.NAME, "email").send_keys("1873190160@qq.com")  # 邮箱输入
# driver.find_element(By.NAME, "telephone").send_keys("15108313187")  # 电话输入
# driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()  # 保存按钮
# driver.forward()#页面返回
# driver.find_element(By.CSS_SELECTOR,"body > div.container > div.row > div:nth-child(2) > form > table > tfoot > tr > "
#                                     "td:nth-child(2) > input:nth-child(2)").click()
#
# # 线索管理模块
#
#
# # driver.quit()
