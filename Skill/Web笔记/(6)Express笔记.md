
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