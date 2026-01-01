""" 用Python设计第一个游戏 """

temp = input("不妨猜一下abobb现在心里想的是哪个数字：")
guess = int(temp)

if guess == 8:
    print("你是abobb心里的蛔虫吗？！")
    print("哼，猜中了也没有奖励！")
else:
    print("猜错了，abobb现在心里想的是8！")

print("游戏结束，不玩啦~")