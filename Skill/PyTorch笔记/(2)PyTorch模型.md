
## nn.Module
```python
class Model(nn.Module):
    def __init__(self, pic_height, pic_width, num_classes):
        super(Model, self).__init__()
        self.seq = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Flatten(),
            nn.Linear(64 * (pic_height // 4) * (pic_width // 4), 128),
            nn.ReLU(),
            nn.Linear(128, num_classes),
        )

    def forward(self, x):
        return self.seq(x)

model = Model(28, 28, 10).to(device)
total_params = 0
for params in model.parameters():
    total_params += params.numel()
print(model)
print(f"Total number of parameters: {total_params}")

for name, param in model.named_parameters():
    print(f"Layer: {name}\n Size: {param.size()}\n Values: {param[:2]}\n")
```


## torch.save, torch.load
```python
torch.save
(function) def save(
    obj: object, # 保存的对象
    f: FILE_LIKE, # 文件路径
    pickle_module: Any = pickle,
    pickle_protocol: int = DEFAULT_PROTOCOL,
    _use_new_zipfile_serialization: bool = True,
    _disable_byteorder_record: bool = False
) -> None

torch.load
(function) def load(
    f: FILE_LIKE, # 文件路径
    map_location: MAP_LOCATION = None,
    pickle_module: Any = None,
    *,
    weights_only: bool = False,
    mmap: bool | None = None,
    **pickle_load_args: Any
) -> Any

torch.save(model.state_dict(), "model.pth")
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model.pth"))
```


## nn.Sequential
组合多个模块
```python
class Sequential(*args: Module)

self.seq = nn.Sequential(
    nn.Linear(in_features=28 * 28, out_features=512),
    nn.ReLU(),
    nn.Linear(in_features=512, out_features=512),
    nn.ReLU(),
    nn.Linear(in_features=512, out_features=10),
)
```

## nn.Embedding
```python
class Embedding(
    num_embeddings: int, # 输入词典大小
    embedding_dim: int,  # 输出词向量维度
    padding_idx: int | None = None,
    max_norm: float | None = None,
    norm_type: float = 2,
    scale_grad_by_freq: bool = False,
    sparse: bool = False,
    _weight: Tensor | None = None,
    _freeze: bool = False,
    device: Any | None = None,
    dtype: Any | None = None
)

nn.Embedding(vocab_size, embedding_dim)
```


## nn.Flatten
将输入张量展平, 用于全连接层之前
```python
class Flatten(
    start_dim: int = 1, # 起始维度
    end_dim: int = -1 # 结束维度
)
```

## nn.ReLU
ReLU激活函数
```python
class ReLU(inplace: bool = False)
```

## nn.Linear
全连接层
```python
class Linear(
    in_features: int, # 输入维度
    out_features: int, # 输出维度
    bias: bool = True,
    device: Any | None = None,
    dtype: Any | None = None
)

nn.Linear(in_features=28 * 28, out_features=512)
```

## nn.Conv2d
卷积层
```python
class Conv2d(
    in_channels: int,  # 输入通道数(灰度图像为1, RGB图像为3)
    out_channels: int, # 输出通道数
    kernel_size: _size_2_t, # 卷积核大小
    stride: _size_2_t = 1,  # 卷积核步长
    padding: _size_2_t | str = 0, # 填充大小
    dilation: _size_2_t = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = 'zeros',
    device: Any | None = None,
    dtype: Any | None = None
)

nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)
```

## nn.MaxPool2d
最大汇聚层
降低卷积层对位置的敏感性
同时降低对空间降采样表示的敏感性
```python
class MaxPool2d(
    kernel_size: _size_any_t,          # 池化核大小
    stride: _size_any_t | None = None, # 池化步长
    padding: _size_any_t = 0,
    dilation: _size_any_t = 1,
    return_indices: bool = False,
    ceil_mode: bool = False
)

nn.MaxPool2d(kernel_size=2, stride=2)
```
