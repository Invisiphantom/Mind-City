

https://godbolt.org/
https://armv8-doc.readthedocs.io/en/latest/06.html
https://courses.cs.washington.edu/courses/cse469/19wi/arm64.pdf
https://www.cs.princeton.edu/courses/archive/spr22/cos217/reading/ArmInstructionSetOverview.pdf
https://www.usna.edu/Users/cs/lmcdowel/courses/ic220/S20/resources/ARM-v8-Quick-Reference-Guide.pdf





| Regs      | 功能                      |
| --------- | ------------------------- |
| pc        | Program Counter           |
| x0        | Param and Ret             |
| x1        | Param                     |
| x2        | Param                     |
| x3        | Param                     |
| x4        | Param                     |
| x5        | Param                     |
| x6        | Param                     |
| x7        | Param                     |
| x8        | Caller Saved / Struct Ret |
| x9        | Caller Saved              |
| x10       | Caller Saved              |
| x11       | Caller Saved              |
| x12       | Caller Saved              |
| x13       | Caller Saved              |
| x14       | Caller Saved              |
| x15       | Caller Saved              |
| x16 (IP0) | Veneers Scratch           |
| x17 (IP1) | Veneers Scratch           |
| x18 (PR)  | Platform Register         |
| x19       | Callee Saved              |
| x20       | Callee Saved              |
| x21       | Callee Saved              |
| x22       | Callee Saved              |
| x23       | Callee Saved              |
| x24       | Callee Saved              |
| x25       | Callee Saved              |
| x26       | Callee Saved              |
| x27       | Callee Saved              |
| x28       | Callee Saved              |
| x29 (FP)  | Frame Pointer             |
| x30 (LR)  | Return Address            |
| xzr       | Constant Zero             |



| Level | Desc       |
| ----- | ---------- |
| EL0   | 用户空间   |
| EL1   | 内核空间   |
| EL2   | 虚拟机管理 |
| EL3   | 安全监视器 |


![](https://s2.loli.net/2024/09/29/5xfhw8rDpNGyBLd.png)

| PSTATE | Desc                                       |
| ------ | ------------------------------------------ |
| N      | Negative flag                              |
| Z      | Zero flag                                  |
| C      | Carry flag                                 |
| V      | oVerflow flag                              |
|        |                                            |
| D      | Debug mask bit                             |
| A      | SError mask bit                            |
| I      | IRQ mask bit                               |
| F      | FIQ mask bit                               |
| SS     | Software Step bit                          |
| IL     | Illegal Execution State bit                |
| EL     | Exception level                            |
| nRW    | Execution state        (0:64-bit 1:32-bit) |
| SP     | Stack Pointer selector (0:SP_EL0 1:SP_ELn) |











| ARMv8  | Name                   | Operand        | Description               |
| ------ | ---------------------- | -------------- | ------------------------- |
| add(s) | ADD                    | rd, rn, rm     | rd = rn + rm      (FLAGS) |
| adc(s) | AdD with Carry         | rd, rn, rm     | rd = rn + rm + C  (FLAGS) |
| sub(s) | SUBstract              | rd, rn, rm     | rd = rn - rm      (FLAGS) |
| sbc(s) | SBstract with Carry    | rd, rn, rm     | rd = rn - rm - ~C (FLAGS) |
| neg(s) | NEGate                 | rd,     rm     | rd = - rm         (FLAGS) |
| ngc(s) | NeGate with Carry      | rd,     rm     | rd = - rm - ~C    (FLAGS) |
| cmp    | CoMPare                | rn, rm         | rn - rm           (FLAGS) |
| cmn    | CoMPare Negative       | rn, rm         | rn + rm           (FLAGS) |
| madd   | Multiply ADD           | rd, rn, rm, ra | rd = ra + rn * rm         |
| msub   | Multiply SUBtract      | rd, rn, rm, ra | rd = ra - rn * rm         |
| mneg   | Multiply NEGate        | rd, rn, rm     | rd = - rn * rm            |
| mul    | MULtiply               | rd, rn, rm     | rd = rn * rm              |
| smulh  | Signed MULtiply High   | rd, rn, rm     | rd = (rn * rm)[127:64]    |
| umulh  | Unsigned MULtiply High | rd, rn, rm     | rd = (rn * rm)[127:64]    |
| sdiv   | Signed DIVide          | rd, rn, rm     | rd = rn / rm              |
| udiv   | Unsigned DIVide        | rd, rn, rm     | rd = rn / rm              |
| adr    | ADd Relative           | rd, rel[21]    | rd = PC + rel             |




![](https://s2.loli.net/2024/09/29/MyU7EODZC6lnsLX.png)

| R-Type | 31-21  | 20-16 | 15-10 | 9-5 | 4-0 |
| ------ | ------ | ----- | ----- | --- | --- |
|        | Opcode | Rm    | Imm6  | Rn  | Rd  |

| I-Type | 31-22  | 21-16  15-10 | 9-5 | 4-0 |
| ------ | ------ | ------------ | --- | --- |
|        | Opcode | Immr   Imms  | Rn  | Rd  |

| D-Type | 31-21  | 20-12 | 11-10 | 9-5 | 4-0 |
| ------ | ------ | ----- | ----- | --- | --- |
|        | Opcode | Imm9  | Op    | Rn  | Rt  |

| B-Type | 31-26  | 25-0  |
| ------ | ------ | ----- |
|        | Opcode | Imm26 |

| CB-Type | 31-24  | 23-5  | 4-0 |
| ------- | ------ | ----- | --- |
|         | Opcode | Imm19 | Rt  |

| IM-Type | 31-21  | 20-5  | 4-0 |
| ------- | ------ | ----- | --- |
|         | Opcode | Imm16 | Rd  |



| ARMv8  | Name                               | FMT | Opcode[31:x]    | Shamt[x:10] | Description                                          |
| ------ | ---------------------------------- | --- | --------------- | ----------- | ---------------------------------------------------- |
| add{s} | ADD                                | R   | 1_0S_01011_SF_0 | Imm6        | R[Rd] = R[Rn] + R[Rm].sf                             |
| sub{s} | SUB                                | R   | 1_1S_01011_SF_0 | Imm6        | R[Rd] = R[Rn] - R[Rm].sf                             |
| add{s} | ADD (Extend)                       | R   | 1_0S_01011_00_1 | Op3 Imm3    | R[Rd] = R[Rn] + R[Rm].ext                            |
| sub{s} | SUB (Extend)                       | R   | 1_1S_01011_00_1 | Op3 Imm3    | R[Rd] = R[Rn] - R[Rm].ext                            |
| adc{s} | AdD with Carry                     | R   | 1_0S_11010_00_0 | 000000      | R[Rd] = R[Rn] + R[Rm] + C                            |
| sbc{s} | SuB with Carry                     | R   | 1_1S_11010_00_0 | 000000      | R[Rd] = R[Rn] - R[Rm] - ~C                           |
|        |                                    |     |                 |             |                                                      |
| and{s} | AND                                | R   | 1_SS_01010_SF_0 | Imm6        | R[Rd] = R[Rn] & R[Rm].sf                             |
| bic{s} | Bit Clear                          | R   | 1_SS_01010_SF_1 | Imm6        | R[Rd] = R[Rn] & ~R[Rm].sf                            |
| orr    | OR                                 | R   | 1_01_01010_SF_0 | Imm6        | R[Rd] = R[Rn] \| R[Rm].sf                            |
| eor    | Exclusive OR                       | R   | 1_10_01010_SF_0 | Imm6        | R[Rd] = R[Rn] ^ R[Rm].sf                             |
| orn    | OR NOT                             | R   | 1_01_01010_SF_1 | Imm6        | R[Rd] = R[Rn] \| ~R[Rm].sf                           |
| eon    | Exclusive OR NOT                   | R   | 1_10_01010_SF_1 | Imm6        | R[Rd] = R[Rn] ^ ~R[Rm].sf                            |
|        |                                    |     |                 |             |                                                      |
| lsl    | Logical Shift Left                 | R   | 1_00_11010_11_0 | 001000      | R[Rd] = R[Rn] << R[Rm]                               |
| lsr    | Logical Shift Right                | R   | 1_00_11010_11_0 | 001001      | R[Rd] = R[Rn] >> R[Rm]                               |
| asr    | Arithmetic Shift Right             | R   | 1_00_11010_11_0 | 001010      | R[Rd] = R[Rn] >>> R[Rm]                              |
| ------ |                                    |     |                 |             |                                                      |
| add{s} | ADD                                | I   | 1_0S_100010_H   | Imm12       | R[Rd] = R[Rn] + Imm << (H ? 12 : 0)                  |
| sub{s} | SUB                                | I   | 1_1S_100010_H   | Imm12       | R[Rd] = R[Rn] - Imm << (H ? 12 : 0)                  |
|        |                                    |     |                 |             |                                                      |
| and{s} | AND                                | I   | 1_SS_100100_1   | Imm12       | R[Rd] = R[Rn] & Imm                                  |
| orr    | OR                                 | I   | 1_01_100100_1   | Imm12       | R[Rd] = R[Rn] \| Imm                                 |
| eor    | Exclusive OR                       | I   | 1_10_100100_1   | Imm12       | R[Rd] = R[Rn] ^ Imm                                  |
|        |                                    |     |                 |             |                                                      |
| sbfm   | Signed BitField Move               | I   | 1_00_100110_1   | Immr Imms   | R[Rd] = [(R[Rn][Imms:0] o>> Immr) & oneSide].sext    |
| ubfm   | Unsigned BitField Move             | I   | 1_10_100110_1   | Immr Imms   | R[Rd] = [(R[Rn][Imms:0] o>> Immr) & oneSide]         |
| ------ |                                    |     |                 |             |                                                      |
| movz   | MOVe with Zero                     | IM  | 110100101       |             | R[Rd] = Imm[15:0] << Inst[22:21]*16                  |
| movk   | MOVe with Keep                     | IM  | 111100101       |             | R[Rd][+15:Inst[22:21]*16] = Imm                      |
| ------ |                                    |     |                 |             |                                                      |
|        |                                    |     |                 |             | BAddr ={inst[25:0],00}.sext                          |
|        |                                    |     |                 |             | CBAddr={inst[18:0],00}.sext                          |
|        |                                    |     |                 |             |                                                      |
| br     | Branch to Register                 | R   | 11010110000     |             | PC = R[Rt]                                           |
| b      | Branch                             | B   | 000101          |             | PC += BAddr                                          |
| bl     | Branch with Link                   | B   | 100101          |             | R[30] = PC + 4; PC += BAddr                          |
| b.cond | Branch CONDitional                 | CB  | 01010100        |             | if(FLAGS==cond) PC += CBAddr                         |
| cbnz   | Compare & Branch if Not Zero       | CB  | 10110101        |             | if(R[Rt] != 0)  PC += CBAddr                         |
| cbz    | Compare & Branch if Zero           | CB  | 10110100        |             | if(R[Rt] == 0)  PC += CBAddr                         |
| ---    |                                    |     |                 |             |                                                      |
| sturb  | STore Unscaled Register Byte       | D   | 00_111000000    |             | M[R[Rn] + Imm][7:0] = R[Rt][7:0]                     |
| sturh  | STore Unscaled Register Halfword   | D   | 01_111000000    |             | M[R[Rn] + Imm][15:0] = R[Rt][15:0]                   |
| sturw  | STore Unscaled Register Word       | D   | 10_111000000    |             | M[R[Rn] + Imm][31:0] = R[Rt][31:0]                   |
| stur   | STore Unscaled Register            | D   | 11_111000000    |             | M[R[Rn] + Imm][63:0] = R[Rt][63:0]                   |
| stxr   | Store eXclusive Register           | R   | 11_001000000    |             | M[R[Rn] + Imm][63:0] = R[Rt][63:0]; R[Rm]=(atom)?0:1 |
| ------ |                                    |     |                 |             |                                                      |
| ldurb  | LoaD Unscaled Register Byte        | D   | 00_111000010    |             | R[Rt] = M[R[Rn] + Imm][7:0]                          |
| ldurh  | LoaD Unscaled Register Half        | D   | 01_111000010    |             | R[Rt] = M[R[Rn] + Imm][15:0]                         |
| ldursw | LoaD Unscaled Register Signed Word | D   | 10_111000100    |             | R[Rt] = M[R[Rn] + Imm][31:0].sext                    |
| ldur   | LoaD Unscaled Register             | D   | 11_111000010    |             | R[Rt] = M[R[Rn] + Imm][63:0]                         |
| ldxr   | LoaD eXclusive Register            | R   | 11_001000010    |             | R[Rd] = M[R[Rn] + Imm][63:0] (atom)                  |



| ARMv8 | Name                   | FMT | Opcode[31:21] | Shamt[15:10] | Description                     |
| ----- | ---------------------- | --- | ------------- | ------------ | ------------------------------- |
| sdiv  | Signed DIVide          | R   | 1001101_0110  | 000010       | R[Rd] = R[Rn] / R[Rm]           |
| udiv  | Unsigned DIVide        | R   | 1001101_0110  | 000011       | R[Rd] = R[Rn] / R[Rm]           |
| mul   | MULtiply               | R   | 1001101_1000  | 011111       | R[Rd] = (R[Rn] * R[Rm])[63:0]   |
| smulh | Signed MULtiply High   | R   | 1001101_1010  |              | R[Rd] = (R[Rn] * R[Rm])[127:64] |
| umulh | Unsigned MULtiply High | R   | 1001101_1110  |              | R[Rd] = (R[Rn] * R[Rm])[127:64] |
| ----- |                        |     |               |              |                                 |
| fmuls | Float MULtiply Single  | R   | 00011110001   | 0000_10      | S[Rd] = S[Rn] * S[Rm]           |
| fdivs | Float DIVide Single    | R   | 00011110001   | 0001_10      | S[Rd] = S[Rn] / S[Rm]           |
| fadds | Float ADD Single       | R   | 00011110001   | 0010_10      | S[Rd] = S[Rn] + S[Rm]           |
| fsubs | Float SUBtract Single  | R   | 00011110001   | 0011_10      | S[Rd] = S[Rn] - S[Rm]           |
| fcmps | Float CoMPare Single   | R   | 00011110001   | 0010_00      | FLAGS = S[Rn] vs S[Rm]          |
| ----- |                        |     |               |              |                                 |
| faddd | Float ADD Double       | R   | 00011110011   | 001010       | D[Rd] = D[Rn] + D[Rm]           |
| fsubd | Float SUBtract Double  | R   | 00011110011   | 001110       | D[Rd] = D[Rn] - D[Rm]           |
| fmuld | Float MULtiply Double  | R   | 00011110011   | 000010       | D[Rd] = D[Rn] * D[Rm]           |
| fdivd | Float DIVide Double    | R   | 00011110011   | 000110       | D[Rd] = D[Rn] / D[Rm]           |
| fcmpd | Float CoMPare Double   | R   | 00011110011   | 001000       | FLAGS = D[Rn] vs D[Rm]          |
| ----- |                        |     |               |              |                                 |
| ldurs | LoaD Single float      | R   | 10_111100010  |              | S[Rt] = M[R[Rn] + Imm]          |
| ldurd | LoaD Double float      | R   | 11_111100010  |              | D[Rt] = M[R[Rn] + Imm]          |
| sturs | STore Single float     | R   | 10_111100000  |              | M[R[Rn] + Imm] = S[Rt]          |
| sturd | STore Double float     | R   | 11_111100000  |              | M[R[Rn] + Imm] = D[Rt]          |



| Alias  | Src    | Situation               |
| ------ | ------ | ----------------------- |
| cmn    | adds   |                         |
| cmp    | subs   |                         |
| neg{s} | sub{s} |                         |
| ngc{s} | sbc{s} |                         |
| lsl(I) | ubfm   | Immr=Imms+1 && Imms!=63 |
| lsr(I) | ubfm   | Imms=63                 |
| ubfiz  | ubfm   | Immr < Imms             |
| uxtb   | ubfm   | Immr=0 && Imms=7        |
| uxth   | ubfm   | Immr=0 && Imms=15       |



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