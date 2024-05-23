## Git资料

[一小时Git教程](https://www.bilibili.com/video/BV1HM411377j)

## Git用法

git config配置信息
```bash
git config --global user.name "Ethan Cao"
git config --global user.email 1677035769@qq.com
git config --global credential.helper store
git config --global init.defaultBranch main
git config --global --unset user.password
git config --global --list
```

git init新建仓库
```bash
git init Demo
```

git clone克隆仓库
```bash
git clone https://github.com/Invisiphantom/Demo.git
```

git status查看状态
```bash
git status
```

git ls-files查看暂存区
```bash
git ls-files
```

git add添加文件
```bash
git add .
git add file1.txt
```

git commit提交
```bash
git commit -m "add file1.txt"
```

git log查看提交历史
```bash
git log
git log --oneline
```


git reset回退版本
```bash
# HEAD^ 上一个版本
git reset --soft  4a35b40  # 保留工作区和保留暂存区
git reset --mixed 4a35b40  # 保留工作区和回退暂存区
git reset --hard  4a35b40  # 回退工作区和回退暂存区
```

git reflog查看命令历史
```bash
git reflog
```

git diff比较文件
```bash
git diff # 比较工作区与暂存区
git diff HEAD # 比较工作区与版本库
git diff --cached # 比较暂存区与版本库
git diff 6940bc6 4a35b40 # 比较两个版本
git diff HEAD~2 HEAD file3.txt # 比较当前版本与上上个版本中的file3.txt
```

git rm删除文件
```bash
git rm file1.txt # 删除工作区和暂存区
git rm --cached file1.txt # 只删除暂存区
```

.gitingore忽略文件([参考文档](https://git-scm.com/docs/gitignore/zh_HANS-CN))
从下往上逐行匹配, 每行表示一个匹配规则
| 符号  | 说明           |
| ----- | -------------- |
| /     | 表示目录       |
| !     | 表示取反       |
| **    | 匹配任意目录   |
| *     | 匹配任意个字符 |
| ?     | 匹配一个字符   |
| [abc] | 匹配a或b或c    |


git push推送到远程仓库
```bash
git push
git push -u origin main:main # 关联远程仓库
```

git pull拉取远程仓库
```bash
git pull
```

git remote add添加远程仓库
```bash
git remote add origin git@github.com:***/***.git
```

git branch查看分支
```bash
git branch
git branch -d dev # 删除已合并的dev分支
git branch -D dev # 强制删除dev分支
```

git switch切换分支
```bash
git switch -c dev # 创建dev分支
git switch main
```

git merge合并分支
```bash
git switch main
git merge dev
```

git rebase变基
```bash
git switch dev
git rebase main # 将dev分支变基到main分支后
```

git checkout撤销修改
```bash
git checkout -b dev a4a333c # 从a4a333c创建dev分支
```