import pymysql

import xlrd
class exceltransfer():

    host="localhost"
    user="root"
    password="root"
    database="bank"

    def create(self,sql, param):
        # 2. 获取连接
        con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        # 3. 创建游标
        cursor = con.cursor()
        # 4.执行sql
        cursor.execute(sql, param)
        # 5.提交
        con.commit()
        # 6.关闭
        cursor.close()
        con.close()

    def insertnum(self,num,table_name,data1):
        if num==1:
            sql= "insert into "+table_name+" values(%s)"
            param=data1
            return self.create(sql,param)
        if num==2:
            sql= "insert into "+table_name+" values(%s,%s)"
            param=data1
            return self.create(sql,param)
        if num==3:
            sql= "insert into "+table_name+" values(%s,%s,%s)"
            param=data1
            return self.create(sql,param)
        if num==4:
            sql= "insert into "+table_name+" values(%s,%s,%s,%s)"
            param=data1
            return self.create(sql,param)
        if num==5:
            sql= "insert into "+table_name+" values(%s,%s,%s,%s,%s)"
            param=data1
            return self.create(sql,param)
        if num==6:
            sql= "insert into "+table_name+" values(%s,%s,%s,%s,%s,%s)"
            param=data1
            return self.create(sql,param)
        if num==7:
            sql= "insert into "+table_name+" values(%s,%s,%s,%s,%s,%s,%s)"
            param=data1
            return self.create(sql,param)
        if num==8:
            sql= "insert into "+table_name+" values(%s,%s,%s,%s,%s,%s,%s,%s)"
            param=data1
            return self.create(sql,param)
        if num==9:
            sql= "insert into "+table_name+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param=data1
            return self.create(sql,param)


    def openexcel(self,name):
        wb = xlrd.open_workbook(name,encoding_override=True)
        l=len(wb.sheets())
        for i in range(l):
            st = wb.sheets()[i]
            rows = st.nrows  # 获取行数  # 4
            # cols = st.ncols  # 获取列数
            data = st.row_values(0)#字段名
            table_name = st.name
            sql="create table "+table_name+"("+data[0]+" varchar(30))"
            self.create(sql,[])
            d=len(data)
            for i in range(1,d):
                sql1="alter table "+table_name+" add `"+data[i]+"` varchar(20)"
                self.create(sql1,[])

            for j in range(1,rows):
                data1 = st.row_values(j)
                # for k in range(d):
                self.insertnum(d,table_name,data1)
                    # c=st.cell(j,k).value
                    # sql2 = "insert into "+table_name+" values "+c+" where rownum=%s and colnum=%s"
                    # self.create(sql2,[j+1,k+1])
            # for a in range(1,rows):
            #     data1 = st.row_values(a)
            #     b=tuple(data1)
            #     sql2 = "insert into "+table_name+" values",b
            #     self.create(sql2,[])





e=exceltransfer()
e.openexcel("12月份衣服销售数据.xlsx")




# wb = xlrd.open_workbook("12月份衣服销售数据.xlsx",encoding_override=True)
# # sb = "12月"
# st = wb.sheet_by_name("12月份各种服饰销售情况")
# # 通过st获取某个表格数据
# rows = st.nrows
# cols = st.ncols


# for i in range(0, 12):
#
# #     y=i
#     st = wd.sheets()[i]
#     rows = st.nrows  # 获取行数  # 4
#     cols = st.ncols  # 获取列数


# data=st.row_values(0)
# print(data)
# # for index,i in enumerate(data):
# #     print(index,i)
# # tables=copy.deepcopy(data[0])
# a= data[0]
# sql1="create table %s( dog varchar(20))"
# print(sql1)
# param="te"
# update(sql1,param)
# print(sql1)
# l=len(data)
# for i in range(data[1],data[l]):
#     sql = "alter table sb add %s varchar(20)"
#
#     print(sql)
#     update(sql,i)
# sql = "create table 1{"
#                       {}varchar
#                       {}
#                       ".format()\
#       "}"
# update(sql,[])
# name='hello'
# sql="create table tab1("+name+" varchar(20))"
#
#
# update(sql,[])