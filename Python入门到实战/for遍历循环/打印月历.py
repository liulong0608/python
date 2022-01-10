# == Coding: UTF-8 ==
# @name             打印月历
# @version          1.0
# @author           -LIULONG
# @description      利用for遍历循环打印1997年7月的月历
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      2022年1月10日16:06:59
# ====/******/=====
"""
1.已知7月共31天
2.1997年7月的第一天是星期二
"""
day_of_week = 2  # 星期二

print("星期一\t星期二\t星期三\t星期四\t星期五\t星期六\t星期日")
print("\t\t" * (day_of_week - 1), end="")
for date in range(1, 32):
    if (date + day_of_week - 1) % 7 == 0:
        print(date)
    else:
        print(date, end="\t\t")
