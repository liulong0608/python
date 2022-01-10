money = eval(input("输入要兑换的钱数（支持一位小数）："))
part_int = int(money)
# part_float = (money - part_int) * 10
# 任何整数，如果模10，那么取的是某个整数的个位数
part_float = money * 10 % 10

paper_10 = part_int // 10
print("需要十元纸币：",paper_10,"张")
part_int %= 10
paper_5 = part_int // 5
print("需要五元纸币：",paper_5,"张")
paper_1 = part_int % 5
print("需要一元纸币：",paper_1,"张")
coin_5 = int(part_float // 5)
print("需要五角硬币：",coin_5,"枚")
