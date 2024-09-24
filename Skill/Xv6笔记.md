




| System Call                                | Desc                                                                   |
| ------------------------------------------ | ---------------------------------------------------------------------- |
| `int fork()`                               | 复制新进程, 但共享文件描述符offset, 父进程返回子进程的pid, 子进程返回0 |
| `int exit(int status)`                     | 终止当前进程, 将status传递给wait()等待进程                             |
| `int wait(int *status)`                    | 等待子进程退出, 返回子进程的pid, 用status存储其退出状态                |
| `int kill(int pid)`                        | 终止进程pid                                                            |
| `int getpid()`                             | 返回当前进程的pid                                                      |
| `int sleep(int n)`                         | 休眠n秒CPU时钟                                                         |
| `int exec(char *file, char *argv[])`       | 内存加载可执行文件file, 传递参数argv, 只在出错时返回                   |
| `char *sbrk(int n)`                        | 扩展进程内存n字节, 返回新内存的起始地址                                |
| `int open(char *file, int flags)`          | 打开文件, flags表示读/写, 返回文件描述符                               |
| `int write(int fd, char *buf, int n)`      | 将buf中的n字节写入文件描述符fd, 返回写入的字节数                       |
| `int read(int fd, char *buf, int n)`       | 从文件描述符fd中读取n字节到buf, 返回读取的字节数, EOF返回0             |
| `int close(int fd)`                        | 关闭文件描述符fd                                                       |
| `int dup(int fd)`                          | 复制文件描述符fd, 但共享offset, 返回新的文件描述符                     |
| `int pipe(int p[])`                        | 创建管道, 读:p[0], 写:p[1], 所有写端关闭后, 读端返回EOF                |
| `int chdir(char *dir)`                     | 改变当前工作目录                                                       |
| `int mkdir(char *dir)`                     | 创建新目录                                                             |
| `int mknod(char *file, int mode, int dev)` | 创建设备文件                                                           |
| `int fstat(int fd, struct stat *st)`       | 将打开文件的信息存储到st中                                             |
| `int link(char *file1, char *file2)`       | 给file1创建新的硬链接file2                                             |
| `int unlink(char *file)`                   | 删除文件链接                                                               |


