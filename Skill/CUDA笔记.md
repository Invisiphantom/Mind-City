


![](https://img.ethancao.cn/20241019212516.png =400x)

线程层次结构
1. 网格(Grid)：所有线程块的集合
2. 线程块(Block)：所有线程的集合
3. 线程(Thread)：最小执行单元

| Cuda Variable     | Desc       |
| ----------------- | ---------- |
| `dim3 gridDim`    | 网格维度   |
| `dim3 blockDim`   | 线程块维度 |
| `uint3 blockIdx`  | 线程块索引 |
| `uint3 threadIdx` | 线程索引   |


| Cuda Notation                      | Desc                 |
| ---------------------------------- | -------------------- |
| `__host__`                         | 主机调用, 主机执行   |
| `__global__`                       | 主机调用, 设备执行   |
| `__device__`                       | 设备调用, 设备执行   |
| `foo<<<dim3 grid, dim3 block>>>()` | 网格维度, 线程块维度 |


| Cuda Function                                                               | C Function | Desc     |
| --------------------------------------------------------------------------- | ---------- | -------- |
| `cudaMalloc(float **devPtr, size_t size)`                                   | `malloc`   | 内存分配 |
| `cudaMemset(void *devPtr, int value, size_t count)`                         | `memset`   | 内存清零 |
| `cudaMemcpy(void *dst, const void *src, size_t count, cudaMemcpyKind kind)` | `memcpy`   | 内存拷贝 |
| `cudaFree(void *devPtr)`                                                    | `free`     | 内存释放 |
| `const char *cudaGetErrorString(cudaError_t error)`                         | `strerror` | 错误信息 |
| `cudaDeviceSynchronize()`                                                   |            | 设备同步 |



