# == Coding: UTF-8 ==
# @name             菜单
# @version          1.0
# @author           -LIULONG
# @description      总菜单
# @GiteeWarehouse   https://gitee.com/liu-long068/python
# @editsession      
# ====/******/=====
#菜单
def select():
    print('宿舍管理系统')
    print('-------------------------------')
    print('1.学生信息')
    print('2.公寓楼信息')
    print('3.宿管信息')
    print('4.水电费信息')
    print('5.评分信息')
    print('6.毕业表信息插入')
    print('7.结束')
    print('-------------------------------')
    i = int(input('请输入你需要操作的编号:'))
    if i == 1:
        in_stu()
    elif i == 2:
        in_flat()
    elif i == 3:
        in_man()
    elif i == 4:
        cost()
    elif i == 5:
        score()
    elif i == 6:
        gra()
    elif i == 7:
        print('结束')