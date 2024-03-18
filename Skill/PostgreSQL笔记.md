## PostgreSQL配置
[Database Client](https://database-client.com/)
[PostgreSQL入门](https://www.bilibili.com/video/BV1Mi4y1K7HS/)
```bash
sudo apt install postgresql postgresql-contrib
systemctl status postgresql
psql --version

sudo cat /etc/shadow
sudo passwd postgres
su postgres -c psql
ALTER USER postgres WITH PASSWORD '123456';

sudo vi /etc/postgresql/14/main/pg_hba.conf
# Database administrative login by Unix domain socket
local  all  postgres  peer -> md5
sudo systemctl reload postgresql

psql -U postgres -W

CREATE USER ethan WITH PASSWORD '123456' SUPERUSER;
CREATE DATABASE ethan OWNER ethan;
psql
```

## PostgreSQL语法

| 语法       | 描述             |
| ---------- | ---------------- |
| \copyright | 显示分发条款     |
| \g         | 执行查询         |
| \q         | 退出             |
| ---------  | ---------------- |
| \?         | PSQL命令帮助     |
| \h         | SQL命令帮助      |
| ---------  | ---------------- |
| \i         | 导入文件         |
| \o         | 导出文件         |
| ---------  | ---------------- |
| \dn        | 列出数据库       |
| \du        | 列出用户         |
| \d         | 列出表,视图,序列 |
| \dt        | 列出表           |
| \dv        | 列出视图         |
| \ds        | 列出序列         |
| \di        | 列出索引         |
| \l         | 列出数据库       |
| ---------  | ---------------- |
| \c         | 连接数据库       |
| \conninfo  | 显示连接信息     |
| \encoding  | 显示或设置编码   |
| \password  | 更改用户密码     |
| ---------  | ---------------- |
| \cd        | 切换目录         |
| \setenv    | 设置环境变量     |
| \! <cmd>   | 执行Shell命令    |
| ---------  | ---------------- |
| \set       | 设置变量         |
| \unset     | 删除变量         |



## SQL基本数据类型

| 数据类型     | 描述         |
| ------------ | ------------ |
| -整数型      |              |
| BIGINT       | 整数(8字节)  |
| INT          | 整数(4字节)  |
| SMALLINT     | 整数(2字节)  |
| TINYINT      | 整数(1字节)  |
| BOOLEAN      | 布尔型       |
| -小数型      |              |
| REAL         | 浮点数       |
| FLOAT        | 单精度浮点数 |
| DOUBLE       | 双精度浮点数 |
| NUMERIC(p,s) | 定长精确数   |
| -二进制型    |              |
| BINARY(n)    | 定长二进制   |
| VARBINARY(n) | 变长二进制   |
| -字符串型    |              |
| CHAR(n)      | 定长字符串   |
| VARCHAR(n)   | 变长字符串   |
| -时间型      |              |
| DATE         | 日期         |
| TIME         | 时间         |
| DATETIME     | 日期时间     |

## SQL数据定义
### 数据库操作

#### 创建数据库: `CREATE DATABASE <name> [AUTHORIZATION <user>]`
#### 删除数据库: `DROP DATABASE <name> [CASCADE|RESTRICT]`
1. CASCADE: 删除数据库的同时删除数据库中的所有表
2. RESTRICT: 只有在数据库中没有表的情况下才能删除数据库

### 基本表操作

#### 创建基本表:
```sql
CREATE TABLE <name> (
    <column> <type> [NOT NULL] [DEFAULT <value>] [CKECK (<condition>)],
    ...
    [PRIMARY KEY (<column>)]
    [FOREIGN KEY (<column>) REFERENCES <table>(<column>)]
)
```

#### 修改基本表
```sql
-- 删除旧列
ALTER TABLE <name> DROP <column>;
-- 增加新列
ALTER TABLE <name> ADD <column> <type> [NOT NULL] [DEFAULT <value>] [CKECK (<condition>)];
-- 修改现有列
ALTER TABLE <name> MODIFY <column> <type> [NOT NULL] [DEFAULT <value>] [CKECK (<condition>)];
```

#### 删除基本表
```sql
DROP TABLE <name> [CASCADE|RESTRICT]
```



### 索引操作

#### 创建索引
```sql
CREATE [UNIQUE] INDEX <name> ON <table> (<column>[ASC|DESC]);
```

#### 删除索引
```sql
DROP INDEX <name>
```



## SQL数据查询

### SELECT基本结构

$\pi_{A_1,\cdots,A_n}(\sigma_F(R_1\times\cdots\times R_m)) \iff$
SELECT $A_1,\cdots,A_n$ FROM $R_1,\cdots,R_m$ WHERE $F$
1. 执行FROM: 选择特定表
2. 执行WHERE: 选择特定行(循环遍历每行)
3. 执行SELECT: 选择特定列



WHERE条件子句中的运算符:
1. 比较运算符: `=,>,<,>=,<=,!=`
2. 逻辑运算符: `AND,OR,NOT`
3. 成员运算符: `IN,NOT IN`
4. 谓词运算符: `BETWEEN,LIKE,IS NULL,IS NOT NULL`
5. 聚合函数: `COUNT,SUM,AVG,MAX,MIN`
6. 嵌套查询: `SELECT`

SELECT查询结果的交,并,差运算:
1. 交: `INTERSECT`
2. 并: `UNION`
3. 差: `EXCEPT`

<br>


教师关系 T(T_NUM, TNAME, TITLE)
课程关系 CT(C_NUM, CNAME, T_NUM)
学生关系 S(S_NUM, SNAME, AGE, SEX)
选课关系 SC(S_NUM, C_NUM, SCORE)

- 检索学习课程号为C2的学生学号和姓名
```sql
-- 连接查询: 先笛卡尔积, 再选择
SELECT S.S_NUM, S.SNAME
FROM S, SC
WHERE S.S_NUM = SC.S_NUM AND SC.C_NUM = 'C2';

-- 嵌套查询: 先从SC选出学习C2课程的学号, 再从S中选出学号和姓名
SELECT S_NUM, SNAME -- 选出学习C2课程的学生学号和姓名
FROM S
WHERE S_NUM IN (
    SELECT S_NUM -- 选出学习C2课程的学生学号
    FROM SC 
    WHERE C_NUM = 'C2');

-- 相关子查询: 对于S中的每行学生, 从SC中选出对应的课程, 如果有C2则输出
SELECT S_NUM, SNAME
FROM S
WHERE 'C2' IN ( -- 判断C2是否在这些课程中
    SELECT C_NUM -- 选出当前学生选的所有课程
    FROM SC 
    WHERE S_NUM = S.S_NUM);

-- 存在量词的相关子查询: 对于S中的每行学生, 从SC中选出对应的C2课程, 如果存在则输出
SELECT S_NUM, SNAME
FROM S
WHERE EXISTS ( -- 判断是否存在 当前学生选的C2课程
    SELECT * -- 选出当前学生选的C2课程
    FROM SC
    WHERE S_NUM = S.S_NUM AND C_NUM = 'C2');
```

- 检索至少选修LIU老师的一门课的学生学号和姓名
```sql
-- 连接查询
SELECT S.S_NUM, S.SNAME
FROM S, SC, CT, T
WHERE (S.S_NUM = SC.S_NUM AND SC.C_NUM = CT.C_NUM AND CT.T_NUM = T.T_NUM) AND T.TNAME = 'LIU';

-- 嵌套查询
SELECT S_NUM, SNAME
FROM S
WHERE S_NUM IN (
    SELECT S_NUM -- 选出LIU老师课程的学生学号
    FROM SC
    WHERE C_NUM IN (
        SELECT C_NUM -- 选出LIU老师的课程号
        FROM CT
        WHERE T_NUM IN (
            SELECT T_NUM -- 选出LIU老师的工号
            FROM T
            WHERE TNAME = 'LIU')));
```

- 检索至少选修课程号为C2和C4的学生学号和姓名
```sql
SELECT X.S_NUM, X.SNAME
FROM SC AS X, SC AS Y
WHERE X.S_NUM = Y.S_NUM AND X.C_NUM = 'C2' AND Y.C_NUM = 'C4';
```

- 检索不学C2课程的学生学号和姓名
```sql
-- 嵌套查询
SELECT S_NUM, SNAME
FROM S
WHERE S_NUM NOT IN ( -- 选出不在这些学号中的学生
    SELECT S_NUM -- 选出学习C2课程的学生学号
    FROM SC
    WHERE C_NUM = 'C2');

-- 存在量词
SELECT S_NUM, SNAME
FROM S
WHERE NOT EXISTS ( -- 判断当前学生 是否存在C2课程
    SELECT * -- 选出当前学生选择的C2课程
    FROM SC
    WHERE S_NUM = S.S_NUM AND C_NUM = 'C2');
```

- 检索学习全部课程的学生学号和姓名
```sql
-- 存在量词
SELECT S_NUM, SNAME -- 如果当前学生没有 没选的课, 则输出
FROM S
WHERE NOT EXISTS ( -- 判断是否存在 当前学生没有选的课程
    SELECT * -- 选出当前学生没有选的课程
    FROM CT
    WHERE C_NUM NOT IN (
        SELECT C_NUM -- 选出当前学生选的所有课程
        FROM SC
        WHERE S_NUM = S.S_NUM));
```

- 检索所学课程 包含学生S3所学课程 的学生学号
在SC表中找一个学生,
对于S3所学的每一门课,
该学生都学了

不存在某门课, S3选了但是该学生没选
```sql
-- 两层循环, 首先循环每个学生, 然后循环每门S3课程
-- 如果有一门S3课程, 该学生没选, 则跳过
CREATE TEMPOARY TABLE S3_COURSE AS
SELECT C_NUM
FROM SC
WHERE S_NUM = 'S3';

SELECT DISTINCT S_NUM
FROM SC AS SC1
WHERE NOT EXISTS ( -- 不存在这样的S3课程
    SELECT * -- 选择 S3课程(它没有被该学生选修)
    FROM S3_COURSE
    WHERE NOT EXISTS (
        SELECT * -- 某学生 与 某门S3课, 
        FROM SC AS SC2
        WHERE SC2.S_NUM = SC1.S_NUM AND SC2.C_NUM = S3_COURSE.C_NUM));
```


### SELECT完整结构

#### 聚合函数
1. COUNT(*): 计算元组的个数
2. COUNT(<col>): 计算列中的非空行数
3. SUM(<col>): 计算列中的数值之和
4. AVG(<col>): 计算列中的数值平均值
5. MAX(<col>): 计算列中的最大值
6. MIN(<col>): 计算列中的最小值

- 计算男学生的总人数和平均年龄
```sql
SELECT COUNT(*), AVG(AGE)
FROM S
WHERE SEX='M'
```

- 计算选过课的学生人数
```sql
SELECT COUNT(DISTINCT S_NUM)
FROM SC
```

#### SLELCT完整句法

```sql
SELECT <列名序列|列表达式序列>
FROM <基本表序列|视图序列>
[WHERE <行条件表达式>]
[GROUB BY <列名序列>
    HAVING <组条件表达式>]
[ORDER BY <列名[ASC|DESC]>]
```
1. 执行FROM: 读取基本表和视图, 进行笛卡尔积
2. 执行WHERE: 选择满足行条件表达式的元组
3. 执行GROUP: 按列名序列分组, 同时提取满足HAVING的组
4. 执行SELECT: 按给定列名和列表达式序列求值输出
5. 执行ORDER: 按列名排序输出, ASC升序, DESC降序
