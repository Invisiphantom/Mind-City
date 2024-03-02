
|  名称  | 前景色 | 背景色 |      Ubuntu      |
| :----: | :----: | :----: | :--------------: |
|  黑色  |   30   |   40   |    rgb(1,1,1)    |
|  红色  |   31   |   41   |  rgb(222,56,43)  |
|  绿色  |   32   |   42   |  rgb(57,181,74)  |
|  黄色  |   33   |   43   |  rgb(255,199,6)  |
|  蓝色  |   34   |   44   |  rgb(0,111,184)  |
|  洋红  |   35   |   45   | rgb(118,38,113)  |
|  青色  |   36   |   46   | rgb(44,181,233)  |
|  白色  |   37   |   47   | rgb(204,204,204) |
| 亮黑色 |   90   |  100   | rgb(128,128,128) |
| 亮红色 |   91   |  101   |   rgb(255,0,0)   |
| 亮绿色 |   92   |  102   |   rgb(0,255,0)   |
| 亮黄色 |   93   |  103   |  rgb(255,255,0)  |
| 亮蓝色 |   94   |  104   |   rgb(0,0,255)   |
| 亮洋红 |   95   |  105   |  rgb(255,0,255)  |
| 亮青色 |   96   |  106   |  rgb(0,255,255)  |
| 亮白色 |   97   |  107   | rgb(255,255,255) |


终端颜色设置(添加git分支显示)
```bash
# Shell Color Config(with git branch)
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ <\1>/'
}

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;33m\]$(parse_git_branch)\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt
```