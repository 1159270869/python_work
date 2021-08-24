
class Tools:
    def isExist(self,a,b):
        if a in b:
            return True
        else:
            return False
    def isFull(self,a):
        if len(a)>100:
            return True

