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
export all_proxy="socks5://$host_ip:7890"
export ALL_PROXY="socks5://$host_ip:7890"

alias apt='apt -o Acquire::http::proxy="http://$host_ip:7890/"'
```

```bash
git config --global user.name "Ethan Cao"
git config --global user.email 1677035769@qq.com
```


## SSH服务器

```bash
sudo apt install openssh-server
sudo service ssh start
sudo service ssh status

wget https://pgy.oray.com/softwares/153/download/2156/PgyVisitor_6.2.0_x86_64.deb
dpkg -i PgyVisitor_6.2.0_x86_64.deb
pgyvisitor autologin -y
pgyvisitor login
orkj980241faslk0
cyl2004...
```

```bash
C:\Users\16770>
ssh-keygen -t rsa

mkdir ~/.ssh
vi ~/.ssh/authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC7YJgwtjdJdHVwEVEgt6vMUIIgJBggc/ABaFSFh2uKxbyPjfl7iYFcM62tLjYE6ScsuOlrrQ8NEVVthDVk9kESzyQ4Rff6ypITax/ib1dZol7MiKbEG3jZYVrQ26nB4hwJcP6teyc0Z2qL2S8FQqcc2An2zDPmqb9ZN7vuNyAoYdL+4j4tVf0F4G2XLifSaYzdMaGhFWLZnWZeRenLrcCZGqJQeeMji88IvUo6X3iF8EHTL7XIJUX+C8/Z/df/x1YcWme7M+8jHoDxhKCZDdp+ZUBh83VZNPrTs4hbsz6NOHMwUquu7LWKeffrkdrI5Gl9H7hGhY8aeFkY75VwNwgctLcOKLiTwpZangV49+1gknaga/p8Vte/GhGJ+kEAsN/xKAI5LddWix0MI4WFSijlRZ5e939iw2KCS21l2+IckTIRgFVrZG2vYZR2umEFwEfJ1lZYRznAE0f6Gv7qFq5ckv/uy9kssmU6g52LIXyIG7eUemMGR12QySog/obbB6U= 16770@Ethan-Surface
```

