https://nodejs.org/en/download/package-manager

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
nvm install 20
npm init
npm install express --save
```


## npm参数

| Para                    | Func             |
| ----------------------- | ---------------- |
| init                    | 初始化项目       |
| install                 | 拉取模块依赖     |
| install xxx             | 局部安装模块     |
| install -g              | 全局安装模块     |
| install --save(default) | 安装生产环境依赖 |
| install --save-dev      | 安装开发环境依赖 |
