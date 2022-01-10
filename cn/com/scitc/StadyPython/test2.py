from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
wd = webdriver.Chrome()
wd.maximize_window()
wd.implicitly_wait(5)
wd.get('https://www.12306.cn')
wd.find_element(By.LINK_TEXT,'注册').click()
wd.find_element(By.ID,'userName').send_keys('ziming06085')
wd.find_element(By.NAME,'userDTO.password').send_keys('printf0608')
wd.find_element(By.NAME,'confirmPassWord').send_keys('printf0608')
eles = wd.find_elements(By.TAG_NAME,'input')
for i in eles:
    if i.get_attribute('name') == 'loginUserDTO.name':

        break
i.send_keys('刘龙')
