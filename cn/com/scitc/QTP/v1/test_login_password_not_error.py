import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 登录
driver = webdriver.Chrome()
driver.get("http://192.168.43.14/ciircrm")
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(3)  # 等待时长3秒
driver.find_element(By.NAME, "name").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
# 获取登录提示信息
msg=driver.find_element(By.CSS_SELECTOR,"body > div.container > div > div.span4 > div > form > fieldset > div").text
print('msg:',msg)
# 断言
assert msg == "请正确输入用户名和密码！"
# 关闭提示框
driver.find_element(By.CSS_SELECTOR,"body > div.container > div > div.span4 > div > form > fieldset > div > button").click()

# 关闭浏览器
time.sleep(5)
driver.quit()