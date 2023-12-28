readelf - display information about ELF files

- 参考链接
  - [StormQ's Blog](https://csstormq.github.io/)
  - [计算机那些事——ELF文件结构](http://chuquan.me/2018/05/21/elf-introduce/)

------


| Option | Description    |
| ------ | -------------- |
| -W     | 宽输出格式     |
| -a     | 显示全部信息   |
| -h     | file-header    |
| -l     | program-header |
| -S     | section-header |
| -s     | symbol-table   |
| -r     | reloaction     |
| -d     | dynamic        |



```yaml
ELF Header:
  Magic:   7f  45 4c 46 02  01      01       00 00 00 00 00 00 00 00 00 
           DEL E  L  F  x64 lit-end version1
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0

  Type:                              REL (Relocatable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x0
  Start of program headers:          0 (bytes into file)
  Start of section headers:          832 (bytes into file)
  Flags:                             0x0

  Size of this header:               64 (bytes)
  Size of program headers:           0 (bytes)
  Number of program headers:         0
  Size of section headers:           64 (bytes)
  Number of section headers:         13
  Section header string table index: 12
```

```c
#include <elf.h>
typedef struct {
    unsigned char e_ident[EI_NIDENT]; /* Magic number and other info */

    Elf64_Half e_type;                /* Object file type */
    Elf64_Half e_machine;             /* Architecture */
    Elf64_Word e_version;             /* Object file version */
    Elf64_Addr e_entry;               /* Entry point virtual address */
    Elf64_Off e_phoff;      /* Program header table file offset */
    Elf64_Off e_shoff;      /* Section header table file offset */
    Elf64_Word e_flags;     /* Processor-specific flags */

    Elf64_Half e_ehsize;    /* ELF header size in bytes */
    Elf64_Half e_phentsize; /* Program header table entry size */
    Elf64_Half e_phnum;     /* Program header table entry count */
    Elf64_Half e_shentsize; /* Section header table entry size */
    Elf64_Half e_shnum;     /* Section header table entry count */
    Elf64_Half e_shstrndx;  /* Section header string table index */
} Elf64_Ehdr;
```



```bash
Section Headers:
  [Nr] Name               Type     Address          Off    Size    ES Flg Lk Inf Al
  [ 0]                    NULL     0000000000000000 000000 000000  00      0   0  0
  [ 1] .text              PROGBITS 0000000000000000 000040 000018  00  AX  0   0  1
  [ 2] .data              PROGBITS 0000000000000000 000058 00000c  00  WA  0   0  4
  [ 3] .bss               NOBITS   0000000000000000 000064 000014  00  WA  0   0  4
  [ 4] .rodata            PROGBITS 0000000000000000 000064 000004  00   A  0   0  4
  [ 5] .comment           PROGBITS 0000000000000000 000068 00002c  01  MS  0   0  1
  [ 6] .note.GNU-stack    PROGBITS 0000000000000000 000094 000000  00      0   0  1
  [ 7] .note.gnu.property NOTE     0000000000000000 000098 000020  00   A  0   0  8
  [ 8] .eh_frame          PROGBITS 0000000000000000 0000b8 000038  00   A  0   0  8
  [ 9] .rela.eh_frame     RELA     0000000000000000 0002b8 000018  18   I 10   8  8
  [10] .symtab            SYMTAB   0000000000000000 0000f0 000138  18     11   9  8
  [11] .strtab            STRTAB   0000000000000000 000228 000090  00      0   0  1
  [12] .shstrtab          STRTAB   0000000000000000 0002d0 00006f  00      0   0  1
```


```c
typedef struct {
    Elf64_Word sh_name;       /* Section name (string tbl index) */
    Elf64_Word sh_type;       /* Section type */
    Elf64_Addr sh_addr;       /* Section virtual addr at execution */
    Elf64_Off sh_offset;      /* Section file offset */
    Elf64_Xword sh_size;      /* Section size in bytes */

    Elf64_Xword sh_entsize;   /* Entry size if section holds table */
    Elf64_Xword sh_flags;     /* Section flags */
    Elf64_Word sh_link;       /* Link to another section */
    Elf64_Word sh_info;       /* Additional section information */
    Elf64_Xword sh_addralign; /* Section alignment */
} Elf64_Shdr;
```

```c
// Type
#define SHT_NULL 0                    /* Section header table entry unused */
#define SHT_PROGBITS 1                /* Program data */
#define SHT_SYMTAB 2                  /* Symbol table */
#define SHT_STRTAB 3                  /* String table */
#define SHT_RELA 4                    /* Relocation entries with addends */
#define SHT_HASH 5                    /* Symbol hash table */
#define SHT_DYNAMIC 6                 /* Dynamic linking information */
#define SHT_NOTE 7                    /* Notes */
#define SHT_NOBITS 8                  /* Program space with no data (bss) */
#define SHT_REL 9                     /* Relocation entries, no addends */
#define SHT_SHLIB 10                  /* Reserved */
#define SHT_DYNSYM 11                 /* Dynamic linker symbol table */
#define SHT_INIT_ARRAY 14             /* Array of constructors */
#define SHT_FINI_ARRAY 15             /* Array of destructors */
```

```c
// Flg
#define SHF_WRITE (1 << 0)            /* Writable */
#define SHF_ALLOC (1 << 1)            /* Occupies memory during execution */
#define SHF_EXECINSTR (1 << 2)        /* Executable */
#define SHF_MERGE (1 << 4)            /* Might be merged */
#define SHF_STRINGS (1 << 5)          /* Contains nul-terminated strings */
#define SHF_INFO_LINK (1 << 6)        /* `sh_info' contains SHT index */
#define SHF_LINK_ORDER (1 << 7)       /* Preserve order after combining */
#define SHF_OS_NONCONFORMING (1 << 8) /* Non-standard OS specific handling required */
#define SHF_GROUP (1 << 9)            /* Section is member of a group.  */
#define SHF_TLS (1 << 10)             /* Section hold thread-local data.  */
#define SHF_COMPRESSED (1 << 11)      /* Section with compressed data. */
#define SHF_MASKOS 0x0ff00000         /* OS-specific.  */
#define SHF_MASKPROC 0xf0000000       /* Processor-specific */
#define SHF_GNU_RETAIN (1 << 21)      /* Not to be GCed by linker.  */
#define SHF_ORDERED (1 << 30)         /* Special ordering requirement (Solaris).  */
#define SHF_EXCLUDE (1U << 31)        /* Section is excluded unless referenced or allocated (Solaris).*/
```