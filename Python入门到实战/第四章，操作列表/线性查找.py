# == Coding: UTF-8 ==
# @name              
# @version          1.0
# @author           -LIULONG
# @description      
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      
# ====/******/=====
import time

# list_names = ["刘","关","张"]
# search_name = input("请输入要查找的英雄名称：")
# search_index = -9999     # 用来记录查找到的英雄下标
# # 使用循环来线性查找
# for i in range(len(list_names)):
#     if search_name == list_names[i]:
#         search_index = i
#         break
# if search_index == -9999:
#     print("很遗憾，没有找到输入的英雄名称！请重试....")
# else:
#     print("{}的下标为：{}".format(search_name,search_index))

start = time.time()
lis = [x for x in range(10000000)]
for i in range(len(lis)):
    if lis[i] == lis[len(lis) - 1]:
        break
print("线性查找{}元素的列表共用时：{}".format(len(lis),time.time() - start))
