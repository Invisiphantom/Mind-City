## clash配置

https://apiv2.pptiok2020.com/apiv2/cxsjm8zuhcouxrbi?clash=1&extend=1
https://xiguayun.pw/link/PwUlY64zoNUiCYzZ?clash=1

## Ubuntu配置

C:\Users\16770\\.wslconfig
```
[experimental]
autoProxy=true
networkingMode=mirrored
```

```bash
wsl --list
wsl --unregister Ubuntu-24.04
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

alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'
alias df='df -h'
alias du='du -c'
alias ps='ps axuc --forest'
alias update='sudo apt update && sudo apt upgrade -y'
export PATH=/usr/local/cuda/bin/:$PATH
export LIBRARY_PATH=$LIBRARY_PATH:/usr/lib/wsl/lib

proxy_port=7890
function proxy_on() {
    export http_proxy=http://127.0.0.1:$proxy_port
    export https_proxy=http://127.0.0.1:$proxy_port
    export no_proxy=127.0.0.1,localhost
    export HTTP_PROXY=http://127.0.0.1:$proxy_port
    export HTTPS_PROXY=http://127.0.0.1:$proxy_port
    export NO_PROXY=127.0.0.1,localhost
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


```cmd
setx http_proxy http://127.0.0.1:7890
setx https_proxy http://127.0.0.1:7890
```
