from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
driver.maximize_window()    # 窗口最大化

driver.find_element(By.ID,"fromStationText").click()
driver.find_element(By.XPATH,"//li[@title='北京']").click()

driver.find_element(By.ID,"toStationText").click()
driver.find_element(By.XPATH,"//li[@data='SHH']").click()
elel=driver.find_element(By.ID,"train_date")
elel.clear()
elel.send_keys("2021-12-20")
driver.find_element(By.ID,"isHighDan").click()
driver.find_element(By.ID,"search_one").click()

#切换到新窗口
# mainwindow变量保存当前窗口的句柄
mainwindow = driver.current_window_handle
# 新打开的窗口总是句柄列表中的最后一个
driver.switch_to.window(driver.window_handles[-1])
driver.forward()#页面返回
driver.back()#页面刷新



driver.find_element(By.CSS_SELECTOR,"#qd_closeDefaultWarningWindowDialog_id").click()