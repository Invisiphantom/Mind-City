# PostgreSQL配置
[Database Client](https://database-client.com/)
[PostgreSQL入门](https://www.bilibili.com/video/BV1Mi4y1K7HS/)
```bash
sudo apt install postgresql postgresql-contrib libecpg-dev
systemctl status postgresql
psql --version

sudo cat /etc/shadow
sudo passwd postgres
su postgres -c psql
ALTER USER postgres WITH PASSWORD '123456';

sudo vi /etc/postgresql/14/main/pg_hba.conf
# Database administrative login by Unix domain socket
local  all  postgres  peer -> md5
sudo systemctl reload postgresql

psql -U postgres -W

CREATE USER ethan WITH PASSWORD '123456' SUPERUSER;
CREATE DATABASE ethan OWNER ethan;
psql
```

# bserv配置

https://github.com/JonathanSilver/bserv

```bash
git clone --recursive https://github.com/JonathanSilver/bserv.git
cd bserv/dependencies/boost
./bootstrap.sh
./b2
sudo ./b2 install
cd ../cryptopp
make -j12
cd ../libpqxx
./configure
make

cd ../..
mkdir build && cd build
cmake ..
cmake --build . -j12

vi ../config-ubuntu.json
{
	"port": 8080,
	"thread-num": 2,
	"conn-num": 4,
	"conn-str": "postgresql://ethan:123456@127.0.0.1:5432/bserv",
	"static_root": "../../templates/statics",
	"template_root": "../../templates",
	"log-dir": "./log"
}
create database bserv;
CREATE TABLE auth_user (
    id serial PRIMARY KEY,
    username character varying(255) NOT NULL UNIQUE,
    password character varying(255) NOT NULL,
    is_superuser boolean NOT NULL,
    first_name character varying(255) NOT NULL,
    last_name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    is_active boolean NOT NULL
);

cd WebApp/
./WebApp ../../config-ubuntu.json
```

```json
// C/Cpp: Edit configurations
// c_cpp_properties.json
{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [
                "${workspaceFolder}/**",
                "/home/ethan/bserv/bserv/include",
                "/home/ethan/bserv/dependencies/libpqxx/include",
                "/home/ethan/bserv/dependencies/inja/include"
            ],
            "defines": [],
            "compilerPath": "/usr/bin/gcc",
            "intelliSenseMode": "linux-gcc-x64"
        }
    ],
    "version": 4
}
```


# bserv语法


```cpp
#include <bserv/common.hpp>
#include <boost/json.hpp>
#include <string>

int main()
{
	bserv::server_config config;
	bserv::server{config, {
		bserv::make_path(
			"/greet", &greet,
			bserv::placeholders::_1),
		bserv::make_path(
			"/greet/<str>/and/<str>", &greet2,
			bserv::placeholders::_1,
			bserv::placeholders::_2)
	}};
}
```

```cpp
    // std::shared_ptr<bserv::session_type>
    constexpr placeholder<-1> session;
    // bserv::request_type&
    constexpr placeholder<-2> request;
    // bserv::response_type&
    constexpr placeholder<-3> response;
    // boost::json::object&&
    constexpr placeholder<-4> json_params;
    // std::shared_ptr<bserv::db_connection>
    constexpr placeholder<-5> db_connection_ptr;
    // std::shared_ptr<bserv::http_client>
    constexpr placeholder<-6> http_client_ptr;
    // std::shared_ptr<bserv::websocket_server>
    constexpr placeholder<-7> websocket_server_ptr;
```


## 响应Any

```cpp
bserv::make_path("/hello", &hello)
boost::json::object hello() {
    return {{"msg", "hello, world!"}};
}
```

## 响应Get

```cpp
bserv::make_path(
    "/greet/<str>/and/<str>", &greet2,
    bserv::placeholders::_1,
    bserv::placeholders::_2
)
boost::json::object greet2(
	const std::string& name1,
	const std::string& name2)
{
	return {
		{"name1", name1},
		{"name2", name2}
	};
}
```

## 响应Post

```cpp
bserv::make_path(
    "/echo", &echo,
    bserv::placeholders::json_params
)
boost::json::object echo(
	boost::json::object&& params) {
	return params;
}
```



