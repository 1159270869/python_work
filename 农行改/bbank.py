import random

from tools import Tools
tools=Tools()
class Bank:

    __bank_name="中国农业银行"
    def setBank_name(self,bank_name):
        self.__bank_name=bank_name
    def getBank_name(self):
        return self.__bank_name
    data={}
    def bank_addUser(self,account,username,password,country,province,street,door):
        # 随机获取账号
        if tools.isFull(self.data) == True:
            return 3
        if tools.isExist(account,self.data) == True:
            return 2
        else:
            self.data[account]={
                "username":username,
                "password":password,
                "country":country,
                "province":province,
                "street":street,
                "door":door,
                "money":0,
                "bank_name":self.getBank_name()
            }
            return 1
    def bank_saveMoney(self,account,password,money):
        if tools.isExist(account,self.data)==True:
            if self.data[account]["password"]==password:
                self.data[account]["money"]=self.data[account]["money"]+money
                return 1
            else:

                return 2
        else:
            return 3
    def bank_takeMoney(self,account,password,money):
        if tools.isExist(account, self.data) == True:
            if self.data[account]["password"]==password:
                if self.data[account]["money"]>=money:
                    self.data[account]["money"] = self.data[account]["money"] - money
                    return 1
                else:
                    return 2
            else:

                return 3
        else:
            return 3

    def bank_transfer(self,account1,account2,password,money):
        if tools.isExist(account1)==True and tools.isExist(account2)==True:
            if self.data[account1]["password"]==password:
                if self.data[account1]["money"]>=money:
                    self.data[account1]["money"]= self.data[account1]["money"]-money
                    self.data[account2]["money"]= self.data[account2]["money"]+money
                    return 1
                else:
                    return 2
            else:
                return 3
        else:
            return 4
    def bank_information(self,account,password):
        if tools.isExist(account,self.data)==True:
            if self.data[account]["password"]==password:
                return 1
            else:
                return 2
        else:
            return 3

