# == Coding: UTF-8 ==
# @name              列表：模拟洗牌
# @version          1.0
# @author           -LIULONG
# @description      
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      
# ====/******/=====
# 生产52个元素
import random

cards = [card for card in range(52)]
types = ["♠","♥","♦","♣"]
values = ["A"]
values += [str(value) for value in range(2,11)]
values += ["J","Q","K"]
# print(cards[24])
# print(types[cards[24] // 13])   # 元素24对应红心
# print(values[cards[24] % 13])
random.shuffle(cards)   # 洗牌
for i in range(len(cards)):
    type = types[cards[i] // 13]
    value = values[cards[i] % 13]
    print("[{}]:{}-{:6}".format(cards[i],type,value),end="")
    if (i + 1) % 13 == 0:
        print()
    else:
        print(end="\t")