import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    # 初始化 setUp
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.31.245/ciircrm")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_login(self):
        self.driver.find_element(By.NAME, "name").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("admins")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    # 结束，tearDown
    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()
    # 新建测试方法，用户名不存在
    def test_login_username_not_exist(self):
        driver = self.driver
        driver.find_element(By.NAME, "name").send_keys("admins") #输入用户名
        driver.find_element(By.NAME, "password").send_keys("admin")  #输入密码
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()    #点击登录
        # 获取登录提示信息
        msg = driver.find_element(By.CSS_SELECTOR,
                                  "body > div.container > div > div.span4 > div > form > fieldset > div").text
        print('msg:', msg)
        try:
            # 断言
            self.assertEqual(msg,"用户名或密码错误！")
            # 关闭提示框
            driver.find_element(By.CSS_SELECTOR,
                            "body > div.container > div > div.span4 > div > form > fieldset > div > button").click()
        except AssertionError:
            #截图
            driver.get_screenshot_as_file("/image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    # 新建测试方法，密码不能为空
    def test_login_passsword_not_error(self):
        driver = self.driver
        driver.find_element(By.NAME, "name").send_keys("admins")  # 输入用户名
        driver.find_element(By.NAME, "password").send_keys("admin")  # 输入密码
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()  # 点击登录
        # 获取登录提示信息
        msg = driver.find_element(By.CSS_SELECTOR,
                                  "body > div.container > div > div.span4 > div > form > fieldset > div").text
        print('msg:', msg)
        try:
            # 断言
            self.assertEqual(msg, "请正确输入用户名和密码！")
            # 关闭提示框
            driver.find_element(By.CSS_SELECTOR,
                                "body > div.container > div > div.span4 > div > form > fieldset > div > button").click()
        except AssertionError:
            # 截图
            driver.get_screenshot_as_file("/image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))