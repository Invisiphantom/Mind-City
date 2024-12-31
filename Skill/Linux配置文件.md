
## WSL配置

C:\Users\16770\\.wslconfig
```
[experimental]
autoProxy=true
networkingMode=mirrored
```

```cmd
wsl --list
wsl --unregister Ubuntu-24.04
setx http_proxy http://127.0.0.1:7890
setx https_proxy http://127.0.0.1:7890
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


## Ubuntu配置

```bash
sudo apt install -y chrome-gnome-shell gnome-tweaks
dconf dump /org/gnome/terminal/ > GTerm.conf
dconf load /org/gnome/terminal/ < GTerm.conf
```

https://img.ethancao.cn/fonts.zip
https://extensions.gnome.org/
https://extensions.gnome.org/extension/19/user-themes/
https://extensions.gnome.org/extension/1160/dash-to-panel/
https://extensions.gnome.org/extension/3628/arcmenu/
https://extensions.gnome.org/extension/6661/wallhub/
https://extensions.gnome.org/extension/779/clipboard-indicator/
