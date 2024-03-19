## MySQL资料链接

[一小时MySQL教程](https://www.bilibili.com/video/BV1AX4y147tA)
[5分钟精通MySql框架](https://www.bilibili.com/video/BV1ve411F794)

## MySQL环境配置

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

## MySQL语法

创建与删除数据库
```sql
CREATE DATABASE game;
SHOW DATABASES;
DROP DATABASE game;
```


导入与导出数据库
```bash
mysql -u root -p game < game.sql
mysqldump -u root -p game > game.sql
```


创建与删除表
```sql
CREATE TABLE `player` (
  `id` int DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `level` int DEFAULT '1',
  `exp` int DEFAULT NULL,
  `gold` decimal(10,2) DEFAULT NULL
);
SHOW TABLES;
DESC player;
DROP TABLE player;
```

<br>

SELECT查询操作
```sql
SELECT name FROM player;
SELECT * FROM player LIMIT 10;
SELECT * FROM player WHERE level > 1 AND level < 10;
SELECT * FROM player WHERE level BETWEEN 1 AND 10;
SELECT * FROM player WHERE level IN (1, 2, 3, 4, 5);
SELECT * FROM player WHERE name LIKE '王%';
SELECT * FROM player WHERE name LIKE '王_';
SELECT * FROM player WHERE name REGEXP '^[王李].$';
SELECT * FROM player WHERE email IS NULL;
SELECT * FROM player ORDER BY level ASC;
SELECT * FROM player ORDER BY level DESC, exp DESC;
SELECT COUNT(*) FROM player;
SELECT sum(gold) FROM player;
SELECT AVG(level) FROM player;
SELECT level, COUNT(level) FROM player GROUP BY level;
SELECT level, COUNT(level) FROM player GROUP BY level HAVING COUNT(level) > 4;
SELECT level, COUNT(level) FROM player GROUP BY level HAVING COUNT(level) > 4 ORDER BY COUNT(level) DESC;

SELECT SUBSTR(name, 1, 1), COUNT(SUBSTR(name, 1, 1)) FROM player
GROUP BY SUBSTR(name, 1, 1)
HAVING COUNT(SUBSTR(name, 1, 1)) >= 5
ORDER BY COUNT(SUBSTR(name, 1, 1)) DESC;

SELECT DISTINCT level FROM player ORDER BY level;

SELECT * FROM player WHERE level BETWEEN 1 AND 3
UNION SELECT * FROM player WHERE exp BETWEEN 1 AND 3;

SELECT * FROM player WHERE level BETWEEN 1 AND 3
INTERSECT SELECT * FROM player WHERE exp BETWEEN 1 AND 3;

SELECT * FROM player WHERE level BETWEEN 1 AND 3
EXCEPT SELECT * FROM player WHERE exp BETWEEN 1 AND 3;

SELECT id, name, level, ROUND((SELECT AVG(level) FROM player)) as average,
 level - ROUND((SELECT AVG(level) FROM player)) as diff
 FROM player ORDER BY level DESC LIMIT 90, 20

CREATE TABLE new_player SELECT * FROM player WHERE level < 10;
INSERT INTO new_player SELECT * FROM player WHERE level >= 90;

SELECT EXISTS(SELECT * FROM player WHERE level = 1);
```

<br>

JOIN关联操作
```sql
SELECT * FROM player
INNER JOIN equip
on player.id = equip.player_id;

SELECT * FROM player, equip; -- 笛卡尔积

SELECT * FROM player, equip
WHERE player.id = equip.player_id; -- 隐式内连接

SELECT * FROM player
LEFT JOIN equip
on player.id = equip.player_id;

SELECT * FROM player
RIGHT JOIN equip
on player.id = equip.player_id;
```

INIDEX索引操作
```sql
CREATE INDEX code_index ON area(code);
SHOW INDEX FROM area;
SELECT * FROM area WHERE code LIKE '41032%';
DROP INDEX code_index ON area;
```

VIEW视图操作
```sql
CREATE VIEW top10 AS
SELECT * FROM player ORDER BY level DESC LIMIT 10;

-- 视图会随着原表的变化而变化
UPDATE player SET level = 99 WHERE id = 57;

DROP VIEW top10;
```