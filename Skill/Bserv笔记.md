[](https://github.com/JonathanSilver/bserv)

```bash
git clone --recurse-submodules https://github.com/JonathanSilver/bserv.git

cd boost
./bootstrap
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
mkdir build && cd build
cmake ..
cmake --build .
cd WebApp
./WebApp ../../config.json
```


```json
{
    "C_Cpp.default.configurationProvider": "ms-vscode.cmake-tools"
}
```