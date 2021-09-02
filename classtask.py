#分析一个水杯的属性和功能，使用类描述并创建对象
class Glass():
    __hight="20cm"
    __volume="800ml"
    __color="蓝色"
    __quality="铁"
    def power(self):
        print(self.__hight,self.__volume,
              self.__color,self.__quality,"的杯子可以盛放液体")

glass=Glass()
glass.power()
#笔记本电脑
class Computer():
    __screen_size=None
    __price=None
    __cpu_model=None
    __ram=None
    __standby=None
    def power(self):
        print("电脑可以打字，打游戏，看视频")
    def __init__(self,screen_size,price,cpu_model,ram,standby):
        self.__screen_size=screen_size
        self.__price=price
        self.__cpu_model=cpu_model
        self.__ram=ram
        self.__standby=standby

com=Computer()
com.power()

#题目一
class Conditioner():
    __brand=""
    __price=""
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand
    def setPrice(self,price):
        self.__price=price
    def getPrice(self):
        return self.__price
    def start(self):
        print("空调开机了。。。")
    def timing(self,time):
        print("空调将在{}分钟后自动关闭".format(time))
con=Conditioner()
con.setBrand("格力")
con.setPrice("2000")
print(con.getBrand(),con.getPrice())
con.start()
con.timing(20)
#题目二
class Student():
    __name=None
    __age=None
    def setName(self,name):
        self.__name=name
    def setAge(self,age):
        self.__age=age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def introduce(self):
        print("大家好，我叫{}，今年{}岁了".format(self.__name,self.__age))
    def compare(self,student):
        if student.getAge() > self.__age:
            age1=student.getAge()-self.__age
            print("我比同桌小{}岁".format(age1))
        elif student.getAge() == self.__age:
            print("我和同桌一样大")
        elif student.getAge() < self.__age:
            age1=self.__age-student.getAge()
            print("我比同桌大{}岁".format(age1))
me=Student()
deskmate=Student()
me.setAge(24)
me.setName("钱")
deskmate.setAge(26)
deskmate.setName("孙")
me.compare(deskmate)
#题目三
class Hunman():
    name=None
    sex=None
    age=None
    call_balance=None
    brand=None
    battery_capacity=None
    screen_size=None
    standby=None
    interal=None
    def texting(self,text):
        print(text)
    def call(self,phonenum,time):
        if time<0:
            print("输入非法")
        else:
            if self.call_balance==None or self.call_balance<1:
                print("话费不足")
            else:
                pass
            if time>=0 and time<=10:
                self.call_balance=self.call_balance-time*1
                self.interal=self.interal-15*time
            elif time>10 and time <=20:
                self.call_balance=self.call_balance-0.8*time
                self.interal=self.interal-39*time
            else:
                self.call_balance=self.call_balance-0.65*time
                self.interal=self.interal-48*time

#题目四
#I
class Student():
    sno=None
    name=None
    age=None
    sex=None
    hight=None
    weight=None
    score=None
    address=None
    phone=None
    def study(self,time):
        print("学习了{}分钟".format(time))
    def play(self,ganmename):
        print("玩了{}".format(ganmename))

    def programming(self,lines):
        print("写了{}行代码".format(lines))
    def sum(self,*num):
        sum=0
        for i in num:
            sum=sum+i
        return sum
s=Student()
print(s.sum(1,2,3,4,5,6,7,8,9))
#II
class Car():
    __size=None
    __wheels=None
    __color=None
    __weight=None
    __capacity=None
    def __init__(self,function):
        print("该车的功能是：",function)

    def setsize(self,size):
        self.__size=size
    def setwheels(self,wheels):
        self.__wheels = wheels
    def setcolor(self,color):
        self.__color=color
    def setweight(self,weight):
        self.__weight=weight
    def setcapacity(self,capacity):
        self.__capacity=capacity
falali=Car("赛车")
baoma=Car("家居")
lingmu=Car("越野")
wuling=Car("神车")
tuolaji=Car("搬运")
#III
class Computer():
    __size=None
    __standby=None
    __color=None
    __weight=None
    __cpu=None
    __memory=None
    __hard_disk=None
    def action1(self,game):
        print("笔记本电脑可以玩{}，办公".format(game))
    def __init__(self,game):
        self.action1(game)


com=Computer("英雄联盟")

# IV
class Monkey():
    __catagory=None
    __sex=None
    __color=None
    __weight=None
    def make_fire(self,material):
        print("会使用{}生火".format(material))
    def learning(self,*learn):
        print("它们会学习：",end="")
        for i in learn:
            print(i,end="  ")


mon=Monkey()
mon.make_fire("木棒")
mon.learning("抽烟","喝酒")

