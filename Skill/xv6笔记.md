

https://github.com/mit-pdos/xv6-riscv
https://pdos.csail.mit.edu/6.S081/2024/xv6/book-riscv-rev4.pdf

```bash
git clone https://github.com/mit-pdos/xv6-riscv.git
sudo apt install binutils-riscv64-linux-gnu gcc-riscv64-linux-gnu qemu-system-riscv64 gdb-multiarch
make qemu

echo "add-auto-load-safe-path /home/ethan/xv6-riscv/.gdbinit" > ~/.gdbinit
make qemu-gdb
gdb-multiarch kernel/kernel



```
