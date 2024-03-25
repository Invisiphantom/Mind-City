https://nodejs.org/en/download/package-manager

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install 20
npm init
npm install express --save
```


## npm参数

| Para                        | Func             |
| --------------------------- | ---------------- |
| npm init                    | 初始化项目       |
| npm login                   | 登录npm          |
| npm install                 | 拉取依赖模块     |
| npm install xxx             | 局部安装模块     |
| npm install -g              | 全局安装模块     |
| npm install --save(default) | 安装生产环境依赖 |
| npm install --save-dev      | 安装开发环境依赖 |

## yarn参数

| Para         | Func       |
| ------------ | ---------- |
| yarn init    | 初始化项目 |
| yarn add xxx | 安装模块   |


## 内置模块

| Module  | Func        |
| ------- | ----------- |
| http    | HTTP服务器  |
| url     | URL解析     |
| mysql   | MySQL数据库 |
| pg      | PostgreSQL  |
| notestn | 自动热重启  |


处理GET请求
```javascript
const http = require("http");
const url = require("url");

const server = http.createServer((req, res) => {
    res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});
    const reqUrl = req.url;
    const formVal = url.parse(reqUrl, true).query;
    console.log(formVal.userName, formVal.userPwd);
    res.end("用户名: "+formVal.userName+" 密码: "+formVal.userPwd);
});

server.listen(8080);
```


处理POST请求
```javascript
const http = require("http");
const querystring = require("querystring");

const server = http.createServer((req, res) => {
    let postVal = "";
    req.on("data", (chunk) => {
        postVal += chunk;
    });
    req.on("end", () => {
        console.log( querystring.parse(postVal) );
        res.end();
    });
});
server.listen(8080);
```


访问MySQL数据库
```javascript
const mysql = require('mysql');
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'test',
    port: 3306
});
connection.connect();
connection.query("SELECT * FROM user", (err, rows) => {
    if (err) throw err;
    console.log('Data received from Db:');
    console.log(rows);
    res.end();
});
connection.end();
```


访问PostgreSQL数据库
```javascript
const pg = require('pg');
const client = new pg.Client({
    host: "localhost",
    user: "ethan",
    password: "123456",
    database: "test",
    port: 5432
});
client.connect();
client.query('SELECT * FROM user', (err, res) => {
    console.log(res.rows);
    client.end();
});
```

登录系统
```javascript
const http = require("http");
const querystring = require("querystring");
const mysql = require("mysql");

const server = http.createServer((req, res) => {
    let postVal = "";
    req.on("data", (chunk) => {
        postVal += chunk;
    });
    req.on("end", () => {
        const formVal = querystring.parse(postVal);
        const userName = formVal.userName;
        const userPwd = formVal.userPwd;

        const connection = mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: '123456',
            database: 'test',
            port: 3306
        });
        connection.connect();
        connection.query("SELECT * FROM user WHERE userName = ? AND userPwd = ?", [userName, userPwd], (err, rows) => {
            if (err) throw err;
            if(rows.length > 0) {
                res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});
                res.write("登录成功");
                res.end();
            }
            else {
                res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});
                res.write("登录失败");
                res.end();
            }
        });
        connection.end();
    });
});
server.listen(8080);
```

注册系统
```javascript
const http = require("http");
const querystring = require("querystring");
const mysql = require("mysql");

const server = http.createServer((req, res) => {
    if (req.url !== "/favicon.ico") {
        let postVal = "";
        req.on("data", (chunk) => {
            postVal += chunk;
        });
        req.on("end", () => {
            const formVal = querystring.parse(postVal);
            const userName = formVal.userName;
            const userPwd = formVal.userPwd;

            const connection = mysql.createConnection({
                host: 'localhost',
                user: 'root',
                password: '123456',
                database: 'test',
                port: 3306
            });
            connection.connect();
            connection.query("INSERT INTO user VALUES (?, ?, ?)", [0, userName, userPwd], (err, result) => {
                if (err) throw err;
                res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
                res.end("注册成功");
            });

            connection.end();
        });
    }
});
server.listen(8080);
```


Express写回
```javascript
const express = require("express");


const test_router = express.Router();
test_router.get("/", (req, res) => {
    res.send({ "name": "小明", "age": 18 });
    res.end();
});

// 这样就能保证在访问/test时，会调用test_router的get方法
const app = express();
app.use("/test", test_router);


app.listen(3000, () => {
    console.log("http://localhost:3000");
});
```