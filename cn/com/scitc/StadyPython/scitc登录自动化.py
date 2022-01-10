import time

from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Chrome()
wd.get('http://www.scitc.com.cn/')
# wd.get('http://scitc.fanya.chaoxing.com/portal')
# wd.get('https://passport2.chaoxing.com/login?loginType=4&newversion=true&fid=3012&newversion=true&refer=http://i.mooc.chaoxing.com')

jxpt_button=wd.find_element(By.XPATH,"//img[@src='/images/cloud.png']")
jxpt_button.click()

wd.implicitly_wait(10)

#我们依次获取wd.window_handles里面的所有句柄 对象，并且调用wd,swithch_to.window(handle)方法，切入到每个窗口
#然后检查里面该窗口对象的属性（可以是标题栏、地址栏），再加个判断，是不是我们要操作的窗口，如果是，跳出循环
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if '网络教学' in wd.title:
        break

dl=wd.find_element(By.XPATH,"//input[@value='登录' and @class='loginSub']")
dl.click()

input_id=wd.find_element(By.ID,'phone')
input_pwd=wd.find_element(By.ID,'pwd')
time.sleep(3)
input_id.send_keys("19198756208")
time.sleep(3)
input_pwd.send_keys("love0608")
time.sleep(3)
cx_dl=wd.find_element(By.ID,'phoneLoginBtn').click()

wd.switch_to.frame("frame_content")
wd.implicitly_wait(3)

#单击python B
wd.find_element(By.XPATH,"//*[@id='course_214910685_45340691']/div[2]/h3/a/span").click()

# 窗口切换
wd.switch_to.window(wd.window_handles[-1])


#点击讨论
wd.find_element(By.CSS_SELECTOR,"#boxscrollleft > div > ul:nth-child(16) > li:nth-child(3) > a").click()
# 切换frame
wd.implicitly_wait(3)
wd.switch_to.frame("frame_content-tl")

wd.find_element(By.XPATH,"//*[@id='topicId_327177042']/div[3]/div").click()
#窗口切换

wd.switch_to.window(wd.window_handles[-1])

# 回复
wd.find_element(By.XPATH,"//*[@id='subPageMain']/div[3]/div[2]/div/div[1]/textarea").send_keys("20301161 刘龙")

# 点击回复
wd.find_element(By.XPATH,"//*[@id='subPageMain']/div[3]/div[2]/div/div[4]/div[5]").click()



time.sleep(20)
wd.quit()   #退出