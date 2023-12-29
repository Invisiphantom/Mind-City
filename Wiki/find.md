find - search for files in a directory hierarchy

------

| Option           | Description                  |
| ---------------- | ---------------------------- |
| `-name`          | 指定文件名                   |
| `-type(d f l)`   | 指定文件类型(目录 文件 链接) |
| `-size`          | 指定文件大小                 |
| `-1K +1M`        | 大于1K 小于1M                |
| `-mtime(-7 +7)`  | 指定修改时间(7天内 7天前)    |
| `-user`          | 指定文件所有者               |
| `-delete`        | 删除                         |
| `-exec`          | 执行                         |
| `-exec rm {} \;` | 删除这些文件                 |
