# == Coding: UTF-8 ==
# @name             列表：冒泡排序
# @version          1.0
# @author           -LIULONG
# @description      todo
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      2022年1月19日10:53:09
# ====/******/=====
import random

lst = [random.randint(1,100) for i in range(100)]
# [94, 65, 88, 4, 48]
print("排序前：",lst)
for i in range(len(lst) -1):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j + 1] = lst[j + 1],lst[j]
print("排序后：",lst)