from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.4399.com/")
driver.find_element(By.LINK_TEXT,"登录").click()
# 登录框元素
element = driver.find_element(By.ID,"popup_login_frame")
element.screenshot("a.png")     # 截取

# 进入新界面
driver.switch_to.frame("popup_login_frame")

# 验证码元素
y_element = driver.find_element("//*[@id='captcha']")
# 获取验证码图片的坐标和长宽
print(y_element.location)   # 获取坐标
print (y_element.size)      # 获取长宽
left = y_element.location['x']
top =y_element.location['y']
right = left + y_element.size['width']
bottom = right + y_element.size['height']
im = Image.open("a.png")
im = im.crop((left,top,right,bottom))
im.save("b.png")
code = input("请输入正确的验证码：")
driver.find_element(By.XPATH,"//*[@id='inputCaptcha']").send_keys(code)
driver.find_element(By.XPATH,"//*[@id='login_form']/fieldset/div[6]/input").click()
