
## WSL配置

C:\Users\16770\\.wslconfig
```
[experimental]
autoProxy=true
networkingMode=mirrored
```

```
[experimental]
autoProxy=false

[wsl2]
networkingMode=bridged
vmSwitch=WSLSwitch
```

```cmd
setx http_proxy http://127.0.0.1:7890
setx https_proxy http://127.0.0.1:7890

wsl --list
wsl --unregister Ubuntu-24.04
```


## bash配置

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

alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'
alias df='df -h'
alias du='du -c'
alias ps='ps axuc --forest'
alias update='sudo apt update && sudo apt upgrade -y'
export PATH=/usr/local/cuda/bin/:$PATH
export LIBRARY_PATH=$LIBRARY_PATH:/usr/lib/wsl/lib


# proxy_addr=110.40.135.15
proxy_addr=127.0.0.1
proxy_port=7890
function proxy_on() {
    export http_proxy=http://$proxy_addr:$proxy_port
    export https_proxy=http://$proxy_addr:$proxy_port
    export no_proxy=$proxy_addr,localhost
    export HTTP_PROXY=http://$proxy_addr:$proxy_port
    export HTTPS_PROXY=http://$proxy_addr:$proxy_port
    export NO_PROXY=$proxy_addr,localhost
}
function proxy_off(){
    unset http_proxy
    unset https_proxy
    unset no_proxy
    unset HTTP_PROXY
    unset HTTPS_PROXY
    unset NO_PROXY
}
proxy_on




update
sudo apt install -y gcc g++ gdb make cmake tree zip git-lfs net-tools openssh-server
git config --global user.name "Ethan Cao"
git config --global user.email 1677035769@qq.com
git lfs install
```

## frp配置

```bash

ssh -R 7890:localhost:7890 ten
wget https://github.com/fatedier/frp/releases/download/v0.61.0/frp_0.61.0_linux_amd64.tar.gz
nohup ./frps &


https://github.com/fatedier/frp/releases/download/v0.61.0/frp_0.61.0_windows_amd64.zip
frpc.exe -c frpc.toml


frpc.toml
serverAddr = "110.40.135.15"
serverPort = 7000

[[proxies]]
name = "clash-asus"
type = "tcp"
localIP = "127.0.0.1"
localPort = 7890
remotePort = 7890
```
