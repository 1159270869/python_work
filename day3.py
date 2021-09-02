import random

num = random.randint(0, 10000)
count = 0
money = 50000
d = {"root": "admin"}


while True:
    name = input("请输入您的用户名：")
    if name in d:
        password = input("请输入您的密码:")
        if d[name] == password:
            print('进入系统')
            break
        else:
            print('您输入的密码错误，请重新输入')
            continue
    else:
        print('您输入的用户名不正确，请重新输入')
        continue
while money >= 500:
    count = count + 1
    chose = input("输入猜的数字：")
    chose = int(chose)
    if chose > num:
        money = money - 500
        print("大了,你还剩", money, "金币")
        if money < 500:
            print("金额不足请充值")
    elif chose < num:
        money = money - 500
        print("小了，你还剩", money, "金币")
        if money < 500:
            print("金额不足请充值")
    else:
        money = money + 10000
        print("对了，本次数字是:", num, ",本轮总共输入", count, "次，奖励10000金币，还有", money, "金币")
        shifou = input("是否继续游戏：y/n:")
        if shifou == "y":
            continue
        elif shifou == "n":
            break