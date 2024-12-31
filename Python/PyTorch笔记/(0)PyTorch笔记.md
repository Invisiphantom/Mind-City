

## PyTorch工具包

https://pytorch.org/docs/stable/torch.html

| Package                | Desc                 |
| ---------------------- | -------------------- |
| torch                  | PyTorch核心库        |
| torch.nn               | 构建神经网络         |
| torch.nn.functional    | 实用数学函数         |
| torch.utils            | 各种工具包           |
| torch.utils.data       | 处理数据集的工具包   |
| torch.autograd         | 自动微分工具包       |
| torch.optim            | 梯度下降优化算法库   |
| torchtext              | 文本数据集的工具包   |
| torchvision            | 图像数据集的工具包   |
| torchvision.transforms | 用于图像数据的预处理 |
| torchviz               | 可视化神经网络       |

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.autograd as autograd
from torch.utils.data import Dataset, DataLoader

import torchvision
import torchvision.datasets as datasets
from torchvision.transforms import ToTensor, Lambda

import numpy as np
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
```


| Func               | Desc                     |
| ------------------ | ------------------------ |
| torch.tensor()     | 拷贝创建张量(不共享内存) |
| torch.as_tensor()  | 创建张量(共享内存)       |
| torch.from_numpy() | 从numpy数组创建张量      |
| torch.item()       | 返回python类型的变量     |
| torch.zeros_like() | 创建与输入相同的全0张量  |
| torch.ones_like()  | 创建与输入相同的全1张量  |
| torch.rand_like()  | 创建与输入相同的随机张量 |
| torch.arange       | 创建等差数列张量         |
| torch.zeros        | 创建全0张量              |
| torch.ones         | 创建全1张量              |
| torch.rand         | 创建随机张量             |
| torch.randn        | 创建正态分布张量         |
| torch.cat          | 拼接张量                 |
| torch.mul (*)      | 逐元素相乘               |
| torch.matmul (@)   | 矩阵相乘                 |
| torch.no_grad()    | 关闭梯度计算             |

张量 = 头信息区 + 数据存储区
| Attri                | Desc             |
| -------------------- | ---------------- |
| tensor.shape         | 张量的形状       |
| tensor.dtype         | 张量的数据类型   |
| tensor.device        | 张量的存储设备   |
| tensor.requires_grad | 张量是否具有梯度 |
| tensor.grad_fn       | 张量的梯度函数   |
| tensor.grad          | 张量的梯度       |

| Func                    | Desc                         |
| ----------------------- | ---------------------------- |
| tensor.numpy()          | 张量转换为numpy数组          |
| tensor.size()           | 获取张量的形状               |
| tensor.stride()         | 获取张量的步长               |
| tensor.view()           | 改变张量视图(共享内存)       |
| tensor.reshape()        | 改变张量形状(连续时共享内存) |
| tensor.is_contiguous()  | 判断张量是否连续             |
| tensor.contiguous()     | 获取张量的连续副本           |
| tensor.storage()        | 张量的存储区                 |
| tensor.data_ptr()       | 张量的存储区地址             |
| tensor.storage_offset() | 张量的存储区偏移量           |


| Func             | Desc           |
| ---------------- | -------------- |
| tensor.permute() | 张量维度交换   |
| tensor.argmax()  | 张量最大值索引 |
| tensor.argmin()  | 张量最小值索引 |
| tensor.sort()    | 张量排序       |
| tensor.sum()     | 张量求和       |


| Method             | Inplace                 | Desc     |
| ------------------ | ----------------------- | -------- |
| tensor.abs()       | tensor.abs_()           | 绝对值   |
| tensor.floor()     | tensor.floor_()         | 向下取整 |
| tensor.scatter()   | tensor.scatter_()       | 索引赋值 |
| tensor.squeeze()   | tensor.squeeze_()       | 去除维度 |
| tensor.unsqueeze() | tensor.unsqueeze_()     | 增加维度 |
| tensor.detach()    | tensor.requires_grad_() | 分离梯度 |
| tensor.add()       | tensor.add_()           | 加法     |
| tensor.sub()       | tensor.sub_()           | 减法     |
| tensor.mul()       | tensor.mul_()           | 乘法     |
| tensor.div()       | tensor.div_()           | 除法     |
| tensor.pow()       | tensor.pow_()           | 幂运算   |
| tensor.sqrt()      | tensor.sqrt_()          | 开方     |



1. view() 只能对满足连续性要求的tensor使用
2. 当 tensor 满足连续性要求时, reshape() = view(), 和原来 tensor 共用内存
3. 当 tensor 不满足连续性要求时, reshape() = contiguous() + view(), 与原来 tensor 不共用存储区
4. resize_() 可以随意的获取任意维度的 tensor, 多退少补, 不推荐使用


```python
tensor = torch.randn(2, 3)
reshaped_tensor = tensor.view(3, 2)

print(tensor)
print(reshaped_tensor)

print(tensor.data_ptr())
print(reshaped_tensor.data_ptr())
```