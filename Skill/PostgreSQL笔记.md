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
CREATE DATABASE ethan;
psql
```

## PostgreSQL语法

| 语法              | 描述             |
| ----------------- | ---------------- |
| *General          | ---------        |
| \copyright        | 显示分发条款     |
| \g                | 执行查询         |
| \q                | 退出             |
| *Help             | ---------        |
| \?                | PSQL命令帮助     |
| \h                | SQL命令帮助      |
| *Input/Output     | ---------        |
| \i                | 导入文件         |
| \o                | 导出文件         |
| *Informational    | ---------        |
| \d                | 列出表,视图,序列 |
| \dn               | 列出模式         |
| \du               | 列出用户         |
| \dt               | 列出表           |
| \dv               | 列出视图         |
| \ds               | 列出序列         |
| \di               | 列出索引         |
| \l                | 列出数据库       |
| *Connection       | ---------        |
| \c                | 连接数据库       |
| \conninfo         | 显示连接信息     |
| \encoding         | 显示或设置编码   |
| \password         | 更改用户密码     |
| *Operating System | ---------        |
| \cd               | 切换目录         |
| \setenv           | 设置环境变量     |
| \\!               | 执行Shell命令    |
| *Variables        | ---------        |
| \set              | 设置变量         |
| \unset            | 删除变量         |