# coding:utf-8

'''
dinghanhua获取验证码自动登录
'''

from selenium import webdriver
import time

import pymysql
#获取有效验证码import pymssql


def get_sms_code(mobile, pymssql=None):
    '''获取手机号最新的一条有效验证码'''
    with pymssql.connect(server='192.168.1.1',user='tester',password='111111',database='sms') as dbconnect:
        with dbconnect.cursor(as_dict=True) as cursor:
            cursor.execute("""SELECT TOP 1 SMS,CreateDate 
                            FROM SMSLog where mobile=%s
                            and  createdate > dateadd(minute,-10,GETDATE())
                            order by CreateDate desc""",mobile)   #获取当前时间前10分钟之内的验证码

            row = cursor.fetchone()
            if row:
                code = row['SMS'].split('：')[1][0:4] #截取短信中的验证码。您的验证码是：1234.10分钟内有效
                return code



url = 'http://testurl/' #环境地址
phone = 'phonenumber' #手机号

browser = webdriver.Chrome()
browser.get(url)

time.sleep(1)
browser.find_element_by_id('Phone').send_keys(phone) #输入手机号

code = get_sms_code(phone) #获取10分钟以内的验证码
if not code: #若不存在，则点击发送验证码，再获取验证码
    browser.find_element_by_id('btnsend').click() #点击发送验证码
    time.sleep(2)
    code = get_sms_code(phone)

browser.find_element_by_id('smsCode').send_keys(code) #输入验证码
browser.find_element_by_id('btnLogin').click() #点击登录