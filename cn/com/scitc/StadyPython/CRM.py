import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://192.168.43.14/ciircrm")

# 登录
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(3)  # 等待时长3秒
driver.find_element(By.NAME, "name").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

# 添加客户
driver.find_element(By.LINK_TEXT,"创建客户").click()
driver.find_element(By.ID,"owner_name").click()
driver.find_element(By.XPATH,'//*[@id="d_content"]/tr[11]/td[1]/input').click()
driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(15) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1)").click()
driver.find_element(By.ID,"name").send_keys("王墓")
driver.find_element(By.ID,"industry").click()
driver.find_element(By.ID,"origin")
driver.find_element(By.XPATH,'//*[@id="origin"]/option[3]').click()
driver.find_element(By.ID,"ownership2").click()
driver.find_element(By.ID,"zip_code").send_keys("644000")
s =driver.find_element(By.ID,"annual_revenue")
Select(s).select_by_value("20-50万")
driver.find_element(By.ID,"rating2").click()
c1 = driver.find_element(By.NAME,"address['state']")
Select(c1).select_by_value("四川省")
c2 = driver.find_element(By.NAME,"address['city']")
Select(c2).select_by_value("宜宾市")
driver.find_element(By.NAME,"address['street']").send_keys("翠屏区金坪镇")
driver.find_element(By.NAME,"con_name").send_keys("刘子铭")
driver.find_element(By.NAME,"con_telephone").send_keys("13308133157")
y = driver.find_element(By.ID,"no_of_employees")
Select(y).select_by_value("50人以上")
driver.find_element(By.NAME,"create_business2").click()
driver.find_element(By.XPATH,'//*[@id="form1"]/table/tfoot/tr/td/input[2]').click()

# 创建商机
address_state = driver.find_element(By.NAME,"contract_address['state']")
Select(address_state).select_by_value("四川省")
address_citi = driver.find_element(By.NAME,"contract_address['city']")
Select(address_citi).select_by_value("广元市")
driver.find_element(By.NAME,"contract_address['street']").send_keys("利州区")
sj_type = driver.find_element(By.ID,"type")
Select(sj_type).select_by_value("新业务")
sj_origin = driver.find_element(By.ID,"origin")
Select(sj_origin).select_by_value("网络营销")
driver.find_element(By.ID,"gain_rate").send_keys("25")
driver.find_element(By.ID,"estimate_price").send_keys("80000000")
driver.find_element(By.XPATH,'//*[@id="form1"]/table/tfoot/tr/td/input[2]').click()

#回到商机首页
time.sleep(3)
driver.find_element(By.LINK_TEXT,"商机").click()
# 查看商机
time.sleep(3)
driver.find_element(By.LINK_TEXT,"查看").click()
# 删除商机
time.sleep(3)
driver.find_element(By.LINK_TEXT,"删除").click()

time.sleep(20)
driver.quit()

