'''
    ����
        �Ż�����С��
        10��е�����Ż�ȯ��0.5
        20�����������Ż�ȯ 0.3
        15��HUA WEI WATCH 0.8
        �����ȡһ���Ż�ȯ��


    �̳ǣ�
        1.׼��һЩ��Ʒ
        2.�пյĹ��ﳵ
        3.Ǯ��
        4.����
    ���̣�
        ��������Ĳ�Ʒ�治���ڣ�
            ������
                ��Ǯ���ˣ�
                    ����Ʒ��ӵ����ﳵ
                    Ǯ������ȥ��Ʒ��Ǯ
                ��Ǯ����
                    ��ܰ��
            ��������
                ��ܰ��ʾ��
            �Ƿ����룺
        �˳���
            ��ӡ����С��
'''
import copy
import random
import time
b = 1#��е����
c = 1#HUA WEI WATCH
d = 1#��������

shop = [
    ["lenovo PC",5600],
    ["HUA WEI WATCH",1200],
    ["Mac pro",12000],
    ["ϴ�»�",3000],
    ["��е����",5000],
    ["��������",4.5],
    ["�ϸ�������",20],
]

a=random.randint(0,44)

# 1.׼����Ǯ��

money = input("���������ĳ�ʼ��")
money = int(money)
ticket = input("���Ƿ�Ҫ��ȡ�Ż�ȯ��\n y/n?\n")
if ticket =="y":
    #time.sleep(2)
    if a >=0 and a<=9:
        b=0.5
        shop[4][1]=round(shop[4][1]*b,2)

        print("��ϲ������һ�Ż�е���������Ż�ȯ")
    elif a > 9 and a <=29:
        d=0.3
        shop[5][1]=round(shop[5][1]*d,2)
        print("��ϲ�����һ���������������Ż�ȯ")
    elif a > 29 and a <= 44:
        c=0.8
        shop[1][1]=round(shop[1][1]*c,2)
        print("��ϲ������һ��HUA WEI WATCH�����Ż�ȯ")
else:
    pass

# 2. ׼��һ���յĹ��ﳵ
mycart = []

sum=0
# 3.��ʼ����
sum=0
i  = 0
while i < 20:
    for key,value in enumerate(shop):
        print(key,value)
        # ��������Ҫ������Ʒ
    chose = input("��������Ҫ�����Ʒ:")

    if chose.isdigit():
        chose = int(chose)  # "1" --> 1
        if chose > len(shop) or chose < 0:  # 9 > 7
            print("����Ʒ�����ڣ���ϹŪ��")
        else:
            if money >= shop[chose][1]:
                money = money - shop[chose][1]
                mycart.append(copy.deepcopy(shop[chose]))
                sum=sum+shop[chose][1]
                print("��ϲ����Ʒ��ӳɹ����������Ϊ����", money)
                if b!=1 and chose==4:
                    shop[4][1]=5000
                elif c!=1 and chose==1:
                    shop[1][1]=1200
                elif d!=1 and chose==5:
                    shop[5][1]=4.5
                else:
                    pass
            else:
                print("��ܰ��ʾ���������п����㣬�������������Ʒ��")
    elif chose == "q" or chose == "Q":
        print("��ӭ�´ι��٣�")
        break
    else:
        print("�Բ��𣬱�ϹŪ���������룡")

    i = i + 1



# 4. ��ӡ���㹺��С��
print("���������Ĺ���С�������úã�������ôô�գ�")
print("".center(30,"-"))
for key,value in enumerate(mycart):
    print(key,value)
print("�����ѣ�",sum)
print("".center(30,"-"))










