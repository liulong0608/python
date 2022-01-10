# 打开百度，输入“自动化测试”，点击百度一下完成搜索
# 文本框id：kw      百度一下id：su
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
input_keywords = input("请输入搜索关键字：")
class test:

    def __init__(self,keywords):
        self.keywords = keywords

    def run(self):

        # 搜索框id：sb_form-q           搜索一下id：sb_form_go
        driver=webdriver.Chrome()
        driver.get('https:cn.bing.com')
        driver.maximize_window()
        # wd.find_elements(By.id,'sb_form_q')
        driver.find_element(By.ID,'sb_form_q').send_keys(self.keywords)
        driver.find_element(By.ID,'search_icon').click()

        time.sleep(10)
        driver.quit()
test(keywords=input_keywords).run()

