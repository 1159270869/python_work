#1��ʵ������ʮ����������ӡʮ����֮��
sum = 0
cishu = 1
while cishu <= 10:
    print("�������",cishu,"������")
    meici = int(input())
    sum =sum+meici
    cishu =cishu+1
print("��ʮ�����ĺ�Ϊ��", sum)

#2���Ӽ�����������ʮ����������ӡ��������ʮ�����ĺ͡�ƽ����
sum = 0

cishu = 1
while cishu <= 10:
    print("�������",cishu,"������")
    b = int(input())
    if cishu ==1:
        a=b
        c=b
        sum=sum+b
        cishu = cishu + 1
    else:
        sum = sum + b
        if a <= b:
            a = b
        else:
            c=b
        cishu = cishu + 1
avg=sum/10
print("ʮ���������ǣ�",a,"\n��С�����ǣ�",c,"\nʮ�����ĺ��ǣ�",sum,"\nƽ�����ǣ�",avg)

#3���Ӽ��������������ߣ��ж��Ƿ����������Σ��Լ�����ʲô������
a=int(input("�������һ������"))
b=int(input("������ڶ�������"))
c=int(input("���������������"))
if a>0 and b>0 and c>0:
    if a<b+c and b<a+c and c<a+b:
        if a==b and b==c and a==c:
            print("�ȱ�������")
        elif a==b or b==c or a==c:
            if a^2 == b^2+c^2 or b^2==a^2+c^2 or c^2==a^2+b^2:
                print("����ֱ��������")
            else:
                print("����������")
        elif a^2 == b^2+c^2 or b^2==a^2+c^2 or c^2==a^2+b^2:
            if a==b or b==c or a==c:
                print("����ֱ��������")
            else:
                print("ֱ��������")
        else:
            print("������ͨ������")
    else:
        print("�޷�����������")
else:
    print("�޷�����������")

#4��ʹ��+-��A��B��ֵ����
A=56
B=78
A=A+B
B=A-B
A=A-B
print(A,B)

#5��ʵ�ֵ�¼ϵͳ������������������������ܣ��û�����root�����룺admin
username="root"
password="admin"
cishu = 0
yonghu=input("�������û���")
case = 3
while cishu < case:
    mima = input("����������")
    if username==yonghu:
        if password != mima:
            print("�������")
            cishu += 1
            continue
        else:
            print("��¼�ɹ�")
            break
if cishu==3:
    print("���Ѿ�������", case, "����������")

#6������1-100֮��
sum=0
case=1
while case<=100:
    sum =sum+case
    case+=1
print("1-100�ĺ�Ϊ��",sum)

#7����������
day = 1
high=20
climb=0
while climb<20:
    climb=3+climb
    if climb<20:
        climb=climb-2

    else:
        break
    day += 1
print("��",day,"��������")

#8��8�γɼ�
from numpy import *
list=[]
sum=0

for i in range(1,7):
    print("�����", i, "�ųɼ�")
    scores=int(input())
    list.append(scores)
for i in range(0,len(list)):
    sum=sum+list[i]

print("�ܷ���",sum,"ƽ������",mean(list),"��߷���",max(list),"��Сֵ��",min(list))

#9����ӡ������
for i in range(8):
    for j in range(0, 8-i):
        print(end="  ")
    for k in range(8-i, 8):
        print("*", end="   ")

    print("")

#10��while�žų˷���

i = 1
while i <= 9:
    j = 1
    while(j <= i):
        print(f'{i}*{j}={i*j}', end='\t')
        j += 1
    print('')
    i += 1
#11������˷���
# �žų˷���
i = 9
while i >=1:
    j = 1
    while j <= i:
        print(f'{i}*{j}={i*j}', end='\t')
        j += 1
    print('')
    i -= 1




