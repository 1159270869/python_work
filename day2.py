#1、实现输入十个数，并打印十个数之和
sum = 0
cishu = 1
while cishu <= 10:
    print("请输入第",cishu,"个数：")
    meici = int(input())
    sum =sum+meici
    cishu =cishu+1
print("这十个数的和为：", sum)

#2、从键盘依次输入十个数，最后打印最大的数、十个数的和、平均数
sum = 0

cishu = 1
while cishu <= 10:
    print("请输入第",cishu,"个数：")
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
print("十个数最大的是：",a,"\n最小的数是：",c,"\n十个数的和是：",sum,"\n平均数是：",avg)

#3、从键盘输入任意三边，判断是否生成三角形，以及生成什么三角形
a=int(input("请输入第一个数："))
b=int(input("请输入第二个数："))
c=int(input("请输入第三个数："))
if a>0 and b>0 and c>0:
    if a<b+c and b<a+c and c<a+b:
        if a==b and b==c and a==c:
            print("等边三角形")
        elif a==b or b==c or a==c:
            if a^2 == b^2+c^2 or b^2==a^2+c^2 or c^2==a^2+b^2:
                print("等腰直角三角形")
            else:
                print("等腰三角形")
        elif a^2 == b^2+c^2 or b^2==a^2+c^2 or c^2==a^2+b^2:
            if a==b or b==c or a==c:
                print("等腰直角三角形")
            else:
                print("直角三角形")
        else:
            print("构成普通三角形")
    else:
        print("无法构成三角形")
else:
    print("无法构成三角形")

#4、使用+-将A，B数值交换
A=56
B=78
A=A+B
B=A-B
A=A-B
print(A,B)

#5、实现登录系统的三次密码输入错误锁定功能（用户名：root，密码：admin
username="root"
password="admin"
cishu = 0
yonghu=input("请输入用户名")
case = 3
while cishu < case:
    mima = input("请输入密码")
    if username==yonghu:
        if password != mima:
            print("密码错误")
            cishu += 1
            continue
        else:
            print("登录成功")
            break
if cishu==3:
    print("你已经输入了", case, "次密码锁定")

#6、计算1-100之和
sum=0
case=1
while case<=100:
    sum =sum+case
    case+=1
print("1-100的和为：",sum)

#7、青蛙爬井
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
print("第",day,"天爬出来")

#8、8课成绩
from numpy import *
list=[]
sum=0

for i in range(1,7):
    print("输入第", i, "门成绩")
    scores=int(input())
    list.append(scores)
for i in range(0,len(list)):
    sum=sum+list[i]

print("总分是",sum,"平均分是",mean(list),"最高分是",max(list),"最小值是",min(list))

#9、打印三角形
for i in range(8):
    for j in range(0, 8-i):
        print(end="  ")
    for k in range(8-i, 8):
        print("*", end="   ")

    print("")

#10、while九九乘法表

i = 1
while i <= 9:
    j = 1
    while(j <= i):
        print(f'{i}*{j}={i*j}', end='\t')
        j += 1
    print('')
    i += 1
#11、反向乘法表
# 九九乘法表
i = 9
while i >=1:
    j = 1
    while j <= i:
        print(f'{i}*{j}={i*j}', end='\t')
        j += 1
    print('')
    i -= 1




