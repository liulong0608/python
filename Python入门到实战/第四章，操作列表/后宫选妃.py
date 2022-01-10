import time


def main():
    emp = input("请输入当前登基的皇帝名号：")
    print("******************************************************************")
    print("\n")
    print(emp+"皇帝登基，武运荣昌！吾皇万岁万岁万万岁！")
    print("\n")
    print("******************************************************************")


def choise():
    time.sleep(5)
    print("1、皇帝下旨选妃：\t\t")
    print("2、翻牌宠幸：\t\t")
    print("3、打入冷宫！\t\t")
    print("4、单独召见爱妃去小树林办点事情：")
    time.sleep(2)
    choise = eval(input("陛下请选择："))
    if choise == 1:
        print("选妃")
    elif choise == 2:
        print("宠幸")
    elif choise == 3:
        print("冷宫")
    elif choise == 4:
        print("单独召见")
"""
def function_1(value):
def function_2(value):

functions = {'a': function_1,
             'b': function_2,...}
func = functions[value]


functions = {
    'a': lambda x:function_1(x),
    ...
}


"""



main()
choise()