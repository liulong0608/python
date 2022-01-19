# == Coding: UTF-8 ==
# @name             列表：字符串按拼音排序
# @version          1.0
# @author           -LIULONG
# @description      todo
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      2022年1月19日10:24:14
# ====/******/=====
"""
1、引入拼音模块xpinyin
2、通过模块中定义的函数，提取每个中文的拼音
3、按照拼音排序
"""
from xpinyin import Pinyin
list_nums = ["刘备","关羽","张飞","孙权","曹操","周瑜","诸葛亮"]
list_result = []        # 根据拼音排序后的结果列表
pinyin = Pinyin()       # 创建拼音工具对象
for name in list_nums:
    list_result.append([pinyin.get_pinyin(name),name])
# 单独取出name的值
# for i in range(len(list_result)):
#     list_result[i] = list_result[i][1]
print("排序前：",list_result)
list_result.sort()
print("排序后：",list_result)