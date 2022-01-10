import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class YB:
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd


    def run(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yiban.cn/")

        driver.find_element(By.LINK_TEXT,"登 录").click()
        driver.find_element(By.ID,"account-txt").send_keys(self.user)
        driver.find_element(By.ID,"password-txt").send_keys(self.pwd)
        driver.find_element(By.CSS_SELECTOR,"#login-btn").click()











        time.sleep(20)
YB(user="19198756208",pwd="love0608").run()