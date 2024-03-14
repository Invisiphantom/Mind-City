

模块接口命名规范
考虑时序的要求，注意不允许组合电路输出，需要使用寄存器输出
|    信号类型    |    命名规范     |
| :------------: | :-------------: |
|    时钟信号    |       clk       |
|    复位信号    |      reset      |
| 顶层文件名命名 | [file_name]_top |
|  模块端口输入  |  [pin_name]_i   |
|  模块端口输出  |  [pin_name]_o   |
| 模块内部寄存器 |  [reg_name]_r   |
|  模块内部连线  |  [wire_name]_w  |
| 低电平有效信号 |  [pin_name]_n   |



`include "../include/common.sv"
