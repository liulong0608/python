# == Coding: UTF-8 ==
# @name             列表;选择排序
# @version          1.0
# @author           -LIULONG
# @description      todo
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      2022年1月19日11:02:39
# ====/******/=====
"""
选择排序：
    1、首先找到列表中的最小元素并将它和第一个元素交换
    2、找到剩余元素中值最小的元素并和剩余列表的第一个元素交换
    3、依次类推，直到只剩下一个元素
"""
import random

lst = [random.randint(1,100) for i in range(50)]
print("选择排序前：",lst)
for i in range(len(lst) - 1):
    min_index = i
    for j in range(i + 1,len(lst)):     # 内循环中求出剩下元素的最小值下标
        if lst[j] < lst[min_index]:
            min_index = j               # 如果某个元素比最小值还小，那么最小值下标就更新为j
    lst[i],lst[min_index] = lst[min_index],lst[i]
print("选择排序后：",lst)