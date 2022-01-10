guests = ['mama','wife','刘晚凝']
print("本次宴会邀请的嘉宾是"+guests[0]+","+guests[1]+","+guests[2]+"!")
print("本次宴会无法到来的是"+guests[2])
son=guests.pop(2)
print(guests)
revamp_guests = guests.insert(3,'刘子铭')
print(guests)