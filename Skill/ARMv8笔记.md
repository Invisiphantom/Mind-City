

https://img.ethancao.cn/Armv8-Ref.pdf
https://img.ethancao.cn/ARMv8%20Instruction.pdf
https://cs140e.sergio.bz/docs/ARMv8-A-Programmer-Guide.pdf

https://armv8-doc.readthedocs.io/en/latest/06.html
https://courses.cs.washington.edu/courses/cse469/19wi/arm64.pdf






| General   | Desc                         |
| --------- | ---------------------------- |
| x0        | Param and RetVal             |
| x1        | Param                        |
| x2        | Param                        |
| x3        | Param                        |
| x4        | Param                        |
| x5        | Param                        |
| x6        | Param                        |
| x7        | Param                        |
| x8        | Caller Saved / Struct RetVal |
| x9        | Caller Saved                 |
| x10       | Caller Saved                 |
| x11       | Caller Saved                 |
| x12       | Caller Saved                 |
| x13       | Caller Saved                 |
| x14       | Caller Saved                 |
| x15       | Caller Saved                 |
| x16 (IP0) | Veneers Scratch              |
| x17 (IP1) | Veneers Scratch              |
| x18 (PR)  | Platform Register            |
| x19       | Callee Saved                 |
| x20       | Callee Saved                 |
| x21       | Callee Saved                 |
| x22       | Callee Saved                 |
| x23       | Callee Saved                 |
| x24       | Callee Saved                 |
| x25       | Callee Saved                 |
| x26       | Callee Saved                 |
| x27       | Callee Saved                 |
| x28       | Callee Saved                 |
| x29 (FP)  | Frame Pointer                |
| x30 (LR)  | Return Address               |
| xzr       | Zero Register                |






| Special   | Desc                        |
| --------- | --------------------------- |
| pc        | Program Counter             |
| sp        | Stack Pointer               |
|           |                             |
| ttbr0     | Translation Table Base 0    |
| ttbr1     | Translation Table Base 1    |
| mpidr     | Multi Processor ID          |
|           |                             |
| cntfrq    | Counter Frequency           |
| cntpct    | Counter Physical Count      |
| cntv_ctl  | Counter Virtual Control     |
| cntv_tval | Counter Virtual Timer Value |
|           |                             |
| spsr      | Saved Program Status        |
| elr       | Exception Link              |
| esr       | Exception Syndrome          |
| vbar      | Vector Base Address         |


异常或中断
1. spsr_el1 <- pstate
2. elr_el1 <- pc
3. esr_el1 <- Trap Info
4. sp_el0 <- sp
5. pc <- vbar_el1




| PSTATE | Desc                                       |
| ------ | ------------------------------------------ |
| N      | Negative flag                              |
| Z      | Zero flag                                  |
| C      | Carry flag                                 |
| V      | oVerflow flag                              |
|        |                                            |
| D      | Debug mask bit                             |
| A      | SError mask bit                            |
| I      | IRQ mask bit (Interrupt ReQuest)           |
| F      | FIQ mask bit (Fast Interrupt Request)      |
|        |                                            |
| SS     | Software Step bit                          |
| IL     | Illegal Execution State bit                |
| EL     | Exception level                            |
| nRW    | Execution state        (0:64-bit 1:32-bit) |
| SP     | Stack Pointer selector (0:SP_EL0 1:SP_ELn) |


| SPSR | Bit | Desc                                          |
| ---- | --- | --------------------------------------------- |
| N    | 31  | Negative flag                                 |
| Z    | 30  | Zero flag                                     |
| C    | 29  | Carry flag                                    |
| V    | 28  | oVerflow flag                                 |
|      |     |                                               |
| SS   | 21  | Software Step bit                             |
| IL   | 20  | Illegal Execution State bit                   |
|      |     |                                               |
| D    | 9   | Debug mask bit                                |
| A    | 8   | SError mask bit                               |
| I    | 7   | IRQ mask bit (Interrupt ReQuest)              |
| F    | 6   | FIQ mask bit (Fast Interrupt Request)         |
|      |     |                                               |
| M    | 4   | Exception Execution state (0:64-bit 1:32-bit) |
| M    | 3:0 | Exception Exception level                     |


| Page Table | Desc                  |
| ---------- | --------------------- |
| PGD        | Page Global Directory |
| PUD        | Page Upper Directory  |
| PMD        | Page Middle Directory |
| PTE        | Page Table Entry      |


| 64:48 | 47:39    | 38:30    | 29:21    | 20:12    | 11:0      |
| ----- | -------- | -------- | -------- | -------- | --------- |
|       | VA_PART0 | VA_PART1 | VA_PART2 | VA_PART3 | VA_OFFSET |


![](https://img.ethancao.cn/202410061649421.png)

![](https://segmentfault.com/img/remote/1460000044036626/view)

![](https://img.ethancao.cn/20241023111107.png)

| Inst | Desc                         |
| ---- | ---------------------------- |
| dsb  | Data Synchronization Barrier |
| isb  | Inst Synchronization Barrier |
| dc   | Data Cache                   |
| tlbi | TLB Invalidate               |
| svc  | Supervisor Call              |
| eret | Exception Return             |



![](https://img.ethancao.cn/2024_09_29_MyU7EODZC6lnsLX.png)

| ARMv8-A64 | Name                               | FMT | Opcode[31:x]    | Shamt[x:10] | Description                                       |
| --------- | ---------------------------------- | --- | --------------- | ----------- | ------------------------------------------------- |
| add{s}    | ADD                                | R   | 1_0S_01011_SF_0 | Imm6        | R[Rd] = R[Rn] + R[Rm].sf                          |
| sub{s}    | SUB                                | R   | 1_1S_01011_SF_0 | Imm6        | R[Rd] = R[Rn] - R[Rm].sf                          |
| add{s}    | ADD (Extend)                       | R   | 1_0S_01011_00_1 | Op3 Imm3    | R[Rd] = R[Rn] + R[Rm].ext                         |
| sub{s}    | SUB (Extend)                       | R   | 1_1S_01011_00_1 | Op3 Imm3    | R[Rd] = R[Rn] - R[Rm].ext                         |
| adc{s}    | AdD with Carry                     | R   | 1_0S_11010_00_0 | 000000      | R[Rd] = R[Rn] + R[Rm] + C                         |
| sbc{s}    | SuB with Carry                     | R   | 1_1S_11010_00_0 | 000000      | R[Rd] = R[Rn] - R[Rm] - ~C                        |
|           |                                    |     |                 |             |                                                   |
| and{s}    | AND                                | R   | 1_SS_01010_SF_0 | Imm6        | R[Rd] = R[Rn] & R[Rm].sf                          |
| bic{s}    | Bit Clear                          | R   | 1_SS_01010_SF_1 | Imm6        | R[Rd] = R[Rn] & ~R[Rm].sf                         |
| orr       | OR                                 | R   | 1_01_01010_SF_0 | Imm6        | R[Rd] = R[Rn] \| R[Rm].sf                         |
| eor       | Exclusive OR                       | R   | 1_10_01010_SF_0 | Imm6        | R[Rd] = R[Rn] ^ R[Rm].sf                          |
| orn       | OR NOT                             | R   | 1_01_01010_SF_1 | Imm6        | R[Rd] = R[Rn] \| ~R[Rm].sf                        |
| eon       | Exclusive OR NOT                   | R   | 1_10_01010_SF_1 | Imm6        | R[Rd] = R[Rn] ^ ~R[Rm].sf                         |
|           |                                    |     |                 |             |                                                   |
| lsl       | Logical Shift Left                 | R   | 1_00_11010_11_0 | 001000      | R[Rd] = R[Rn] << R[Rm]                            |
| lsr       | Logical Shift Right                | R   | 1_00_11010_11_0 | 001001      | R[Rd] = R[Rn] >> R[Rm]                            |
| asr       | Arithmetic Shift Right             | R   | 1_00_11010_11_0 | 001010      | R[Rd] = R[Rn] >>> R[Rm]                           |
| --------- |                                    |     |                 |             |                                                   |
| add{s}    | ADD                                | I   | 1_0S_100010_H   | Imm12       | R[Rd] = R[Rn] + Imm << (H ? 12 : 0)               |
| sub{s}    | SUB                                | I   | 1_1S_100010_H   | Imm12       | R[Rd] = R[Rn] - Imm << (H ? 12 : 0)               |
|           |                                    |     |                 |             |                                                   |
| and{s}    | AND                                | I   | 1_SS_100100_1   | Imm12       | R[Rd] = R[Rn] & Imm                               |
| orr       | OR                                 | I   | 1_01_100100_1   | Imm12       | R[Rd] = R[Rn] \| Imm                              |
| eor       | Exclusive OR                       | I   | 1_10_100100_1   | Imm12       | R[Rd] = R[Rn] ^ Imm                               |
|           |                                    |     |                 |             |                                                   |
| sbfm      | Signed BitField Move               | I   | 1_00_100110_1   | Immr Imms   | R[Rd] = [(R[Rn][Imms:0] o>> Immr) & oneSide].sext |
| ubfm      | Unsigned BitField Move             | I   | 1_10_100110_1   | Immr Imms   | R[Rd] = [(R[Rn][Imms:0] o>> Immr) & oneSide]      |
| --------- |                                    |     |                 |             |                                                   |
| movn      | MOVe with NOT                      | IM  | 1_00_100101_HW  |             | R[Rd] = ~{0, Imm[15:0] << 16HW, 0}                |
| movz      | MOVe with Zero                     | IM  | 1_10_100101_HW  |             | R[Rd] =  {0, Imm[15:0] << 16HW, 0}                |
| movk      | MOVe with Keep                     | IM  | 1_11_100101_HW  |             | R[Rd][+15:16HW] = Imm                             |
| --------- |                                    |     |                 |             |                                                   |
|           |                                    |     |                 |             | BAddr ={inst[25:0],00}.sext                       |
|           |                                    |     |                 |             | CBAddr={inst[18:0],00}.sext                       |
|           |                                    |     |                 |             |                                                   |
| br        | Branch to Register                 | R   | 11010110000     | 111110000   | PC = R[Rt]                                        |
| b         | Branch                             | B   | 0_00101         |             | PC += BAddr                                       |
| bl        | Branch with Link                   | B   | 1_00101         |             | R[30] = PC + 4; PC += BAddr                       |
| b.cond    | Branch CONDitional                 | CB  | 01010100        |             | if(FLAGS==cond) PC += CBAddr                      |
| cbnz      | Compare & Branch if Not Zero       | CB  | 10110101        |             | if(R[Rt] != 0)  PC += CBAddr                      |
| cbz       | Compare & Branch if Zero           | CB  | 10110100        |             | if(R[Rt] == 0)  PC += CBAddr                      |
| --------- |                                    |     |                 |             |                                                   |
|           |                                    |     |                 |             |                                                   |
| strb      | STore Register Byte                | R   | 00_111000_00_1  | Ext_S_10    | M[R[Rn] + R[Rm]][7:0] = R[Rt][7:0]                |
| strh      | STore Register Halfword            | R   | 01_111000_00_1  | Ext_S_10    | M[R[Rn] + R[Rm] << S ? 1:0][15:0] = R[Rt][15:0]   |
| str       | STore Register                     | R   | 10_111000_00_1  | Ext_S_10    | M[R[Rn] + R[Rm] << S ? 2:0][31:0] = R[Rt][31:0]   |
| str       | STore Register                     | R   | 11_111000_00_1  | Ext_S_10    | M[R[Rn] + R[Rm] << S ? 3:0][63:0] = R[Rt][63:0]   |
|           |                                    |     |                 |             | Imm >= 0                                          |
| strb      | STore Register Byte                | I   | 00_111001_00    | Imm12       | M[R[Rn] + Imm][7:0] = R[Rt][7:0]                  |
| strh      | STore Register Halfword            | I   | 01_111001_00    | Imm12       | M[R[Rn] + Imm][15:0] = R[Rt][15:0]                |
| str       | STore Register                     | I   | 10_111001_00    | Imm12       | M[R[Rn] + Imm][31:0] = R[Rt][31:0]                |
| str       | STore Register                     | I   | 11_111001_00    | Imm12       | M[R[Rn] + Imm][63:0] = R[Rt][63:0]                |
| stp       | STore Pair                         | I   | 10_101001_00    | Imm7        | M[R[Rn] + Imm][127:0] = R[Rt1], R[Rt2]            |
|           |                                    |     |                 |             | Imm < 0                                           |
| sturb     | STore Unscaled Register Byte       | D   | 00_111000000    | 00          | M[R[Rn] + Imm][7:0] = R[Rt][7:0]                  |
| sturh     | STore Unscaled Register Halfword   | D   | 01_111000000    | 00          | M[R[Rn] + Imm][15:0] = R[Rt][15:0]                |
| stur      | STore Unscaled Register            | D   | 10_111000000    | 00          | M[R[Rn] + Imm][31:0] = R[Rt][31:0]                |
| stur      | STore Unscaled Register            | D   | 11_111000000    | 00          | M[R[Rn] + Imm][63:0] = R[Rt][63:0]                |
| --------- |                                    |     |                 |             |                                                   |
|           |                                    |     |                 |             |                                                   |
| ldrsb     | LoaD Register Signed Byte          | R   | 00_111000_10_1  | Ext_S_10    | R[Rt] = M[R[Rn] + R[Rm]][7:0].sext                |
| ldrsh     | LoaD Register Signed Half          | R   | 01_111000_10_1  | Ext_S_10    | R[Rt] = M[R[Rn] + R[Rm] << S ? 1:0][15:0].sext    |
| ldrsw     | LoaD Register Signed Word          | R   | 10_111000_10_1  | Ext_S_10    | R[Rt] = M[R[Rn] + R[Rm] << S ? 2:0][31:0].sext    |
| ldrb      | LoaD Register Byte                 | R   | 00_111000_01_1  | Ext_S_10    | R[Rt] = M[R[Rn] + R[Rm]][7:0]                     |
| ldrh      | LoaD Register Half                 | R   | 01_111000_01_1  | Ext_S_10    | R[Rt] = M[R[Rn] + R[Rm] << S ? 1:0][15:0]         |
| ldr       | LoaD Register                      | R   | 10_111000_01_1  | Ext_S_10    | R[Rt] = M[R[Rn] + R[Rm] << S ? 2:0][31:0]         |
| ldr       | LoaD Register                      | R   | 11_111000_01_1  | Ext_S_10    | R[Rt] = M[R[Rn] + R[Rm] << S ? 3:0][63:0]         |
|           |                                    |     |                 |             | Imm >= 0                                          |
| ldrsb     | LoaD Register Signed Byte          | I   | 00_111001_10    | Imm12       | R[Rt] = M[R[Rn] + Imm][7:0].sext                  |
| ldrsh     | LoaD Register Signed Half          | I   | 01_111001_10    | Imm12       | R[Rt] = M[R[Rn] + Imm][15:0].sext                 |
| ldrsw     | LoaD Register Signed Word          | I   | 10_111001_10    | Imm12       | R[Rt] = M[R[Rn] + Imm][31:0].sext                 |
| ldrb      | LoaD Register Byte                 | I   | 00_111001_01    | Imm12       | R[Rt] = M[R[Rn] + Imm][7:0]                       |
| ldrh      | LoaD Register Half                 | I   | 01_111001_01    | Imm12       | R[Rt] = M[R[Rn] + Imm][15:0]                      |
| ldr       | LoaD Register                      | I   | 10_111001_01    | Imm12       | R[Rt] = M[R[Rn] + Imm][31:0]                      |
| ldr       | LoaD Register                      | I   | 11_111001_01    | Imm12       | R[Rt] = M[R[Rn] + Imm][63:0]                      |
| ldp       | LoaD Pair                          | I   | 10_101001_01    | Imm7        | R[Rt1], R[Rt2] = M[R[Rn] + Imm][127:0]            |
|           |                                    |     |                 |             | Imm < 0                                           |
| ldursb    | LoaD Unscaled Register Signed Byte | D   | 00_111000_10_0  | 00          | R[Rt] = M[R[Rn] + Imm][7:0].sext                  |
| ldursh    | LoaD Unscaled Register Signed Half | D   | 01_111000_10_0  | 00          | R[Rt] = M[R[Rn] + Imm][15:0].sext                 |
| ldursw    | LoaD Unscaled Register Signed Word | D   | 10_111000_10_0  | 00          | R[Rt] = M[R[Rn] + Imm][31:0].sext                 |
| ldurb     | LoaD Unscaled Register Byte        | D   | 00_111000_01_0  | 00          | R[Rt] = M[R[Rn] + Imm][7:0]                       |
| ldurh     | LoaD Unscaled Register Half        | D   | 01_111000_01_0  | 00          | R[Rt] = M[R[Rn] + Imm][15:0]                      |
| ldur      | LoaD Unscaled Register             | D   | 10_111000_01_0  | 00          | R[Rt] = M[R[Rn] + Imm][31:0]                      |
| ldur      | LoaD Unscaled Register             | D   | 11_111000_01_0  | 00          | R[Rt] = M[R[Rn] + Imm][63:0]                      |



| ARMv8-A64 | Name                   | FMT | Opcode[31:21] | Shamt[15:10] | Description                     |
| --------- | ---------------------- | --- | ------------- | ------------ | ------------------------------- |
| sdiv      | Signed DIVide          | R   | 1001101_0110  | 000010       | R[Rd] = R[Rn] / R[Rm]           |
| udiv      | Unsigned DIVide        | R   | 1001101_0110  | 000011       | R[Rd] = R[Rn] / R[Rm]           |
| mul       | MULtiply               | R   | 1001101_1000  | 011111       | R[Rd] = (R[Rn] * R[Rm])[63:0]   |
| smulh     | Signed MULtiply High   | R   | 1001101_1010  |              | R[Rd] = (R[Rn] * R[Rm])[127:64] |
| umulh     | Unsigned MULtiply High | R   | 1001101_1110  |              | R[Rd] = (R[Rn] * R[Rm])[127:64] |
| -----     |                        |     |               |              |                                 |
| fmuls     | Float MULtiply Single  | R   | 00011110001   | 0000_10      | S[Rd] = S[Rn] * S[Rm]           |
| fdivs     | Float DIVide Single    | R   | 00011110001   | 0001_10      | S[Rd] = S[Rn] / S[Rm]           |
| fadds     | Float ADD Single       | R   | 00011110001   | 0010_10      | S[Rd] = S[Rn] + S[Rm]           |
| fsubs     | Float SUBtract Single  | R   | 00011110001   | 0011_10      | S[Rd] = S[Rn] - S[Rm]           |
| fcmps     | Float CoMPare Single   | R   | 00011110001   | 0010_00      | FLAGS = S[Rn] vs S[Rm]          |
| -----     |                        |     |               |              |                                 |
| faddd     | Float ADD Double       | R   | 00011110011   | 001010       | D[Rd] = D[Rn] + D[Rm]           |
| fsubd     | Float SUBtract Double  | R   | 00011110011   | 001110       | D[Rd] = D[Rn] - D[Rm]           |
| fmuld     | Float MULtiply Double  | R   | 00011110011   | 000010       | D[Rd] = D[Rn] * D[Rm]           |
| fdivd     | Float DIVide Double    | R   | 00011110011   | 000110       | D[Rd] = D[Rn] / D[Rm]           |
| fcmpd     | Float CoMPare Double   | R   | 00011110011   | 001000       | FLAGS = D[Rn] vs D[Rm]          |
| -----     |                        |     |               |              |                                 |
| ldurs     | LoaD Single float      | R   | 10_111100010  |              | S[Rt] = M[R[Rn] + Imm]          |
| ldurd     | LoaD Double float      | R   | 11_111100010  |              | D[Rt] = M[R[Rn] + Imm]          |
| sturs     | STore Single float     | R   | 10_111100000  |              | M[R[Rn] + Imm] = S[Rt]          |
| sturd     | STore Double float     | R   | 11_111100000  |              | M[R[Rn] + Imm] = D[Rt]          |




| Shift | Name | Desc                   |
| ----- | ---- | ---------------------- |
| 00    | LSL  | Logical Shift Left     |
| 01    | LSR  | Logical Shift Right    |
| 10    | ASR  | Arithmetic Shift Right |


| Extend | Name     | Desc                     |
| ------ | -------- | ------------------------ |
| 000    | UXTB     | Unsigned eXTend Byte     |
| 001    | UXTH     | Unsigned eXTend Halfword |
| 010    | UXTW     | Unsigned eXTend Word     |
| 011    | UXTX/LSL | Unsigned eXTend          |
| 100    | SXTB     | Signed eXTend Byte       |
| 101    | SXTH     | Signed eXTend Halfword   |
| 110    | SXTW     | Signed eXTend Word       |
| 111    | SXTX     | Signed eXTend            |


| b.cond[3:0] | Cond Name | Desc                      |
| ----------- | --------- | ------------------------- |
| 0000        | EQ        | Equal                     |
| 0001        | NE        | Not Equal                 |
| 0010        | CS        | Carry Set                 |
| 0011        | CC        | Carry Clear               |
| 0100        | MI        | Minus                     |
| 0101        | PL        | Plus                      |
| 0110        | VS        | Overflow Set              |
| 0111        | VC        | Overflow Clear            |
| 1000        | HI  U>    | Unsigned Higher           |
| 1001        | LS  U<=   | Unsigned Lower or Same    |
| 1010        | GE  S>=   | Signed Greater or Equal   |
| 1011        | LT  S<    | Signed Less Than          |
| 1100        | GT  S>    | Signed Greater Than       |
| 1101        | LE  S<=   | Signed Less Than or Equal |
| 1110        | AL  1     | Always                    |
| 1111        | NV  0     | Never                     |