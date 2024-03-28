## PyTorch安装

https://pytorch.org/get-started/locally/
https://developer.nvidia.com/cuda-downloads

```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-4
sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev


export PATH=/usr/local/cuda-12/bin:${PATH}
export LD_LIBRARY_PATH=/usr/local/cuda-12/lib64:${LD_LIBRARY_PATH}

import torch
print(torch.__version__)
torch.cuda.is_available()
```



## PyTorch工具包

https://pytorch.org/docs/stable/torch.html

| Package                  | Desc                 |
| ------------------------ | -------------------- |
| torch                    | PyTorch核心库        |
| torch.nn as nn           | 构建神经网络         |
| torch.nn.functional as F | 实用数学函数         |
| torch.utils              | 各种工具包           |
| torch.utils.data         | 处理数据集的工具包   |
| torch.autograd           | 自动微分工具包       |
| torch.optim              | 梯度下降优化算法库   |
| torchvision              | 图像数据集的工具包   |
| torchvision.transforms   | 用于图像数据的预处理 |

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.autograd as autograd
from torch.utils.data import DataLoader

import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms

import numpy as np
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
```


## PyTorch数据类型



| Data Type              | dtype                       | CPU Tensor                       | GPU Tensor                |
| ---------------------- | --------------------------- | -------------------------------- | ------------------------- |
| Boolean                | torch.bool                  | torch.BoolTensor                 | torch.cuda.BoolTensor     |
| 8-bit integer          | torch.uint8                 | torch.ByteTensor                 | torch.cuda.ByteTensor     |
| 8-bit integer          | torch.int8                  | torch.CharTensor                 | torch.cuda.CharTensor     |
| 16-bit integer         | torch.int16                 | torch.ShortTensor                | torch.cuda.ShortTensor    |
| 32-bit integer         | torch.int32                 | torch.IntTensor                  | torch.cuda.IntTensor      |
| 64-bit integer         | torch.int64                 | torch.LongTensor                 | torch.cuda.LongTensor     |
| 16-bit floating point  | torch.float16               | torch.HalfTensor                 | torch.cuda.HalfTensor     |
| 16-bit floating point+ | torch.bfloat16              | torch.BFloat16Tensor             | torch.cuda.BFloat16Tensor |
| 32-bit floating point  | torch.float32, torch.float  | torch.FloatTensor (torch.Tensor) | torch.cuda.FloatTensor    |
| 64-bit floating point  | torch.float64, torch.double | torch.DoubleTensor               | torch.cuda.DoubleTensor   |


