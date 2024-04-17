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
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDsOPasY+BHAoHRLbC/qYXtXN16FkecK+p6kTdX8rOqjdBoywrKETffxtWTB+bc0qTP7twO3LP3942mn/8op/8mMz9D0B9EtQJV4fwJh/BXNvWrfg093tLYj9bAsi7SP1tyLgFc+al09a/istVWWmHczustorsxoH96mU4mUrm92iDj6/kvOFew3bP66mzKrYc3W52cOMbMEEQAyd42bBQOAo24mewu4dudYm2Dh+ISSgjILHAsfLS67FGPAoZbqE2ic/iq9G16WZjEGpyrou68FLK/Rzf5hJZ7VIa24Cn9WK3ZhWGW3EpiPtEu/4GgYD3pzIygqae5za2bgN144ucCRK+xmkVzq0gxIchSdvp2FdSB2cpUAK++WofkjWLC1tiJ2RMUtFYkFilCCnUd/XyLrFjtVH7iO6g0K/D15fhSKTGZuAO/LzQ37jakWowO2YFIiNPP+r5ZWvMAex0cJmRmrj4n4T0Q/sHTazU2udbeXjvyx28s9S18J82umlH/tDk= 16770@Ethan-Surface
```