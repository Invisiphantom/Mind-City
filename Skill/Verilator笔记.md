环境配置
```bash
git clone https://github.com/verilator/verilator.git
cd verilator
git checkout v4.210
sudo apt install perl make autoconf g++ flex bison ccache gtkwave
autoconf
./configure
make -j12 or -j4
sudo make uninstall
sudo make install
verilator --version
```

