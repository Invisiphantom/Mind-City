RISC-V中文手册

https://github.com/Tan-YiFan/rvcpu

ISA设计的七种衡量标准
1. 成本(美元硬币)
2. 简洁性(轮子)
3. 性能(速度计)
4. 架构与实现分离(分开半圆)
5. 提升空间(手风琴)
6. 程序大小(箭头)
7. 易于编程/编译/链接(abc)


R型指令: 用于寄存器-寄存器操作
I型指令: 用于短立即数, 读存操作
S型指令: 用于写存操作
B型指令: 用于分支操作
U型指令: 用于长立即数
J型指令: 用于跳转操作



| 编号 | 别称  | 功能                           |
| ---- | ----- | ------------------------------ |
| x0   | zero  | Hardwired zero                 |
| x1   | ra    | Return address                 |
| x2   | sp    | Stack pointer                  |
| x3   | gp    | Global pointer                 |
| x4   | tp    | Thread pointer                 |
| x5   | t0    | Temporary                      |
| x6   | t1    | Temporary                      |
| x7   | t2    | Temporary                      |
| x8   | s0/fp | Saved register/Frame pointer   |
| x9   | s1    | Saved register                 |
| x10  | a0    | Function argument/Return value |
| x11  | a1    | Function argument/Return value |
| x12  | a2    | Function argument              |
| x13  | a3    | Function argument              |
| x14  | a4    | Function argument              |
| x15  | a5    | Function argument              |
| x16  | a6    | Function argument              |
| x17  | a7    | Function argument              |
| x18  | s2    | Saved register                 |
| x19  | s3    | Saved register                 |
| x20  | s4    | Saved register                 |
| x21  | s5    | Saved register                 |
| x22  | s6    | Saved register                 |
| x23  | s7    | Saved register                 |
| x24  | s8    | Saved register                 |
| x25  | s9    | Saved register                 |
| x26  | s10   | Saved register                 |
| x27  | s11   | Saved register                 |
| x28  | t3    | Temporary                      |
| x29  | t4    | Temporary                      |
| x30  | t5    | Temporary                      |
| x31  | t6    | Temporary                      |

![](img/RISC-V笔记-1.png)


| Inst    | Name                        | FMT | Opcode[6:0] | Funct3[14:12] | Funct7[31:25] | Description                               |
| ------- | --------------------------- | --- | ----------- | ------------- | ------------- | ----------------------------------------- |
| add     | ADD                         | R   | 0110011     | 000           | 0000000       | R[rd] = R[rs1] + R[rs2]                   |
| addw+   | ADD (W)                     | R   | 0111011     | 000           | 0000000       | R[rd] = sext((R[rs1] + R[rs2])[31:0])     |
| sub     | SUB                         | R   | 0110011     | 000           | 0100000       | R[rd] = R[rs1] - R[rs2]                   |
| subw+   | SUB (W)                     | R   | 0111011     | 000           | 0100000       | R[rd] = sext((R[rs1] - R[rs2])[31:0])     |
| xor     | XOR                         | R   | 0110011     | 100           | 0000000       | R[rd] = R[rs1] ^ R[rs2]                   |
| or      | OR                          | R   | 0110011     | 110           | 0000000       | R[rd] = R[rs1] \| R[rs2]                  |
| and     | AND                         | R   | 0110011     | 111           | 0000000       | R[rd] = R[rs1] & R[rs2]                   |
| sll     | Shift Left Logical          | R   | 0110011     | 001           | 0000000       | R[rd] = R[rs1] << R[rs2][4:0] [5:0]+      |
| srl     | Shift Right Logical         | R   | 0110011     | 101           | 0000000       | R[rd] = R[rs1] >> R[rs2][4:0] [5:0]+      |
| sra     | Shift Right Arith           | R   | 0110011     | 101           | 0100000       | R[rd] = R[rs1] >>> R[rs2][4:0] [5:0]+     |
| sllw+   | Shift Left Logical (W)      | R   | 0111011     | 001           | 0000000       | R[rd] = sext((R[rs1] << R[rs2])[31:0])    |
| srlw+   | Shift Left Logical (W)      | R   | 0111011     | 101           | 0000000       | R[rd] = sext((R[rs1] >> R[rs2])[31:0])    |
| sraw+   | Shift Left Logical (W)      | R   | 0111011     | 101           | 0100000       | R[rd] = sext((R[rs1] >>> R[rs2])[31:0])   |
| slt     | Set Less Than               | R   | 0110011     | 010           | 0000000       | R[rd] = (R[rs1] < R[rs2])?1:0             |
| sltu    | Set Less Than (U)           | R   | 0110011     | 011           | 0000000       | R[rd] = (R[rs1] < R[rs2])?1:0             |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| addi    | ADD Imm                     | I   | 0010011     | 000           |               | R[rd] = R[rs1] + imm                      |
| addiw+  | ADD Imm (W)                 | I   | 0011011     | 000           |               | R[rd] = sext((R[rs1] + imm)[31:0])        |
| xori    | XOR Imm                     | I   | 0010011     | 100           |               | R[rd] = R[rs1] ^ imm                      |
| ori     | OR Imm                      | I   | 0010011     | 110           |               | R[rd] = R[rs1] \| imm                     |
| andi    | AND Imm                     | I   | 0010011     | 111           |               | R[rd] = R[rs1] & imm                      |
| slli    | Shift Left Logical Imm      | I   | 0010011     | 001           | 000000(0-)    | R[rd] = R[rs1] << imm[4:0] [5:0]+         |
| srli    | Shift Right Logical Imm     | I   | 0010011     | 101           | 000000(0-)    | R[rd] = R[rs1] >> imm[4:0] [5:0]+         |
| srai    | Shift Right Arith Imm       | I   | 0010011     | 101           | 010000(0-)    | R[rd] = R[rs1] >>> imm[4:0] [5:0]+        |
| slliw+  | Shift Left Logical Imm (W)  | I   | 0011011     | 001           | 0000000       | R[rd] = sext((R[rs1] << imm[4:0])[31:0])  |
| srliw+  | Shift Right Logical Imm (W) | I   | 0011011     | 101           | 0000000       | R[rd] = sext((R[rs1] >> imm[4:0])[31:0])  |
| sraiw+  | Shift Right Arith Imm (W)   | I   | 0011011     | 101           | 0100000       | R[rd] = sext((R[rs1] >>> imm[4:0])[31:0]) |
| slti    | Set Less Than Imm           | I   | 0010011     | 010           |               | R[rd] = (R[rs1] < imm)?1:0                |
| sltiu   | Set Less Than Imm (U)       | I   | 0010011     | 011           |               | R[rd] = (R[rs1] < imm)?1:0                |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| lb      | Load Byte                   | I   | 0000011     | 000           |               | R[rd] = M[R[rs1] + imm][7:0]              |
| lh      | Load Half                   | I   | 0000011     | 001           |               | R[rd] = M[R[rs1] + imm][15:0]             |
| lw      | Load Word                   | I   | 0000011     | 010           |               | R[rd] = M[R[rs1] + imm][31:0]             |
| ld+     | Load Doubleword             | I   | 0000011     | 011           |               | R[rd] = M[R[rs1] + imm][63:0]             |
| lbu     | Load Byte (U)               | I   | 0000011     | 100           |               | R[rd] = M[R[rs1] + imm][7:0]              |
| lhu     | Load Half (U)               | I   | 0000011     | 101           |               | R[rd] = M[R[rs1] + imm][15:0]             |
| lwu+    | Load Word (U)               | I   | 0000011     | 110           |               | R[rd] = M[R[rs1] + imm][31:0]             |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| sb      | Store Byte                  | S   | 0100011     | 000           |               | M[R[rs1] + imm][7:0] = R[rs2][7:0]        |
| sh      | Store Half                  | S   | 0100011     | 001           |               | M[R[rs1] + imm][15:0] = R[rs2][15:0]      |
| sw      | Store Word                  | S   | 0100011     | 010           |               | M[R[rs1] + imm][31:0] = R[rs2][31:0]      |
| sd+     | Store Doubleword            | S   | 0100011     | 011           |               | M[R[rs1] + imm][63:0] = R[rs2][63:0]      |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| beq     | Branch ==                   | B   | 1100011     | 000           |               | if (R[rs1] == R[rs2]) PC += imm           |
| bne     | Branch !=                   | B   | 1100011     | 001           |               | if (R[rs1] != R[rs2]) PC += imm           |
| blt     | Branch <                    | B   | 1100011     | 100           |               | if (R[rs1] <  R[rs2]) PC += imm           |
| bge     | Branch >=                   | B   | 1100011     | 101           |               | if (R[rs1] >= R[rs2]) PC += imm           |
| bltu    | Branch <  (U)               | B   | 1100011     | 110           |               | if (R[rs1] <  R[rs2]) PC += imm           |
| bgeu    | Branch >= (U)               | B   | 1100011     | 111           |               | if (R[rs1] >= R[rs2]) PC += imm           |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| jal     | Jump And Link               | J   | 1101111     |               |               | R[rd] = PC + 4; PC += imm                 |
| jalr    | Jump And Link Register      | I   | 1100111     | 000           |               | R[rd] = PC + 4; PC = R[rs1] + imm         |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| lui     | Load Upper Imm              | U   | 0110111     |               |               | R[rd] = imm << 12                         |
| auipc   | Add Upper Imm to PC         | U   | 0010111     |               |               | R[rd] = PC + (imm << 12)                  |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| fence   | Fence                       | I   | 0001111     | 000           | 0000          |                                           |
| fence.i | Fence.i                     | I   | 0001111     | 001           | 0000000       |                                           |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| ecall   | Environment Call            | I   | 1110011     | 000           | 0000000       |                                           |
| ebreak  | Environment Breakpoint      | I   | 1110011     | 000           | 0000000       |                                           |
| ------- | ------                      | --- | -------     | ------        | -------       | ---------                                 |
| csrrw   | CSR Read Write              | I   | 1110011     | 001           |               |                                           |
| csrrs   | CSR Read Set                | I   | 1110011     | 010           |               |                                           |
| csrrc   | CSR Read Clear              | I   | 1110011     | 011           |               |                                           |
| csrrwi  | CSR Read Write Imm          | I   | 1110011     | 101           |               |                                           |
| csrrsi  | CSR Read Set Imm            | I   | 1110011     | 110           |               |                                           |
| csrrci  | CSR Read Clear Imm          | I   | 1110011     | 111           |               |                                           |


