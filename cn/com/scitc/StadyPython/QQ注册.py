from selenium import webdriver
from selenium.webdriver.common.by import By
import pymysql
driver = webdriver.Chrome()
driver.get("https://ssl.zc.qq.com/v3/index-chs.html")

driver.find_element(By.ID,"nickname").send_keys("即将离开高速路口过")
driver.find_element(By.ID,"password").send_keys("system.0608")
driver.find_element(By.ID,"phone").send_keys("19198756208")

# 获取手机验证码

driver.find_element(By.CSS_SELECTOR,"label.checkbox").click()