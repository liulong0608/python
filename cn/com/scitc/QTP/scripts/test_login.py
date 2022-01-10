import unittest
from cn.com.scitc.QTP.page.page_login import PageLogin
from parameterized import parameterized

# 新建测试类
class TestLogin(unittest.TestCase):
    # 初始化
    def stUp(self):
        self.lofin = PageLogin()

    # 结束
    def tearDown(self):
        self.lofin.driver.quit()


    # 新建测试方法
    @parameterized.expand([("admins","admin","用户名或密码错误"),("admin","","请正确输入用户名或密码")])
    def test_login(self,username,pwd,expect):
        # 调用组装
        self.lofin.page_login(username,pwd)
        # 获取登录后的提示信息
        msg = self.login.page_get_text()
        try:
            self.assertEqual(msg,expect)
            # 点击登录提示框
            self.lofin.page_click_err_btn_X()
        expect AssertionError:
            pass