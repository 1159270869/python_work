import copy

import xlrd

clothes=['羽绒服', '牛仔裤', '风衣', '皮草', 'T血', '马甲', '小西装', '皮衣', '衬衫', '休闲裤', '卫衣', '棉衣', '铅笔裤']
price=[]
c=[]
nums=[]
for i in range(len(clothes)):
    nums.append(0)
    price.append(0)

# 1. 打开工作簿
wd = xlrd.open_workbook("2020年每个月的销售情况.xlsx",encoding_override=True)
# 2.打开您要操作的选项卡

total_sum = 0

total_cloth_sum=0
for i in range(0, 12):

    y=i
    st = wd.sheets()[i]
    rows = st.nrows  # 获取行数  # 4
    cols = st.ncols  # 获取列数
    sum = 0
    cloth_sum = 0


    for a in range(1,rows):
        data = st.row_values(a)
        sum = sum +data[2]*data[4]

        # cloth=data[1]
        cloth_sum=data[4]+cloth_sum#数量
        for i in range(len(clothes)):
            if data[1]==clothes[i]:
                nums[i]=nums[i]+data[4]
                price[i]=price[i]+data[2]*data[4]
    c.append(copy.deepcopy(nums))



#    print(round(sum,1))
    total_sum = sum + total_sum
    total_cloth_sum=total_cloth_sum+cloth_sum
    print(y+1,"月:")
    for i in range(len(clothes)):
        f = nums[i] / total_cloth_sum
        p = price[i] / sum
        print(clothes[i],"销售数量占比:{:.2%}".format(f))



for i in range(len(clothes)):
    f=nums[i]/total_cloth_sum
    p=price[i]/total_sum
    print(clothes[i],"的总数量占比为：{:.2%},总销售额占比为：{:.2%}".format(f,p))
d = clothes[nums.index(max(nums))]
g = clothes[nums.index(min(nums))]
# print(total_cloth_sum,nums[0])
print("全年的销售总额：",round(total_sum,1),"最畅销的衣服是：",d,"销售最低的是：",g)


q=[]
quarter1 = list(map(lambda x, y: x - y, c[3], c[0]))#第一季度
q1=clothes[quarter1.index(max(quarter1))]
q.append(q1)
quarter2 = list(map(lambda x, y: x - y, c[6], c[3]))
q2=clothes[quarter2.index(max(quarter2))]
q.append(q2)
quarter3 = list(map(lambda x, y: x - y, c[9], c[6]))
q3=clothes[quarter3.index(max(quarter3))]
q.append(q3)
quarter4 = list(map(lambda x, y, z: x - y + z, c[11], c[9],c[0]))
q4=clothes[quarter4.index(max(quarter4))]
q.append(q4)
for i in range(1,5):
    print(i,"季度最畅销的是：",q[i-1])











# lst1 = [1, 4, 7]
#
# lst2 = [2, 5, 3]
#
# sum_lst = list(map(lambda x, y: x + y, lst1, lst2))
#
# print(sum_lst)
# sum1 = 0
# t = 0
# for i in range(1, 12):
#     st = wd.sheets()[i]
#     rows = st.nrows  # 获取行数  # 4
#     cols = st.ncols  # 获取列数
#
#     sum = 0
#     for a in range(1,rows):
#         data = st.row_values(a)
#         sum = sum +data[2]*data[4]
#     t = t+1
#     sum1 = sum1+sum
#     if t%3 == 0:
#         #print(round(sum1/total_sum, 1))
#         zhanbi=(sum1/total_sum)
#         print("季度占比:{:.2%}".format(zhanbi))
#         sum1=0




