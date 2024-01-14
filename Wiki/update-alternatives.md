update-alternatives - maintain symbolic links determining default commands


```
$ update-alternatives --help
用法：update-alternatives [<选项> ...] <命令>

命令：
  --install <链接> <名称> <路径> <优先级>
    [--slave <链接> <名称> <路径>] ...
                           在系统中加入一组候选项。
  --remove <名称> <路径>   从 <名称> 替换组中去除 <路径> 项。
  --remove-all <名称>      从替换系统中删除 <名称> 替换组。
  --auto <名称>            将 <名称> 的主链接切换到自动模式。
  --display <名称>         显示关于 <名称> 替换组的信息。
  --query <名称>           机器可读版的 --display <名称>.
  --list <名称>            列出 <名称> 替换组中所有的可用候选项。
  --config <名称>          列出 <名称> 替换组中的可选项，并就使用其中哪一个，征询用户的意见。
  --set <名称> <路径>      将 <路径> 设置为 <名称> 的候选项。
  --all                    对所有可选项一一调用 --config 命令。

<链接> 是指向 /etc/alternatives/<名称> 的符号链接。(如 /usr/bin/pager)
<名称> 是该链接替换组的主控名。(如 pager)
<路径> 是候选项目标文件的位置。(如 /usr/bin/less)
<优先级> 是一个整数，在自动模式下，这个数字越高的选项，其优先级也就越高。
```


使用实例：Ubuntu22.04安装g++-13
```bash
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
sudo update-alternatives --remove-all cpp

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 20 \
--slave /usr/bin/g++ g++ /usr/bin/g++-13 \
--slave /usr/bin/cpp cpp /usr/bin/cpp-13 \
--slave /usr/bin/cc1 cc1 /usr/libexec/gcc/x86_64-linux-gnu/13/cc1 \
--slave /usr/bin/cc1plus cc1plus /usr/libexec/gcc/x86_64-linux-gnu/13/cc1plus

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 10 \
--slave /usr/bin/g++ g++ /usr/bin/g++-11 \
--slave /usr/bin/cpp cpp /usr/bin/cpp-11 \
--slave /usr/bin/cc1 cc1 /usr/libexec/gcc/x86_64-linux-gnu/11/cc1 \
--slave /usr/bin/cc1plus cc1plus /usr/libexec/gcc/x86_64-linux-gnu/11/cc1plus

sudo update-alternatives --config gcc
```