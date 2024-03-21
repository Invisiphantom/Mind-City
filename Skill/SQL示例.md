学生关系 S(S#, SNAME, AGE, SEX)
选课关系 SC(S#, SCORE, C#)
课程关系 C(C#, CNAME, T#)
教师关系 T(T#, TNAME, TITLE)


- 创建各基本表
```sql
CREATE TABLE S (
    S#      CHAR(4) NOT NULL,
    SNAME   CHAR(8) NOT NULL,
    AGE     SMALLINT,
    SEX     CHAR(1),
    PRIMARY KEY (S#)
);

CREATE TABLE SC (
    S#      CHAR(4) NOT NULL,
    SCORE   SMALLINT,
    C#      CHAR(4),
    PRIMARY KEY (S#, C#),
    FOREIGN KEY (S#) REFERENCES S(S#),
    FOREIGN KEY (C#) REFERENCES C(C#)
);

CREATE TABLE C (
    C#      CHAR(4) NOT NULL,
    CNAME   CHAR(10) NOT NULL,
    T#      CHAR(4),
    PRIMARY KEY (C#),
    FOREIGN KEY (T#) REFERENCES T(T#)
);

CREATE TABLE T (
    T#      CHAR(4) NOT NULL,
    TNAME   CHAR(8) NOT NULL,
    TITLE   CHAR(10),
    PRIMARY KEY (T#)
);
```

- 检索学习课程号为C2的学生学号和姓名
```sql
-- 连接查询: 先笛卡尔积, 再选择
SELECT S.S#, S.SNAME
FROM S, SC
WHERE S.S# = SC.S# AND SC.C# = 'C2';

-- 嵌套查询: 先从SC选出学习C2课程的学号, 再从S中选出学号和姓名
SELECT S#, SNAME
FROM S
WHERE S# IN (
    SELECT S#
    FROM SC 
    WHERE C# = 'C2');

-- 相关子查询: 对于S中的每行学生, 从SC中选出对应的课程, 如果有C2则输出
SELECT S#, SNAME
FROM S
WHERE 'C2' IN ( -- 判断C2是否在这些课程中
    SELECT C# -- 选出当前学生选的所有课程
    FROM SC 
    WHERE S# = S.S#);

-- 存在量词的相关子查询: 对于S中的每行学生, 从SC中选出对应的C2课程, 如果存在则输出
SELECT S#, SNAME
FROM S
WHERE EXISTS ( -- 判断是否存在 当前学生选的C2课程
    SELECT * -- 选出当前学生选的C2课程
    FROM SC
    WHERE S# = S.S# AND C# = 'C2');
```

- 检索至少选修LIU老师的一门课的学生学号和姓名
```sql
-- 连接查询
SELECT S.S#, S.SNAME
FROM S, SC, CT, T
WHERE (S.S# = SC.S# AND SC.C# = CT.C# AND CT.T# = T.T#) AND T.TNAME = 'LIU';

-- 嵌套查询
SELECT S#, SNAME
FROM S
WHERE S# IN (
    SELECT S# -- 选出LIU老师课程的学生学号
    FROM SC
    WHERE C# IN (
        SELECT C# -- 选出LIU老师的课程号
        FROM CT
        WHERE T# IN (
            SELECT T# -- 选出LIU老师的工号
            FROM T
            WHERE TNAME = 'LIU')));
```

- 检索至少选修课程号为C2和C4的学生学号和姓名
```sql
SELECT X.S#, X.SNAME
FROM SC AS X, SC AS Y
WHERE X.S# = Y.S# AND X.C# = 'C2' AND Y.C# = 'C4';
```

- 检索不学C2课程的学生学号和姓名
```sql
-- 嵌套查询
SELECT S#, SNAME
FROM S
WHERE S# NOT IN ( -- 选出不在这些学号中的学生
    SELECT S# -- 选出学习C2课程的学生学号
    FROM SC
    WHERE C# = 'C2');

-- 存在量词
SELECT S#, SNAME
FROM S
WHERE NOT EXISTS ( -- 判断当前学生 是否存在C2课程
    SELECT * -- 选出当前学生选择的C2课程
    FROM SC
    WHERE S# = S.S# AND C# = 'C2');
```

- 检索学习全部课程的学生学号和姓名
```sql
-- 存在量词
SELECT S#, SNAME -- 如果当前学生没有 没选的课, 则输出
FROM S
WHERE NOT EXISTS ( -- 判断是否存在 当前学生没有选的课程
    SELECT * -- 选出当前学生没有选的课程
    FROM CT
    WHERE C# NOT IN (
        SELECT C# -- 选出当前学生选的所有课程
        FROM SC
        WHERE S# = S.S#));
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
SELECT C#
FROM SC
WHERE S# = 'S3';

SELECT DISTINCT S#
FROM SC AS SC1
WHERE NOT EXISTS ( -- 不存在这样的S3课程
    SELECT * -- 选择 S3课程(它没有被该学生选修)
    FROM S3_COURSE
    WHERE NOT EXISTS (
        SELECT * -- 某学生 与 某门S3课, 
        FROM SC AS SC2
        WHERE SC2.S# = SC1.S# AND SC2.C# = S3_COURSE.C#));
```



- 计算男学生的总人数和平均年龄
```sql
SELECT COUNT(*), AVG(AGE)
FROM S
WHERE SEX='M'
```

- 计算选过课的学生人数
```sql
SELECT COUNT(DISTINCT S#)
FROM SC
```

- 统计每门课的选课人数, 显示课程号, 课程名和选课人数
```sql
SELECT C.C#, C.CNAME, COUNT(*)
FROM C, SC
WHERE C.C# = SC.C#
GROUP BY C.C#, C.CNAME
```

- 统计每个教师每门课的选课人数(超过50人), 显示教师号, 课程号和选课人数
查询结果按人数升序, 工号升序, 课程号降序排列
```sql
SELECT C.T#, C.C#, COUNT(SC.S#)
FROM C, SC
WHERE C.C# = SC.C#
GROUP BY C.T#, C.C#
    HAVING COUNT(SC.S#) > 50
ORDER BY COUNT(SC.S#) ASC, C.T# ASC, C.C# DESC
```

- 在基本表S中检索每个学生的姓名和出生年份,
输出的列名为STUDENT_NAME, BIRTH_YEAR
```sql
SELECT SNAME AS STUDENT_NAME, 2024-AGE AS BIRTH_YEAR
FROM S
```

- 在基本表S中检索18-20岁的学生姓名
```sql
SELECT SNAME
FROM S
WHERE AGE BETWEEN 18 AND 20
```

- 在基本表S中检索以字符D开头的学生姓名
```sql
SELECT SNAME
FROM S
WHERE SNAME LIKE 'D%'
```

- 在基本表S中检索年龄为空值的学生姓名
```sql
SELECT SNAME
FROM S
WHERE AGE IS NULL
```

- 在基本表S中检索C2和C4都没学的学生姓名
```sql
SELECT SNAME
FROM S
WHERE S# NOT IN (
    SELECT S#
    FROM SC
    WHERE C# IN ('C2', 'C4'))
```

- 检索至少有一门成绩超过学生S4的一门成绩的学生学号
```sql
SELECT DISTINCT S#
FROM SC
WHERE SCORE > SOME (
    SELECT SCORE
    FROM SC
    WHERE S# = 'S4')
```


- 检索只开设一门课程的教师号和姓名
```sql
SELECT T#, TNAME
FROM T
WHERE UNIQUE (
    SELECT T#
    FROM C
    WHERE C.T# = T.T#)
```

- 检索平均成绩最高的学生学号
```sql
SELECT S#
FROM SC
GROUP BY S#
ORDER BY AVG(SCORE) DESC
LIMIT 1;

SELECT S#
FROM SC
GROUP BY S#
HAVING AVG(SCORE) >= ALL(
        SELECT AVG(SCORE)
        FROM SC
        GROUP BY S#);

SELECT SC.S#
FROM SC, (
    SELECT AVG(SCORE)
    FROM SC
    GROUP BY S#) AS RESULT(AVG_SCORE)
GROUP BY SC.S#
HAVING AVG(SCORE) >= ALL(RESULT.AVG_SCORE);

WITH RESULT(AVG_SCORE) AS (
    SELECT AVG(SCORE)
    FROM SC
    GROUP BY S#)
SELECT SC.S#
FROM SC, RESULT
GROUP BY SC.S#
HAVING AVG(SCORE) >= ALL(RESULT.AVG_SCORE);
```


已知课程先修与直接后继关系 COURSE(C#, CNAME, PC#)
临时视图 PRE(C#, PC#) 表示直接或间接先修关系
1. PRE(x,y) <- COURSE(x,u,y)
2. PRE(x,z) <- COURSE(x,u,y) AND PRE(y,z)
```sql
WITH RECURSIVE PRE(C#, PC#) AS (
    (SELECT C#, PC# FROM COURSE)
    UNION
    (SELECT COURSE.C#, PRE.PC#
    FROM COURSE, PRE
    WHERE COURSE.PC# = PRE.C#))
SELECT * FROM PRE;
```

- 往基本表S中插入元组('S36', 'GU', 20, 'M')
```sql
INSERT INTO S(S#, SNAME, AGE, SEX)
VALUES ('S36', 'GU', 20, 'M')
```

- 把C5课程的课程名改为'DB'
```sql
UPDATE C
SET CNAME = 'DB'
WHERE C# = 'C5'
```

- C4课程的成绩低于平均成绩时, 提高5%
```sql
UPDATE SC
SET SCORE = SCORE * 1.05
WHERE C# = 'C4' AND SCORE < (
    SELECT AVG(SCORE)
    FROM SC
    WHERE C# = 'C4')
```