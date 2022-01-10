
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

ele=driver.find_element(By.LINK_TEXT,"更多")
ActionChains(driver).move_to_element(ele).perform()
# driver.find_element(By.LINK_TEXT,"文库").click()
driver.find_element(By.CSS_SELECTOR,"#s-top-more > div.s-top-more-content.row-1.clearfix > a:nth-child(3) > div").click()

driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.CSS_SELECTOR,"#app > div.edit-subscription-dialog-wrapper.mod > div.edit-subscription-container > div.edit-subscription-content > div.btn-wrap > div:nth-child(2)").click()

driver.find_element(By)