Ubuntu22.04配置MySQL环境

```bash
sudo apt install mysql-server
systemctl status mysql
systemctl start mysql
sudo cat /etc/mysql/debian.cnf
sudo mysql_secure_installation
mysql -u debian-sys-maint -p
H7m6n0gWVjQZxWU5
```

```sql
use mysql
SHOW VARIABLES LIKE 'validate_password%';
SET GLOBAL validate_password.length = 6;
SET GLOBAL validate_password.number_count = 0;
SET GLOBAL validate_password.policy = 0;
alter user 'root'@'%' identified with mysql_native_password by '123456';
```