import time

guests = ['mama','wife','刘晚凝']
print("本次宴会邀请的嘉宾是"+guests[0]+","+guests[1]+","+guests[2]+"!")
print("本次宴会无法到来的是"+guests[2])
son=guests.pop(2)
print(guests)
revamp_guests = guests.insert(3,'刘子铭')
print(guests)
time.sleep(3)
print("咦，发现了一个更大的桌子，这下可以邀请更多嘉宾了")
time.sleep(2)
print("你还想邀请谁？")
Rm_guests = []
print(type(Rm_guests))
welcom = input("：")
Rm_guests.append(welcom)

print("确定嘉宾都是他们吗？",Rm_guests)
choose = input("请输入y/x")
if choose =='y':
    print("本次邀请的嘉宾是",guests,Rm_guests)
else:
    w=input(":")