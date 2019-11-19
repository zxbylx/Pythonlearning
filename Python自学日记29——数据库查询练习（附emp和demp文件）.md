# Python自学日记29——数据库查询练习（附emp和demp文件）

```mysql
SELECT * FROM emp;

-- 1.查询部门编号为30的所有员工
SELECT * FROM emp where DEPTNO=30; 
-- 2.所有销售员的姓名、编号和部门编号
SELECT ENAME,EMPNO,DEPTNO FROM emp where JOB='SALESMAN';
-- 3.找出奖金高于工资的员工
SELECT ENAME FROM emp where COMM>SAL;
-- 4.找出奖金高于工资60%的员工
SELECT * FROM emp where COMM>0.6*SAL;
-- 5.找出部门编号为10中所有经理，和部门编号为20中所有销售员的详细资料
SELECT * FROM emp where (DEPTNO=10 AND JOB='MANAGER') OR (DEPTNO=20 AND JOB='SALESMAN');
-- 6.找出部门编号为10中所有经理，部门编号为20中所有销售员，还有既不是经理又不是销售员但工资大于等于2000的所有员工详细资料
SELECT * FROM emp where (DEPTNO=10 AND JOB='MANAGER') OR (DEPTNO=20 AND JOB='SALESMAN') OR (JOB NOT IN('MANAGER','SALESMAN') AND SAL>=2000);-- 容易忘记分号
-- 7.无奖金或者奖金低于1000的员工
SELECT * FROM emp where COMM IS NULL OR COMM<1000;
-- 8.查询名字由四个字组成的员工
-- SELECT * FROM emp where ENAME='____';不能用=
SELECT * FROM emp where ENAME LIKE '____';
SELECT * FROM emp where ENAME LIKE 'A%'; -- 模糊查询练习
-- 9.查询1981年入职的员工
SELECT * FROM emp where HIREDATE BETWEEN '1981-01-01' AND '1981-12-31';
-- SELECT * FROM emp where HIREDATE LIKE '1981-%';不知道为啥报错，视频上是对的，结果我这错了，可能版本升级语言改了
-- 10.查询所有员工信息，用编号升序排序
SELECT * FROM emp ORDER BY EMPNO;-- 忘记order
-- 11.查询所有员工信息，用工资降序排列，如果工资相同，使用入职日期升序排列
SELECT * FROM emp ORDER BY SAL desc,HIREDATE asc;
-- 12.每个部门的平均工资（分组查询）
SELECT DEPTNO,AVG(SAL) FROM emp group by DEPTNO; 
-- 13.每个部门的员工数量
SELECT DEPTNO,count(*) FROM emp group by DEPTNO;
-- 14.查询每种工作的最高工资，最低工资，人数
SELECT JOB,MAX(SAL),MIN(SAL),COUNT(*) AS NUM_MEMBERS FROM emp group by JOB;
```

数据库的导出备份和还原

```mysql
-- 导出数据库的语句，在cmd中需要在登录前输入，只备份数据库内容，并不备份数据库
mysqldump -uroot -p123456 news>F:/数据库/news.sql -- 注意斜线方向
-- 导入到数据库中文件，需要保证数据库存在，还是在登录前输入
mysql -uroot -p123456 news<F:/数据库/news.sql -- 箭头方向向左了
-- 在登录状态下切换到对应数据库输入source +路径及文件可导入
source F:/数据库/news.sql;
```

主键外键以及关系模型

```mysql
-- use news;
-- CREATE TABLE emp(
-- empno INT PRIMARY KEY,
-- ename VARCHAR(50)
-- );
-- INSERT INTO emp VALUES(1,'张三');
-- SELECT *  FROM emp;
-- CREATE TABLE emp(
-- empno INT,
-- ENAME VARCHAR(50),
-- PRIMARY KEY(empno)
-- );
-- INSERT INTO emp VALUES(1,'张三');
-- SELECT *  FROM emp;
drop table emp;
CREATE TABLE emp(
empno INT,
ENAME VARCHAR(50)
);
ALTER TABLE emp
-- ADD -->添加列
-- MODIFY -->修改列名和类型
-- CHANGE -->修改列名
-- DROP -->删除列
-- RENAME -->修改表名
ADD PRIMARY KEY(empno);
ALTER TABLE emp DROP PRIMARY KEY; -- 删除主键stu
CREATE TABLE stu1(
ID INT PRIMARY KEY AUTO_INCREMENT, -- 主键自增长限制是整型
SNAME VARCHAR(20),
AGE VARCHAR(10),
GENDER VARCHAR(10)
);
DESC stu1;
INSERT INTO stu1 VALUES(NULL,'张三',18,'male');
INSERT INTO stu1 VALUES(NULL,'李四',18,'male');
SELECT * FROM stu1;
ALTER TABLE stu1
modify SNAME VARCHAR(20) NOT NULL UNIQUE;-- 非空和唯一约束

-- 概述模型，对象模型，关系模型
SELECT * FROM emp;
SELECT * FROM dept;
-- 对象模型：可以双向关联，而且引用的是对象，而不是一个主键
-- 关系模型：只能多方引用一方，而且引用的只是主键，而不是一整行记录
drop table emp;
-- 一对多关系
CREATE TABLE dept(
dno INT PRIMARY KEY AUTO_INCREMENT,
dname VARCHAR(50)
);
INSERT INTO dept VALUES(10,'研发部');
INSERT INTO dept VALUES(20,'人力资源部');
INSERT INTO dept VALUES(30,'产品部');

SELECT * FROM dept;
CREATE TABLE emp(
empno INT PRIMARY KEY AUTO_INCREMENT,
ename VARCHAR(50),
dno INT,
CONSTRAINT fk_emp_dept FOREIGN KEY(dno) REFERENCES dept(dno)  -- 外键需要CONSTRAINT,修改表增加外键约束用add加这一句即可
);
desc emp;
INSERT INTO emp(empno,ename) VALUES(NULL,'张三');
INSERT INTO emp(empno,ename,dno) VALUES(NULL,'李四',10);
INSERT INTO emp(empno,ename,dno) VALUES(NULL,'王五',20);
select * from emp;
ALTER TABLE emp
DROP FOREIGN KEY fk_emp_dept; -- 外键名的作用可以使用这个语句删除外键，但是保留本列，如果不用外键名直接用drop dno就会报错，有外键约束
INSERT INTO emp(empno,ename,dno) VALUES(NULL,'赵六',40);-- 删除外键后，dno这一列不再受外键约束限制
ALTER TABLE emp
DROP dno; -- 通过外键名删除外键后这一列可以直接删除了

-- 一对一关系：夫妻（从表的主键即是外键）
CREATE TABLE hasband(
hid INT PRIMARY KEY AUTO_INCREMENT,
hname VARCHAR(50)
);
ALTER TABLE hasband
RENAME TO husband;
INSERT INTO husband VALUES(NULL,'刘备');
INSERT INTO husband VALUES(NULL,'关羽');
INSERT INTO husband VALUES(NULL,'张飞');
SELECT * FROM husband;
CREATE TABLE wife(
wid INT PRIMARY KEY,
wname VARCHAR(50),
CONSTRAINT a FOREIGN KEY(wid) REFERENCES husband(hid)
);
INSERT INTO wife VALUES(1,'杨贵妃');
INSERT INTO wife VALUES(4,'杨贵');
SELECT * FROM wife;
SHOW CREATE TABLE wife; -- 查看创建某张表的语句，可查看外键名
-- SELECT * FROM wife where constraint_name='a';想尝试用这个语句查外键名对应的表，结果不行

-- 多对多关系:需要中间表，在中间表中将二表关系写出来
CREATE TABLE student(
SID INT PRIMARY KEY AUTO_INCREMENT,
SNAME VARCHAR(50)
);

CREATE TABLE teacher(
TID INT PRIMARY KEY AUTO_INCREMENT,
TNAME VARCHAR(50)
);

CREATE TABLE stu_tea(
SID INT,
TID INT,
CONSTRAINT fk_student FOREIGN KEY(SID) REFERENCES student(SID),
CONSTRAINT fk_teacher FOREIGN KEY(TID) REFERENCES teacher(TID)
);

INSERT INTO student VALUES(NULL,'小明');
INSERT INTO student VALUES(NULL,'小红');
INSERT INTO student VALUES(NULL,'小刚');
INSERT INTO student VALUES(NULL,'小黄');
INSERT INTO student VALUES(NULL,'小亮');
select * FROM student;
INSERT INTO teacher VALUES(NULL,'赵老师');
INSERT INTO teacher VALUES(NULL,'李老师');
INSERT INTO teacher VALUES(NULL,'王老师');
select * from teacher;

INSERT INTO stu_tea VALUES(1,1);
INSERT INTO stu_tea VALUES(2,1);
INSERT INTO stu_tea VALUES(3,1);
INSERT INTO stu_tea VALUES(4,1);
INSERT INTO stu_tea VALUES(5,1);
INSERT INTO stu_tea VALUES(2,2);
INSERT INTO stu_tea VALUES(3,2);
INSERT INTO stu_tea VALUES(4,2);
INSERT INTO stu_tea VALUES(3,3);
INSERT INTO stu_tea VALUES(4,3);
INSERT INTO stu_tea VALUES(5,3);
SELECT * FROM stu_tea;
```

emp.sql和dept.sql文件

链接: [https://pan.baidu.com/s/1agNCkmU_-02QXan0aJL-1w](https://link.zhihu.com/?target=https%3A//pan.baidu.com/s/1agNCkmU_-02QXan0aJL-1w) 提取码: 2uq4