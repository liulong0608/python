# 1.进入网站，网址：www.12306.cn
# 2.窗口最大化
# 3.使用find_element_by_link_text()定位到“注册”后单击
# 4. 使用find_element_by_id定位到用户名后发送要注册的用户名信息
# 5.使用find_element_by_name定位到登录密码后发送要使用的密码信息
# 6.使用find_elements_by_class_name定位到确认密码后发送确认密码信息
# 7.使用find_elements_by_tag_name定位到姓名发送本人信息
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
class ZC12306:
    def __init__(self,userName,pwd,Qpwd,name,IDcard,email,phoneNo):
        self.userName = userName
        self.pwd = pwd
        self.Qpwd = Qpwd
        self.name = name
        self.IDcard = IDcard
        self.email = email
        self.phoneNo = phoneNo
    # def Uinput(self):
    #     UuserName = input("请输入注册用户名：")
    #     Upwd = input("请输入注册密码：")
    #     UQpwd = input("请确认注册密码：")
    #     Uname = input("请输入注册姓名：")
    #     UIDcard = input("请输入注册人身份证号码：")
    #     Uemail = input("请输入注册邮箱：")
    #     Uphone = input("请输入注册手机号：")
    def run(self):
        driver = webdriver.Chrome()
        driver.get("https://www.12306.cn/index/")

        driver.maximize_window()   #窗口最大化

        driver.implicitly_wait(5)

        driver.find_element(By.LINK_TEXT,"注册").click()

        driver.find_element(By.ID,"userName").send_keys(self.userName)
        driver.find_element(By.NAME,"userDTO.password").send_keys(self.pwd)
        # driver.find_element(By.CSS_SELECTOR,"input#confirmPassWord").send_keys("printf0608")
        pwd_input = driver.find_elements(By.CLASS_NAME,"inptxt")
        for i in pwd_input:
            if i.get_attribute('id') == 'confirmPassWord':
                break
        i.send_keys(self.Qpwd)

        name_input=driver.find_elements(By.TAG_NAME,"input")
        for i in name_input:
            if i.get_attribute('name') == 'loginUserDTO.name':
                i.send_keys(self.name)


        driver.find_element(By.CSS_SELECTOR,"input#cardCode").send_keys(self.IDcard)

        driver.find_element(By.ID,"email").send_keys(self.email)

        driver.find_element(By.CSS_SELECTOR,"#mobileNo").send_keys(self.phoneNo)

        driver.find_element(By.CSS_SELECTOR,"#checkAgree").click()

        driver.find_element(By.LINK_TEXT,"下一步").click()

        time.sleep(10)
ZC12306(userName='qq1873190160',pwd='printf0608',Qpwd='printf0608',name='刘龙',IDcard='430426200006088878',email='1873190160@qq.com',phoneNo='19198756208').run()