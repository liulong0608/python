# == Coding: UTF-8 ==
# @name             控制台版进度条
# @version          1.0
# @author           -LIULONG
# @description      利用time.time()函数打印进度条
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      2022年1月11日13:32:02
# ====/******/=====
import time

# for i in range(10):
#     print("\r"+"*" * (i + 1),end="")
#     time.sleep(1)
print("开始执行".center(100,"*"))
curr_time = time.time()
total_time = 0
for i in range(100):
    rect_solid = "■" * (i + 1)
    rect_hollow= "□" * (100 - i - 1)
    percent = (i + 1) / 100 * 100
    print("\r{:^3.0f}%【{}{}】".format(percent,rect_solid,rect_hollow),end="")

    time.sleep(0.1)