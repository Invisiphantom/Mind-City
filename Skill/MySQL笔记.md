Ubuntu22.04配置MySQL环境

```bash
sudo apt install mysql-server
systemctl status mysql
sudo cat /etc/mysql/debian.cnf
mysql -u debian-sys-maint -p
```

```sql
use mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
FLUSH PRIVILEGES;
```

<br>

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

SELECT语句
```sql
SELECT * FROM player LIMIT 10;
SELECT name FROM player;
SELECT * from player WHERE level > 1 AND level < 10
SELECT * from player WHERE level BETWEEN 1 AND 10
SELECT * from player WHERE level IN (1, 2, 3, 4, 5)
```