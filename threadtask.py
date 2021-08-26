import time
import threading
basket=0


class Cook(threading.Thread):
    name=None
    count=0
    tuichu=0
    def run(self)->None:
        global basket
        while True:
            if basket<500:
                basket=basket+1
                self.count=self.count+1
                print(self.name,"做了{}个面包,篮子里还剩{}个".format(self.count,basket))
            elif basket==500:
                self.tuichu=self.tuichu+1
                if self.tuichu==15 :
                    time.sleep(10)

                    break
                else:
                    time.sleep(2)
                    print(self.name, "休息了2秒钟")
            else:
                time.sleep(2)

                print(self.name,"休息了2秒钟")


                continue
        print(self.name, "做了{}个面包,篮子里还剩{}个".format(self.count, basket))





class Customer(threading.Thread):
    money=3000
    name=None
    count=0
    def run(self) -> None:
        global basket
        while True:
            if basket>0 and self.money>0:
                self.count=self.count+1
                basket=basket-1
                self.money=self.money-3
                print(self.name,"买了",self.count,"个面包,还剩",self.money,"元")
            elif self.money==0:
                time.sleep(20)

                break
            else:
                time.sleep(3)
                continue
        print(self.name, "买了", self.count, "个面包,还剩", self.money, "元")



c1=Cook()
c1.name="厨师1"
c2=Cook()
c2.name="厨师2"
c3=Cook()
c3.name="厨师3"
cust1=Customer()
cust1.name="顾客1"
cust2=Customer()
cust2.name="顾客2"
cust3=Customer()
cust3.name="顾客3"
cust4=Customer()
cust4.name="顾客4"
cust5=Customer()
cust5.name="顾客5"
cust6=Customer()
cust6.name="顾客6"
T1=time.perf_counter()
c1.start()
c2.start()
c3.start()

cust1.start()
cust2.start()
cust3.start()
cust4.start()
cust5.start()
cust6.start()






