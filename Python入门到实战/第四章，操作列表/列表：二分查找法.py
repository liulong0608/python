# == Coding: UTF-8 ==
# @name             列表：二分查找法
# @version          1.0
# @author           -LIULONG
# @description      todo
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      2022年1月19日09:57:57
# ====/******/=====
"""
二分查找法：  （使用前提：列表已经按升序排列）
    基本原理：
        首先将要查找的元素与列表的中间元素比较
            1、如果元素小于中间元素，只需要在列表的前一半元素中继续查找
            2、如果元素和中间元素相等，匹配成功，直接结束
            3、如果元素大于中间元素，只需要在列表的后一半元素中继续查找元素
"""
# list_nums = [56,45,58,2,25,65,45,56,99,632,154,5,0,12]
import random

list_nums = []
for i in range(50):
    rand_nums = random.randint(1,101)
    while rand_nums in list_nums:
        rand_nums = random.randint(1, 101)
    list_nums.append(rand_nums)
list_nums.sort()    # sort() 列表元素升序
print(list_nums)
# 二分查找法
search_num = int(input("请输入要查找的数字："))
seach_index = -1
low = 0    # 最小边界的下标
high = len(list_nums) - 1   # 最大边界的下标
while high >= low:
    mid = (low + high) // 2     #中间元素
    if search_num < list_nums[mid]:
        high = mid - 1
    elif search_num == list_nums[mid]:
        seach_index = mid
        break
    else:
        low = mid + 1
print("要查找的元素下标为：",seach_index)