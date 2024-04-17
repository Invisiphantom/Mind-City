## clash配置

https://apiv2.pptiok2020.com/apiv2/cxsjm8zuhcouxrbi?clash=1&extend=1
https://xiguayun.pw/link/PwUlY64zoNUiCYzZ?clash=1

## Ubuntu配置

```shell
wsl --list
wsl --unregister Ubuntu-22.04
```

```bash
# Shell Color Config (with git branch)
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ <\1>/'
}

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;33m\]$(parse_git_branch)\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt


host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
export https_proxy="http://$host_ip:7890"
export http_proxy="http://$host_ip:7890"
export all_proxy="sock5://$host_ip:7890"
export ALL_PROXY="sock5://$host_ip:7890"

alias apt='apt -o Acquire::http::proxy="http://$host_ip:7890/"'
```


## SSH服务器

https://www.zerotier.com/download/
https://my.zerotier.com/

```bash
sudo apt install openssh-server
sudo service ssh start
sudo service ssh status

curl -s https://install.zerotier.com | sudo bash
sudo zerotier-cli join 35c192ce9b6b3b60
ssh ethan@192.168.196.1
```

```bash
C:\Users\16770>
ssh-keygen -t rsa

cd ~/.ssh
vi authorized_keys
I id_rsa.pub
```