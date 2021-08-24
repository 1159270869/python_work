# account,username,password,country,province,street,door,money,bank_name
import random
from bbank import Bank
bank=Bank()
data=bank.data

class Action:
    def addUser(self):
        username = input("请输入用户名：")
        password = input("请输入你的密码：")
        country = input("请输入你的国家:")
        province = input("请输入省份：")
        street = input("请输入街道：")
        door = input("请输入门牌号：")

        li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "e", "f"]
        account = ""
        for i in range(8):
            index = random.randint(0, len(li) - 1)
            account = account + li[index]
        status = bank.bank_addUser(account,username, password, country, province, street, door)
        if status==1:
            print("恭喜开户成功！您的信息如下：")
            info='''
               ************个人信息***********
               账号：%s
               用户名：%s
               密码：******
               地址信息
                   国家：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
               余额：%s
               开户行：%s
               *****************************
               
                '''
            print(info % (account,username,country,province,street,door,0,bank.getBank_name()))

        if status ==2:
            print("该账户已经存在！")
        if status==3:
            print("数据已满，无法开户")
    def saveMoney(self):
        account =input("请输入你的账号：")
        password=input("请输入密码：")
        money=int(input("请输入存款金额："))
        status=bank.bank_saveMoney(account,password,money)
        if status==1:
            print("存款成功,你的账户余额为：",bank.data[account]["money"])
        if status==2:
            print("密码错误")
        if status==3:
            print("账号错误")

    def takeMoney(self):
        account = input("请输入你的账号：")
        password = input("请输入密码：")
        money = int(input("请输入取款金额："))
        status = bank.bank_takeMoney(account, password, money)
        if status == 1:
            print("取款成功")
        if status == 2:
            print("余额不足")
        if status == 3:
            print("密码错误")
        if status == 4:
            print("账号错误")
    def transfer(self):
        account1 = input("请输入你的账号：")
        account2 = input("请输入转入账号：")
        password = input("请输入你的密码：")
        money = int(input("请输入转账金额："))
        status = bank.bank_transfer(account1,account2,password, money)
        if status == 1:
            print("转账成功，你的账户余额为：",bank.data[account1]["money"])
        if status == 2:
            print("余额不足")
        if status == 3:
            print("密码错误")
        if status == 4:
            print("账号错误")
    def information(self):
        account=input("请输入账号：")
        password=input("请输入密码：")
        status=bank.bank_information(account,password)
        if status==1:
            pdata=bank.data[account]
            print("以下是你的个人信息\n")
            info='''
                ************个人信息***********
               账号：%s
               用户名：%s
               密码：******
               地址信息
                   国家：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
               余额：%s
               开户行：%s
               *****************************
            '''
            print(info % (account,pdata[0],pdata[2],pdata[3],pdata[4],pdata[5],pdata[6],bank.getBank_name()))
        if status==2:
            print("密码错误")
        if status==3:
            print("账号不存在")
    def welcome(self):
        print("---------------------------------")
        print("-     中国农业银行账户管理系统V1.0     -")
        print("---------------------------------")
        print("-   1.开户                       -")
        print("-   2.存钱                       -")
        print("-   3.取钱                       -")
        print("-   4.转账                       -")
        print("-   5.查询                       -")
        print("-   6.Bye!                       -")
        print("----------------------------------")