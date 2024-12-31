# MySQL环境配置

[一小时MySQL教程](https://www.bilibili.com/video/BV1AX4y147tA)
[5分钟精通MySql框架](https://www.bilibili.com/video/BV1ve411F794)

```bash
sudo apt install mysql-server
systemctl status mysql
sudo cat /etc/mysql/debian.cnf
mysql -u debian-sys-maint -p
```

```sql
USE mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
FLUSH PRIVILEGES;
sudo mysql -u root -p
```



# PostgreSQL配置
[Database Client](https://database-client.com/)
[PostgreSQL入门](https://www.bilibili.com/video/BV1Mi4y1K7HS/)
```bash
sudo apt install postgresql postgresql-contrib libecpg-dev
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


# PostgreSQL语法

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



# SQL基本数据类型

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

# SQL语法

## 数据库, 基本表, 索引, 视图

创建数据库: `CREATE DATABASE <name> [AUTHORIZATION <user>]`
删除数据库: `DROP DATABASE <name> [CASCADE|RESTRICT]`
1. CASCADE: 删除数据库的同时删除数据库中的所有表
2. RESTRICT: 只有在数据库中没有表的情况下才能删除数据库


创建基本表:
```sql
CREATE TABLE <name> (
    <column> <type> [NOT NULL] [DEFAULT <value>] [CKECK (<condition>)],
    ...
    [PRIMARY KEY (<column>)]
    [FOREIGN KEY (<column>) REFERENCES <table>(<column>)]
)
```
修改基本表
```sql
-- 删除旧列
ALTER TABLE <name> DROP <column>;
-- 增加新列
ALTER TABLE <name> ADD <column> <type> [NOT NULL] [DEFAULT <value>] [CKECK (<condition>)];
-- 修改现有列
ALTER TABLE <name> MODIFY <column> <type> [NOT NULL] [DEFAULT <value>] [CKECK (<condition>)];
```
删除基本表: `DROP TABLE <name> [CASCADE|RESTRICT]`


创建索引: `CREATE [UNIQUE] INDEX <name> ON <table> (<column>[ASC|DESC]);`
删除索引: `DROP INDEX <name>`


创建视图: `CREATE VIEW <name>(<列名序列>) AS <SELECT语句>`
删除视图: `DROP VIEW <name>`

## SELECT查询操作

```sql
[WITH [RECURSIVE] <视图名> AS (<视图查询>)]
SELECT [ALL|DISTINCT]<列表达式序列|*>[AS <新列名>]
FROM <基本表序列|视图序列>
[WHERE <行条件表达式>]
[GROUB BY <列名序列>
    HAVING <组条件表达式>]
[ORDER BY <列名[ASC|DESC]>]
[LIMIT <行数> [OFFSET <行数>] | FETCH FIRST <行数> ROWS ONLY]
```

1. 执行FROM: 读取基本表或视图, 进行笛卡尔积
2. 执行WHERE: 选择满足行条件表达式的元组
3. 执行GROUP: 按列名序列分组, 同时提取满足HAVING的组
4. 执行SELECT: 按给定列名和列表达式序列求值输出
5. 执行ORDER: 按列名排序输出, ASC升序, DESC降序

聚合函数
1. COUNT(*): 计算元组的个数
2. COUNT(col): 计算列中的非空行数
3. SUM(col): 计算列中的数值之和
4. AVG(col): 计算列中的数值平均值
5. MAX(col): 计算列中的最大值
6. MIN(col): 计算列中的最小值

SELECT列表达式:
1. 列表达式: +,-,*,/,列名,常量
2. DISTINCT: 去除重复元组
3. ALL: 保留重复元组(默认)
4. AS: 重命名列名
5. *: 选取所有列

WHERE条件子句中的运算符:
1. 限定判断: `op ALL|SOME`
2. 比较判断: `=,>,<,>=,<=,!=`
3. 之内判断: `[NOT] IN`
4. 存在判断: `[NOT] EXISTS`
5. 唯一判断: `[NOT] UNIQUE`
6. 空值判断: `IS [NOT] NULL`
7. 区间判断: `[NOT] BETWEEN AND`
8. 匹配判断: `[NOT] LIKE %_ [ESCAPE '\']`
9. 逻辑运算符: `AND,OR,NOT`
10. 聚合函数: `COUNT,SUM,AVG,MAX,MIN`
11. 嵌套查询: `SELECT`

SELECT查询结果的交,并,差运算:
1. 交: `INTERSECT [ALL]`
2. 并: `UNION [ALL]`
3. 差: `EXCEPT [ALL]`
4. ALL: 保留重复元组(默认消重)


连接类型:
1. JOIN: 笛卡尔积
2. LEFT JOIN: 左连接
3. RIGHT JOIN: 右连接
4. FULL JOIN: 全连接

连接条件:
1. NATURAL: 合并公共属性
2. USING: 指定连接属性
3. ON: 指定连接条件

## INSERT插入操作

```sql
INSERT INTO <表名> [(<列名序列>)]
    VALUES(<元组序列>);

INSERT INTO <表名> [(<列名序列>)]
    <SELECT语句>

INSERT INTO <表名> [(<列名序列>)]
    TABLE <表名>;
```

## DELETE删除操作

```sql
DELETE FROM <表名>
    [WHERE <行条件表达式>];
```

## UPDATE更新操作

```sql
UPDATE <表名>
    SET <列名> = <表达式> | ROW = (<元组>)
    [WHERE <行条件表达式>];
```


CASE语句




[](https://github.com/JonathanSilver/bserv)

```bash
git clone --recurse-submodules https://github.com/JonathanSilver/bserv.git

cd boost
./boostrap.sh
./b2
sudo ./b2 install

cd cryptopp
make

cd libpqxx
./configure
make
sudo apt install libpq-dev
sudo ldconfig



cd examples
mkdir build && cd build
cmake ..
cmake --build .
./hello
curl http://localhost:8080/hello
./routing
curl http://localhost:8080/greet/world
curl http://localhost:8080/greet/world1/and/world2
curl http://localhost:8080/echo?hello=world
curl -X POST -H "Content-Type: application/json" -d '{"hello": "world"}' http://localhost:8080/echo


cd ~/bserv
create database bserv;
psql bserv < db.sql
mv config-ubuntu.json config.json
code config.json
modify: "conn-str": "postgresql://ethan:123456@localhost:5432/bserv",

mkdir build && cd build
cmake ..
cmake --build .
cd WebApp
./WebApp ../../config.json
```

