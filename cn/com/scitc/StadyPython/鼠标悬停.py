import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


wd = webdriver.Chrome()
wd.get('https://www.baidu.com')

# move=wd.find_element(By.XPATH,"//*[@id='s-top-left']/div/a")
# move=wd.find_element(By.NAME,"bj_briion").click()
wd.find_element(By.CSS_SELECTOR,"a.s-bri").click()
# ActionChains(wd).move_to_element(move).perform()

