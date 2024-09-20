

ARMv8 指令集


| Level | Desc       |
| ----- | ---------- |
| EL0   | 用户空间   |
| EL1   | 内核空间   |
| EL2   | 虚拟机管理 |
| EL3   | 安全监视器 |


| Regs     | Function                               | 功能           |
| -------- | -------------------------------------- | -------------- |
| PC       | Program Counter Register               | 程序计数器     |
| XZR      | Zero Register                          | 零值寄存器     |
| X0-X7    | Parameter and Result Registers         | 传参和返回值   |
| X8 (XR)  | Indirect Result Location Register      | 间接结果       |
| X9-X15   | Caller Saved Registers                 | 调用者保存     |
| X16-X17  | Intra-procedure Call Scratch Registers | 程序内调用     |
| X18 (PR) | Platform Register                      | 平台寄存器     |
| X19-X28  | Callee Saved Registers                 | 被调用者保存   |
| X29 (FP) | Frame Pointer Register                 | 帧指针寄存器   |
| X30 (LR) | Link Register                          | 返回地址寄存器 |



|                                         | EL0    | EL1       | EL2       | EL3       |
| --------------------------------------- | ------ | --------- | --------- | --------- |
| Stack Pointer                           | SP_EL0 | SP_EL1    | SP_EL2    | SP_EL3    |
| Exception Link Register                 |        | ELR_EL1   | ELR_EL2   | ELR_EL3   |
| Saved Processor State Register          |        | SPSR_EL1  | SPSR_EL2  | SPSR_EL3  |
| System Control Register                 |        | SCTLR_EL1 | SCTLR_EL2 | SCTLR_EL3 |
| Translation Table Base Registers (Low)  |        | TTBR0_EL1 | TTBR0_EL2 | TTBR0_EL3 |
| Translation Table Base Registers (High) |        | TTBR1_EL1 | TTBR1_EL2 |           |




| PSTATE | Desc                                       |
| ------ | ------------------------------------------ |
| N      | Negative flag                              |
| Z      | Zero flag                                  |
| C      | Carry flag                                 |
| V      | oVerflow flag                              |
| D      | Debug mask bit                             |
| A      | SError mask bit                            |
| I      | IRQ mask bit                               |
| F      | FIQ mask bit                               |
| SS     | Software Step bit                          |
| IL     | Illegal Execution State bit                |
| EL     | Exception level                            |
| nRW    | Execution state        (0:64-bit 1:32-bit) |
| SP     | Stack Pointer selector (0:SP_EL0 1:SP_ELn) |



