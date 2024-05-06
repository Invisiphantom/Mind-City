![IMG_20240503_221324.jpg](https://s2.loli.net/2024/05/03/gLY3SmHVtylo2DB.jpg =500x)
- PC模块: 负责更新跳转PCaddress
- InstMem模块: 负责读取指令
- Control模块: 负责控制指令的译码
- ALUControl模块: 负责控制ALU执行的运算
- Regs模块: 负责寄存器读写
- RegsCSR模块: 负责CSR读写
- ImmGen模块: 负责生成立即数
- aluA模块: 负责选择与前递ALU的A端口数据
- aluB模块: 负责选择与前递ALU的B端口数据
- ALU模块: 负责执行运算
- BranchJudge模块: 负责判断是否跳转
- DataMem模块: 负责读写内存
- RegWrite模块: 负责选择写入寄存器的数据


RV64I流水线已实现的指令
- add, addw, sub, subw, xor, or, and, sll, srl, sra, sllw, srlw, sraw, slt, sltu
- addi, addiw, xori, ori, andi, slli, srli, srai, slliw, srliw, sraiw, slti, sltiu
- mul, mulw, mulh, mulhsu, mulhu, div, divw, divu, divuw, rem, remw, remu, remuw
- lb, lh, lw, ld, lbu, lhu, lwu, sb, sh, sw, sd
- beq, bne, blt, bge, bltu, bgeu, jal, jalr
- lui, auipc