## PyTorch配置

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
```


```python
import torch
print(torch.__version__)
torch.cuda.is_available()
```

## PyTorch工具包

| Package                | Desc                 |
| ---------------------- | -------------------- |
| torch                  | PyTorch核心库        |
| torch.nn               | 构建神经网络         |
| torch.nn.functional    | 实用数学函数         |
| torch.utils            | 各种工具包           |
| torch.utils.data       | 处理数据集的工具包   |
| torch.optim            | 梯度下降优化算法库   |
| torchvision            | 图像数据集的工具包   |
| torchvision.transforms | 用于图像数据的预处理 |


## PyTorch函数

torch.utils.data.DataLoader
class DataLoader(
    dataset: Dataset,
    batch_size: int | None = 1,
    shuffle: bool | None = None,
    sampler: Sampler | Iterable | None = None,
    batch_sampler: Sampler[List] | Iterable[List] | None = None,
    num_workers: int = 0
)

| Para          | Desc         |
| ------------- | ------------ |
| dataset       | 数据集       |
| batch_size    | 批次大小     |
| shuffle       | 是否打乱数据 |
| sampler       | 样本抽样器   |
| batch_sampler | 批次抽样器   |
| num_workers   | 工作线程数   |




torch.no_grad

torch.save
(function) def save(
    obj: object,
    f: FILE_LIKE,
    pickle_module: Any = pickle,
    pickle_protocol: int = DEFAULT_PROTOCOL,
    _use_new_zipfile_serialization: bool = True,
    _disable_byteorder_record: bool = False
) -> None

torch.load
(function) def load(
    f: FILE_LIKE,
    map_location: MAP_LOCATION = None,
    pickle_module: Any = None,
    *,
    weights_only: bool = False,
    mmap: bool | None = None,
    **pickle_load_args: Any
) -> Any