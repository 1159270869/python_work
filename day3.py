import random

num = random.randint(0, 10000)
count = 0
money = 50000
d = {"root": "admin"}


while True:
    name = input("�����������û�����")
    if name in d:
        password = input("��������������:")
        if d[name] == password:
            print('����ϵͳ')
            break
        else:
            print('������������������������')
            continue
    else:
        print('��������û�������ȷ������������')
        continue
while money >= 500:
    count = count + 1
    chose = input("����µ����֣�")
    chose = int(chose)
    if chose > num:
        money = money - 500
        print("����,�㻹ʣ", money, "���")
        if money < 500:
            print("�������ֵ")
    elif chose < num:
        money = money - 500
        print("С�ˣ��㻹ʣ", money, "���")
        if money < 500:
            print("�������ֵ")
    else:
        money = money + 10000
        print("���ˣ�����������:", num, ",�����ܹ�����", count, "�Σ�����10000��ң�����", money, "���")
        shifou = input("�Ƿ������Ϸ��y/n:")
        if shifou == "y":
            continue
        elif shifou == "n":
            break