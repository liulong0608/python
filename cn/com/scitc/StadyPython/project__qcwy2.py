import time,csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
class Qcwy:
    def __init__(self,keyword,city,maxpagenum):
        self.keyword = keyword
        self.city = city
        self.maxpagenum = maxpagenum


    def run(self):
        # 启动浏览器
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https:www.51job.com")
# 1、搜索爬取关键字
        # 输入关键字
        driver.find_element(By.ID,"kwdselectid").send_keys(self.keyword)
        #选择城市
        driver.find_element(By.ID,"work_position_input").click()
        #前端代码或许有变化，等待1秒
        time.sleep(1)

        #选择城市，点击上方当前已经选中的城市，去掉这些
        selectedCityEles = driver.find_elements(By.CSS_SELECTOR,"#work_position_click_multiple_selected > span")
        for one in selectedCityEles:
            one.click()

        cityEles = driver.find_elements(By.CSS_SELECTOR,"#work_position_click_center_right_list_000000 em")

        #判断是否是我要找的城市cityEle.text==self.cityEles??，赋值给cityEle,跳出循环
        target = None
        for cityEle in cityEles:
            if cityEle.text == self.city:
                target = cityEle
                break
        #如果没找城市，则执行下一步在以字母开头的城市中寻找
            # .......（代码待完成）

        #没有找到该名称的城市
        if target is None:
            input(f'{self.city}不在热门城市列表，请手动点击选中城市后，按回车继续...')
        else:
            target.click()
        #选中城市后保存城市选择
        driver.find_element(By.CSS_SELECTOR,"#work_position_click_bottom_save").click()
        #点击搜索
        driver.find_element(By.CSS_SELECTOR,"div.ush > button").click()


        with open(f'前途无忧招聘_关键词_{self.keyword}_城市_{self.city}.csv',
                        'w',newline='',encoding='gbk') as f:
            f_csv=csv.DictWriter(f,
                                     ['职位名称',
                                      '发布时间',
                                      '薪资',
                                      '工作简介',
                                      '职位信息'])
            f_csv.writeheader()
            for pageNum in range(1, self.maxpagenum + 1):
                    # 设置页码
                    pageNumInput = driver.find_element(By.ID, "jump_page")
                    pageNumInput.clear()
                    pageNumInput.send_keys(str(pageNum))
                    driver.find_element(By.CSS_SELECTOR, "span.og_but").click()
                    #暂停一秒
                    time.sleep(1)

                    rows=self.handleOnepage(driver)
                    f_csv.writerows(rows)

                    #是否到了最后一页
                    if self.isLastPage(driver):
                        break
    # 是否到了最后一页
    def isLastPage(self,driver):
        #如果下一页是连接，表示还有下一页
        NextPageButton = driver.find_element(By.CSS_SELECTOR,"div.j_page li:last-child")
        driver.implicitly_wait(2)
        hasLink = NextPageButton.find_element(By.TAG_NAME,"a")
        driver.implicitly_wait(10)
        if hasLink: #不是最后一页
            return False
        else:
            return True


    def handleOnepage(self,driver):
        rows = []
        # 处理每页信息
        # jobs = driver.find_elements(By.CSS_SELECTOR,"j_joblist div[class=e]")
        jobs = driver.find_elements(By.XPATH, "//a[@class='el']")

        # print(jobs)
        for job in jobs:

            fields = job.find_elements(By.TAG_NAME,"span")
            stringFilelds = [field.text for field in fields]
            print(stringFilelds)

            data = {
                "职位名称":stringFilelds[0],
                "发布时间":stringFilelds[1],
                "薪资":stringFilelds[2],
                "工作简介":stringFilelds[3],
                # "职位信息":stringFilelds[4],
                # "公司信息":stringFilelds[5]
            }

            # 点击打开详细链接
            fields[1].click()

            # mainwindow变量保存当前窗口的句柄
            mainwindow = driver.current_window_handle
            # 新打开的窗口总是句柄列表中的最后一个
            driver.switch_to.window(driver.window_handles[-1])

            info = driver.find_elements(By.CSS_SELECTOR,".tCompany_main .job_msg")
            if info and len(info)==1:
                data["职位信息"] = info[0].text
            infogs = driver.find_elements(By.CSS_SELECTOR,".tCompany_main .tmsg")
            if infogs and len(infogs)==1:
                data["公司信息"] = infogs[0].text

            rows.append(data)
            # 关闭具体信息页
            driver.close()
        #     切换到原来窗口
            driver.switch_to.window(mainwindow)

        return rows

#创建实例
Qcwy(keyword='软件测试',city='成都',maxpagenum=1).run()
