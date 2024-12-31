
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
bcdedit /set hypervisorlaunchtype off
bcdedit /set hypervisorlaunchtype auto

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

## frp配置

```bash
wget https://github.com/fatedier/frp/releases/download/v0.61.0/frp_0.61.0_linux_amd64.tar.gz
nohup ./frps &

https://github.com/fatedier/frp/releases/download/v0.61.0/frp_0.61.0_windows_amd64.zip
frpc.exe -c frpc.toml
```

frpc.toml
```toml
serverAddr = "110.40.135.15"
serverPort = 7000

[[proxies]]
name = "clash-asus"
type = "tcp"
localIP = "127.0.0.1"
localPort = 7890
remotePort = 7890
```

## Ubuntu配置

https://github.com/ventoy/Ventoy/releases
https://ubuntu.com/download/desktop

https://github.com/clash-verge-rev/clash-verge-rev/releases
https://www.clashverge.dev/faq/linux.html

https://xiguayun.pw/link/PwUlY64zoNUiCYzZ?clash=1
https://submit.xz61.cn:20443/api/v1/client/subscribe?token=acf63b53750436b3920d86b0e7051640

https://code.visualstudio.com/download
https://www.microsoft.com/zh-cn/edge/download?form=MA13FJ

https://www.youtube.com/watch?v=Cy4Zo9-Tn-c
https://www.pling.com/p/1670979/

```bash
sudo apt install -y chrome-gnome-shell gnome-tweaks libfuse2t64 wine64 wine32
rm -rf ~/.wine && winecfg

cd ~/Downloads/
sudo apt install -y ostree appstream-util
git clone https://github.com/refi64/stylepak.git
cd stylepak/
./stylepak install-user

cd ~/Downloads/
git clone https://github.com/yeyushengfan258/Win11-icon-theme.git
cd Win11-icon-theme/
./install.sh -a

cd ~/Downloads/
git clone https://github.com/mrbvrz/segoe-ui-linux.git
cd segoe-ui-linux/
./install.sh

HH:mm\nyyyy/MM/dd
```

界面字体: Segoe UI (11)
文档字体: Segoe UI (11)
等宽字体: Cascadia Code (11)
光标: Fluent-cursors
图标: Win11-blue-dark
Shell: Yaru-blue-dark

https://extensions.gnome.org/
https://extensions.gnome.org/extension/19/user-themes/
https://extensions.gnome.org/extension/1160/dash-to-panel/
https://extensions.gnome.org/extension/3628/arcmenu/
https://extensions.gnome.org/extension/4655/date-menu-formatter/
https://extensions.gnome.org/extension/6661/wallhub/
https://extensions.gnome.org/extension/779/clipboard-indicator/
