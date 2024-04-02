https://nodejs.org/en/download/package-manager

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install 20
npm init
npm install -g nodemon
npm install express
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


| HTTP Status | Desc     |
| 200         | 请求成功 |
| 201         | 创建成功 |
| 404         | 未找到   |
| 500         | 服务器错误 |



处理GET请求
```html
<!-- index.html -->
<form method="get" action="http://localhost:8080">
    <input type="text" name="userName">
    <input type="password" name="userPwd">
    <input type="submit" value="登录">
</form>
```
```js
// server.js
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
```html
<!-- index.html -->
<form method="post" action="http://localhost:8080">
    <input type="text" name="userName">
    <input type="password" name="userPwd">
    <input type="submit" value="登录">
</form>
```
```js
const http = require("http");
const querystring = require("querystring");

const server = http.createServer((req, res) => {
    let postVal = "";
    req.on("data", (chunk) => {
        postVal += chunk;
    });
    req.on("end", () => {
        const formVal = querystring.parse(postVal);
        console.log(formVal.userName, formVal.userPwd);
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        res.end("用户名: " + formVal.userName + " 密码: " + formVal.userPwd);
    });
});
server.listen(8080);
```


访问MySQL数据库
```js
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
```js
const pg = require('pg');
const client = new pg.Client({
    host: "localhost",
    user: "ethan",
    password: "123456",
    database: "ethan",
    port: 5432
});
client.connect();
client.query('SELECT * FROM user', (err, res) => {
    console.log(res.rows);
    client.end();
});
```

登录系统
```js
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
```js
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
```js
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

## Express用法

| Func                          | Desc         |
| ----------------------------- | ------------ |
| app.set("view engine", "ejs") | 设置模板引擎 |
| app.set("views", "./views")   | 设置模板路径 |
| app.use("/path", middleWare)  | 使用中间件   |
| app.get(path, callback)       | GET请求      |
| app.post(path, callback)      | POST请求     |
| app.put(path, callback)       | PUT请求      |
| app.delete(path, callback)    | DELETE请求   |
| app.listen(port, callback)    | 监听端口     |
| res.set()                     | 设置头部     |
| res.status()                  | 设置状态码   |
| res.send()                    | 返回数据     |
| res.end()                     | 结束请求     |


示例:
```js
// index.js
const express = require('express');
const pg = require('pg');

// 建立与 PostgreSQL 数据库的连接
const client = new pg.Client({
    host: "localhost",
    user: "ethan",
    password: "123456",
    database: "ethan"
});
client.connect();

// 创建服务器处理请求
const app = express();

// 处理 GET 请求
app.set("view engine", "ejs");
app.set("views", "./views");
app.get('/', (req, res) => {
    client.query('SELECT * FROM users', (error, results) => {
        if (error) {
            throw error;
        }
        const users = results.rows;
        res.render('index', { users: users });
    });
});

// 处理 POST 请求
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.post("/", (req, res) => {
    const username = req.body.username;
    const userpwd = req.body.userpwd;

    // 向 PostgreSQL 数据库插入数据
    const query = 'INSERT INTO users (username, userpwd) VALUES ($1, $2)';
    const values = [username, userpwd];
    client.query(query, values, (err, result) => {
        if (err) {
            console.error('Error inserting data:', err);
            res.status(500).send('Error inserting data');
        } else {
            console.log('Data inserted successfully');
            res.redirect('/');
        }
    });

});

// 监听端口
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});
```

index.ejs
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post" action="http://localhost:3000/">
        <input type="text" name="username">
        <input type="password" name="userpwd">
        <input type="submit" value="Submit">
    </form>

    <table>
        <tr>
            <td>Name</td>
            <td>Password</td>
        </tr>

        <% for (let i = 0; i < users.length; i++) { %>
            <tr>
                <td><%= users[i].username %></td>
                <td><%= users[i].userpwd %></td>
            </tr>
        <% } %>
    </table>


</body>
</html>
```