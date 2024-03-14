[Verilator文档](https://veripool.org/guide/latest/)

## Verilator环境配置
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

## Verilator参数

| Para       | Func             |
| ---------- | ---------------- |
| -Wall      | 打开所有警告     |
| --Mdir     | 指定生成文件目录 |
| --sc       | 生成SystemC代码  |
| --cc       | 生成C++代码      |
| --exe      | 生成可执行文件   |
| --build -j | make并行编译     |
| --trace    | 生成波形文件     |

## Verilator测试


```json
// code-runner
".v": "cd $dir && verilator -Wall --Mdir bin --cc --exe --build -j --trace $fileName $fileNameWithoutExt.cpp && cd bin && rm -rf !(V$fileNameWithoutExt|V$fileNameWithoutExt.h) && ./V$fileNameWithoutExt && gtkwave wave.vcd",
// c_cpp_properties.json
{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [
                "${workspaceFolder}/**",
                "/usr/local/share/verilator/include"
            ],
            "defines": [],
            "compilerPath": "/usr/bin/gcc",
            "intelliSenseMode": "linux-gcc-x64"
        }
    ],
    "version": 4
}
```

```verilog
// and_gate.v
module and_gate (
    input  a,
    input  b,
    output f
);
    assign f = a & b;
endmodule

```

```cpp
// and_gate.cpp
#include "Vand_gate.h"
#include <iostream>
#include <verilated_vcd_c.h>

using namespace std;

vluint64_t main_time = 0;
double sc_time_stamp() { return main_time; }

int main(int argc, char **argv) {
    Verilated::commandArgs(argc, argv);
    Verilated::traceEverOn(true);

    VerilatedVcdC *tfp = new VerilatedVcdC();
    Vand_gate *top = new Vand_gate("top");
    top->trace(tfp, 0);
    tfp->open("wave.vcd");

    for (; main_time < 20 && !Verilated::gotFinish(); main_time++) {
        auto a = top->a;
        auto b = top->b;

        switch (main_time) {
        case 0:
            a = 0;
            b = 0;
            break;
        case 5:
            a = 1;
            b = 0;
            break;
        case 10:
            a = 0;
            b = 1;
            break;
        case 15:
            a = 1;
            b = 1;
            break;
        default:
            break;
        }

        top->a = a;
        top->b = b;

        top->eval();
        tfp->dump(main_time);
        printf("%ld: a = %d, b = %d, f = %d\n", main_time, a, b, top->f);
    }
}
```
```
