import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.xiaomi.cn/')
# time.sleep(5)
driver.find_element(By.ID,'area').click()   #单击登录按钮


driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR,"span.btnRight-QI7tQ").click()      #同意协议声明

# 输入账号
all_input=driver.find_element(By.NAME,'account')    #账号输入元素
pwd_input=driver.find_element(By.NAME,'password')   #密码输入元素
all_input.send_keys('1235504770')
pwd_input.send_keys('love0608')
#
# # time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"label.ant-checkbox-wrapper").click()    #勾选用户协议

# 登录
driver.find_element(By.CSS_SELECTOR,"button.mi-button").click()

