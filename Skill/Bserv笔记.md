[](https://github.com/JonathanSilver/bserv)

```bash
git clone --recurse-submodules https://github.com/JonathanSilver/bserv.git

cd boost
./boostrap.sh
./b2
sudo ./b2 install

cd cryptopp
make

cd libpqxx
./configure
make
sudo apt install libpq-dev
sudo ldconfig



cd examples
mkdir build && cd build
cmake ..
cmake --build .
./hello
curl http://localhost:8080/hello
./routing
curl http://localhost:8080/greet/world
curl http://localhost:8080/greet/world1/and/world2
curl http://localhost:8080/echo?hello=world
curl -X POST -H "Content-Type: application/json" -d '{"hello": "world"}' http://localhost:8080/echo


cd ~/bserv
create database bserv;
psql bserv < db.sql
mv config-ubuntu.json config.json
code config.json
modify: "conn-str": "postgresql://ethan:123456@localhost:5432/bserv",

mkdir build && cd build
cmake ..
cmake --build .
cd WebApp
./WebApp ../../config.json
```

Windows访问WSL的localhost
```bash
ip a |grep "global eth0"
netstat -tuln
```


C_Cpp.SelectIntelliSenseConfiguration -> use cmake-tools
