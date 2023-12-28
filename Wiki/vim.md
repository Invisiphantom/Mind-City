vim - Vi IMproved, a programmer's text editor

------

| Option | Description       |
| ------ | -------------- |
| -      | 从标准输入读取 |
| -R     | 只读模式       |
| -b    | 二进制模式     |


```
Normal mode
    /pattern 搜索pattern
    n 下一个搜索结果
    N 上一个搜索结果
    hjkl 上下左右
    gg 文件首
    G 文件尾
    nG 第n行
    0 行首
    $ 行尾
    i 插入字符
    a 追加字符
    I 插入行首
    A 追加行尾
    x 删除字符
    w 下一个单词
    b 上一个单词
    e 下一个单词的末尾
    yw 复制单词
    dw 剪切单词
    cw 修改单词
    o 插入下一行
    O 插入上一行
    yy 复制整行
    dd 剪切整行
    cc 修改整行
    p 粘贴
    u 撤销
    ctrl+r 重做
    . 重复上一次操作

Visual mode
    v 进入可视模式
    V 进入可视行模式
    ctrl+v 进入可视块模式
    y 复制
    d 剪切
    c 修改

Command-line mode
    :wq 保存并退出
    :q! 不保存退出
    :w 保存
    :q 退出
    :e! 撤销所有修改
    :set number 显示行号
    :set nonu 不显示行号
    :set relativenumber 显示相对行号
    :%s/old/new/g 全局替换

```