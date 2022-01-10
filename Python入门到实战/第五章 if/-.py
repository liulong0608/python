"""
按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
创建一个至少包含5个用户名的列表，并将其命名为current_users 。
再创建一个包含5个用户名的列表，将其命名为new_users ，并确保其中有一两个用户名也包含在列表current_users 中。
遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指
出这个用户名未被使用。
确保比较时不区分大消息；换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN'
"""

current_users = ['sudan','John','libai','leo','vn']
new_users = ['lee','ruli','John','leo','deves','sudan']
# set1 = set(current_users)
# set2 = set(new_users)
# print(set1&set2)
# 同时遍历两个列表
# for i,j in zip(current_users,new_users):
#     print(i,j)

for i in current_users:
    for j in new_users:
        if i == j:
            iter = i = j
            print(iter)
        # else:
            # pass