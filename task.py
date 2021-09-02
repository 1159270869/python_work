import time


class Oldphone:
    __brand = ""
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand
    def call(self,phone):
        print("正在给",phone,"打电话")
        for i in range(8):
            print(".",end="")
            time.sleep(1)

class Newphone(Oldphone):
    picture = ""
    def call(self,number):
        print("语音拨号中")
        super().call(number)
    def introduce(self):
        print("品牌为：",self.getBrand(),"的手机很好用",)

new = Newphone()
new.setBrand("华为")
new.introduce()
new.call("18835067088")

class Cook:
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
    def cookrice(self):
        print("淘米，打开电饭煲，就这么简单")
class Newcook(Cook):
    def cookveget(self):
        print("大火爆炒鸡蛋")
class Nnewcook(Newcook):
    # def setName(self,name):
    #     super().setName(name)
    #     print("定义名字")
    # def setAge(self,age):
    #     super().setAge(age)
    #     print("定义年龄")
    # def getAge(self):
    #     print("调用年龄")
    # def getName(self):
    #     print("调用姓名")
    def cookrice(self):
        print("蒸饭")
    def cookveget(self):
        print("炒菜")
cook=Nnewcook()
cook.setAge(18)
cook.setName("小刘")
print(cook.getName(),cook.getAge())
cook.setAge(88)
cook.setName("老刘")
cook.cookrice()
cook.cookveget()

class Person:
    __age=None
    __sex=None
    __name=None
    def setAge(self,age):
        self.__age=age
    def setSex(self,sex):
        self.__sex=sex
    def setName(self,name):
        self.__name=name
    def getAge(self):
        return self.__age
    def getSex(self):
        return self.__sex
    def setName(self):
        return self.__name
class Worker(Person):
    def work(self):
        print(self.setName(),"正在干活")

class Student(Person):
    __sid = None
    def setSid(self,sid):
        self.__sid=sid
    def getSid(self):
        return self.__sid
    def action(self):
        print("唱歌，跳舞")