# 软件20-6    刘龙
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

wd = webdriver.Chrome()
wd.get("https://www.jd.com/")

wd.implicitly_wait(5)
move = wd.find_element(By.LINK_TEXT,"家用电器")
ActionChains(wd).move_to_element(move).perform()

wd.find_element(By.CSS_SELECTOR,"a.cate_detail_con_lk").click()

wd.switch_to.window(wd.window_handles[-1])
time.sleep(3)
wd.find_element(By.CSS_SELECTOR,"#brand-709010").click()
wd.find_element(By.XPATH,"//*[@id='J_selector']/div[1]/div/div[2]/div[1]/ul/li[4]/a").click()

mov = wd.find_element(By.CSS_SELECTOR,".ui-area-text")
ActionChains(wd).move_to_element(mov).perform()

# wd.find_element(By.CSS_SELECTOR,".ui-switchable-item ui-area-current").click()
wd.find_element(By.XPATH,'//*[@id="J_store_selector"]/div[2]/div[1]/a[2]/em').click()
wd.find_element(By.XPATH,"//*[@id='J_store_selector']/div[2]/div[2]/div[2]/ul/li[8]/a").click()
wd.find_element(By.XPATH,"//*[@id='J_store_selector']/div[2]/div[2]/div[3]/ul/li[4]/a").click()
wd.find_element(By.XPATH,"//*[@id='J_']")