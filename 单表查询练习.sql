company数据库：
	|--dept:部门表
		|--`deptno` 部门编号
		|--`dname`  部门名称
		|--`loc`    部门所在地址
  

	|--employees:员工表
		|--`empno`	员工编号
		|--`ename`	员工姓名
		|--`job`	工作
		|--`MGR`	上级领导
		|--`hiredate`   入职日期
		|--`sal`	薪资
		|--`comm`       将金
		|--`deptno`     部门编号

/*
	1. 查询出部门编号为30的所有员工
	2. 所有经理的姓名、编号和部门编号。
	3. 找出奖金高于工资的员工。
	4. 找出奖金高于工资60%的员工。
	5. 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料。
	6. 找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
	7. 无奖金或奖金低于1000的员工。
	8. 查询名字由三个字组成的员工。
	9. 查询2000年以及以后入职的员工。
	10. 查询所有员工详细信息，用编号升序排序
	11. 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
	12. 查询每个部门的平均工资
	13. 查询每个部门的雇员数量。
	14. 查询每种工作的最高工资、最低工资、人数

*/

SELECT ename
FROM t_employees
WHERE deptno=30

SELECT ename,empno,deptno
FROM t_employees
WHERE job = "经理"


SELECT ename
FROM t_employees
WHERE comm > sal

SELECT ename
FROM t_employees
WHERE comm > sal*0.6

SELECT *
FROM t_employees
WHERE job="经理" OR (deptno=20 AND job="分析员")

SELECT *
FROM t_employees
WHERE job="经理" OR (deptno=20 AND job="分析员") OR (job NOT IN("经理","武装上将") AND sal>=3000)

SELECT ename
FROM t_employees
WHERE comm=NULL OR comm<1000

SELECT *
FROM t_employees
WHERE ename LIKE "___"

SELECT *
FROM t_employees
WHERE hiredate LIKE "2000%" OR hiredate > "2000%"

SELECT *
FROM t_employees
ORDER BY empno

SELECT *
FROM t_employees
ORDER BY sal DESC,hiredate ASC

SELECT deptno,AVG(sal)
FROM t_employees
GROUP BY deptno

SELECT deptno,COUNT(*)
FROM t_employees
GROUP BY deptno

SELECT deptno,MAX(sal),MIN(sal),COUNT(*)
FROM t_employees
GROUP BY deptno


笔试题
1、
Inner join 与left join 都是通过两个表之间的匹配的连接谓词生成结果集，不同的是，inner join用左表的每一行与右表每一行作比较，当满足要求双方皆是非空时组合成结果，即两者的交集，
而 left join则是以左边表为基准，返回左表所有值，匹配值为空时，则以null补充
2、
	1、Select current_balance From account Where uid=’10001’
	2、update account a set a.current_balance=50000 where a.uid = (select uid from user_secret where mobile=’13600010001’)
3、
Update A set B=C where D=E
A
Select count(*)
From emp
Group by `部门`
B、
Select `部门`,count(*)
From emp 
Group by `部门`
Having count(*)>10
C、
Select `姓名`
From emp
Where 部门=（select 部门 from emp where name = ‘张一’）
4、
Limit 0,5
5、
5.1
select count(*) from company c, em_info e, em_basic eb

where c.cid = eb.cid and e.eid = eb.eid

and c.status = '1'

group by c.cid having avg(a.work_age) > 3;
5.1.2.2、
select count(cname) 
from employee a left join em_basic b on a.eid = b.eid left join company c on c.cid = b.cid

where c.status = '1'

group by c.cid having avg(a.work_age) > 3;


5.2、Select c.cname,count(e.ename)
From company c,employee_info e,employee_basic b
Where e.eid=b.eid and c.cid=b.cid
Group by c.cid desc limit 0,10
6、
Select *
From 密码汇款登记表 b1,密码汇款兑付业务登记表 b2
Where b1.RemitNo=b2.RemitNo and b2.PaymentStat=01
Select paymentstat,count(*)
From 密码汇款登记表 b1
Group by paymentstat
7、
区别：
1、表只用物理空间而视图不占用物理空间，视图只是逻辑概念的存在，表可以及时对它进行修改，但视图只能有创建的语句来修改。
2、视图是查看数据表的一种方法，可以查询数据表中某些字段构成的数据，只是一些SQL语句的集合。从安全的角度说，视图可以不给用户接触数据表，从而不知道表结构。
3、表属于全局模式中的表，是实表；视图属于局部模式的表，是虚表。

联系：视图（view）是在基本表之上建立的表，它的结构（即所定义的列）和内容（即所有数据行）都来自基本表，
它依据基本表存在而存在。一个视图可以对应一个基本表，也可以对应多个基本表。视图是基本表的抽象和在逻辑意义上建立的新关系。
8、
Select 班级，count(学生)
From 表
Where 成绩>60
Group by 班级
9、
Select name，sum(score) as total_scores
From Ta
Group by name
Having total_scores>145


