## Miniconda安装

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash

conda remove --name Py --all
conda create --name Py python=3.11
conda activate Py

conda remove --name PyT --all
conda create --name PyT python=3.11
conda activate PyT

conda install numpy pandas matplotlib jupyter seaborn scikit-learn
pip install nltk torchviz 
sudo apt install graphviz
nltk.download('all')
```

## Cuda-Toolkit安装

https://pytorch.org/get-started/locally/
https://developer.nvidia.com/cuda-downloads
https://developer.nvidia.com/cudnn-downloads
https://developer.download.nvidia.cn/compute/cudnn/redist/cudnn/linux-x86_64/


```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-4
sudo apt-get -y install cudnn-cuda-12
wget https://developer.download.nvidia.cn/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz
tar -xvf cudnn-linux-x86_64-8.9.7.29_cuda12-archive.tar.xz
sudo cp -f -d cudnn-linux-x86_64-8.9.7.29_cuda12-archive/include/* /usr/local/cuda-12.4/include/
sudo cp -f -d cudnn-linux-x86_64-8.9.7.29_cuda12-archive/lib/* /usr/local/cuda-12.4/lib64/


export PATH=/usr/local/cuda-12/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-12/lib64/stubs/:/usr/local/cuda-12/lib64:$LD_LIBRARY_PATH

conda install -y pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

import torch
print(torch.__version__)
torch.cuda.is_available()
```

## Real3D-Portrait项目配置


https://real3dportrait.github.io/
https://github.com/yerfor/Real3DPortrait


```bash
conda create -n real3dportrait python=3.9
conda activate real3dportrait
conda install -y conda-forge::ffmpeg
conda install -y pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.7 -c pytorch -c nvidia
conda install -y -c fvcore -c iopath -c conda-forge fvcore iopath
conda install -y pytorch3d::pytorch3d
pip install cython openmim==0.3.9 lit httpx[socks] gdown
mim install mmcv==2.1.0
sudo apt install -y unzip portaudio19-dev gcc g++ cmake libx11-dev libopenblas-dev liblapack-dev libavdevice-dev libavfilter-dev libavformat-dev libavcodec-dev libswresample-dev libswscale-dev libavutil-dev
pip install -r docs/prepare_env/requirements.txt -v


cd deep_3drecon/BFM
gdown https://drive.google.com/uc?id=1SPM3IHsyNAaVMwqZZGV6QVaV7I2Hly0v
gdown https://drive.google.com/uc?id=1MSldX9UChKEb3AXLVTPzZQcsbGD4VmGF
gdown https://drive.google.com/uc?id=180ciTvm16peWrcpl4DOekT9eUQ-lJfMU
gdown https://drive.google.com/uc?id=1KX9MyGueFB3M-X0Ss152x_johyTXHTfU
gdown https://drive.google.com/uc?id=19-NyZn_I0_mkF-F5GPyFMwQJ_-WecZIL
gdown https://drive.google.com/uc?id=11ouQ7Wr2I-JKStp2Fd1afedmWeuifhof
gdown https://drive.google.com/uc?id=18ICIvQoKX-7feYWP61RbpppzDuYTptCq
gdown https://drive.google.com/uc?id=1VktuY46m0v_n_d4nvOupauJkK4LF6mHE
cd ../..
cd checkpoints
gdown https://drive.google.com/uc?id=1gz8A6xestHp__GbZT5qozb43YaybRJhZ
gdown https://drive.google.com/uc?id=1gSUIw2AkkKnlLJnNfS2FCqtaVw9tw3QF
unzip 240210_real3dportrait_orig.zip
unzip pretrained_ckpts.zip
ls
cd ..

/home/tiger/.cache -> /home/ethan/.cache
python inference/app_real3dportrait.py
```

## NeRF-pytorch项目配置

https://www.matthewtancik.com/nerf
https://github.com/yenchenlin/nerf-pytorch

```bash
git clone https://github.com/yenchenlin/nerf-pytorch.git
cd nerf-pytorch
conda create -n nerf-pytorch python=3.9
conda activate nerf-pytorch
conda install -y pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
pip install imageio imageio-ffmpeg matplotlib configargparse tensorboard tqdm opencv-python
https://drive.google.com/drive/folders/1jIr8dkvefrQmv737fFm2isiT6tqpbTbv
vi configs/lego.txt         expname = lego_test
python run_nerf.py --config configs/lego.txt --render_only
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
| torchtext                | 文本数据集的工具包   |
| torchvision              | 图像数据集的工具包   |
| torchvision.transforms   | 用于图像数据的预处理 |
| torchviz                 | 可视化神经网络       |

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


## PyTorch数据类型

[TORCH.TENSOR](https://pytorch.org/docs/stable/tensors.html)

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