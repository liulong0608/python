from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

uanme=input("请输入用户名：")
pwd=input("请输入密码：")
# yzm=input("请输入验证码：")
class TPYZ:
    def __init__(self,uname,pwd,yzm):
        self.uname=uname
        self.pwd=pwd
        self.yzm=yzm

    def run(self):

        driver = webdriver.Chrome()
        driver.get("https://passport2.chaoxing.com/login?loginType=3&newversion=true&fid=3012&hidecompletephone=0&refer=https%3A%2F%2Fmooc1.chaoxing.com%2Fexam%2Ftest%2FreVersionPaperMarkContentNew%3FcourseId%3D214910685%26classId%3D45340691%26p%3D1%26id%3D49087855%26ut%3Ds%26examsystem%3D0%26cpi%3D164737175&accounttip=&pwdtip=")


        driver.find_element(By.ID,"uname").send_keys(uanme)
        driver.find_element(By.ID,"password").send_keys(pwd)

        # 登录框元素
        element = driver.find_element(By.CSS_SELECTOR,"body > div > div")
        element.screenshot("dlk.png")
        #验证码元素
        y_element = driver.find_element(By.ID,"numVerCode")
        # 获取验证码图片的坐标和长宽
        print(y_element.location)   # 坐标
        print(y_element.size)   # 长宽
        left = y_element.location['x']
        top = y_element.location['y']
        right = left+y_element.size['width']
        bottom = right+y_element.size['height']
        im = Image.open("dlk.png")
        im = im.crop((left,top,right,bottom))
        im.save("yzm.png")
        yzm = input("请输入验证码：")
        driver.find_element(By.ID,"vercode").send_keys(yzm)
        driver.find_element(By.ID,"loginBtn").click()
yzm=input("请输入验证码：")
TPYZ(uanme=uanme,pwd=pwd,yzm=yzm).run()