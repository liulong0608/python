import random
import time

import pygame

# pygame.mixer.init()
# music_path = 'music/KOF.mp3'
# pygame.mixer.music.load(music_path.encode("UTF-8"))#加载背景音乐
# pygame.mixer.music.set_volume(0.5)#设置音量
# pygame.mixer.music.play(-1,0)#循环播放
#
#
# input()

name_player1 = name_player2 = ''  # 名字
hp_player1 = hp_player2 = 100  # 生命值
attack_player1 = attack_player2 = 0  # 攻击力
choice = ""  # 玩家对菜单项的选择

print("欢迎加入拳皇游戏".center(72, '*'))
print("\t请选择您的角色：1-草稚京\t2-八神庵")
choice = input("请输入您的选择：")
if choice == '1':
    name_player1 = "草稚京"
    name_player2 = "八神庵"
else:
    name_player1, name_player2 = "八神庵", "草稚京"
print("\t\t{}   VS.   {}".format(name_player1,name_player2))

# 开始对战
while hp_player1 > 0 or hp_player2 > 0:
    num_rand = random.randint(1,100)
    if num_rand % 2 == 1:
        attack_player1 = random.randint(5,15)
        hp_player2 -= attack_player1    #玩家2掉的血量 = 玩家2 原来的血量 - 玩家1的攻击力
        print("{}被攻击，吐了{}两血！！".format(name_player2,attack_player1))
        time.sleep(0.2)
        attack_player2 = random.randint(5,15)
        hp_player1 -= attack_player2
        print("{}被攻击，吐了{}两血！！".format(name_player1,attack_player2))
        time.sleep(0.5)
    else:
        attack_player2 = random.randint(5,15)
        hp_player1 -= attack_player2
        print("{}被攻击，吐了{}两血！！".format(name_player1,attack_player2))
        time.sleep(0.2)
        attack_player1 = random.randint(5, 15)
        hp_player2 -= attack_player1  # 玩家2掉的血量 = 玩家2 原来的血量 - 玩家1的攻击力
        print("{}被攻击，吐了{}两血！！".format(name_player2, attack_player1))
        time.sleep(0.5)
print("对战结果：")
if hp_player1 <= 0 and hp_player2 <= 0:
    print("双方KO！平局")
elif hp_player1 <= 0 and hp_player2 > 0:
    print("{}胜利！".format(name_player2))
else:
    print("{}胜利！！".format(name_player1))