"""
    页面对象层：
        页面对象编写技巧：
            类名：使用大驼峰将模块名称抄进来，有下划线就去掉
            方法：根据业务需求将每个操作步骤单独封装成一个方法
            方法名：page_XXX
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class PageLogin:
    # 初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.31.245/ciircrm")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    # 输入用户名
    def page_input_username(self,username):
        self.driver.find_element(By.NAME, "name").send_keys(username)

    # 输入密码
    def page_input_password(self,pwd):
        self.driver.find_element(By.NAME, "password").send_keys(pwd)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    # 获取异常提示信息
    def page_get_text(self):
        return self.driver.find_element(By.CSS_SELECTOR,
                                  "body > div.container > div > div.span4 > div > form > fieldset > div").text

    # 点击提示框信息按钮
    def page_click_err_btn_X(self):
        self.driver.find_element(By.CSS_SELECTOR,
                            "body > div.container > div > div.span4 > div > form > fieldset > div > button").click()

    # 组装登陆方法给业务调用
    def page_login(self,username,pwd):
        self.page_input_username(username)
        self.page_input_password(pwd)
        self.page_click_login_btn()
        self.page_get_text()
        self.page_click_err_btn_X()