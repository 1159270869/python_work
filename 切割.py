file = open(baidu_x_system.log",mode='r+',encoding='utf-8')
data=file.readlines()
list1=[]
for i in data:
    list=i.split(' - - ')
    # print(list[0])
    list1.append(list[0])

list2=set(list1)
for i in list2:
    print("{}出现{}次\n".format(i,list1.count(i)))