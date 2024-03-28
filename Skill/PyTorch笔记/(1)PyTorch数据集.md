
## torchvision.datasets
| Dataset      | Name                                                             | Desc             |
| ------------ | ---------------------------------------------------------------- | ---------------- |
| MNIST        | Modified National Institute of Standards and Technology database | 手写数字数据集   |
| FashionMNIST | Fashion-MNIST                                                    | 时尚服饰数据集   |

```python
class FashionMNIST(
    root: str, # 数据集存放路径
    train: bool = True, # 训练集或测试集
    transform: ((...) -> Any) | None = None, # 数据预处理
    target_transform: ((...) -> Any) | None = None, # 标签预处理
    download: bool = False # 是否下载数据集
)

train_data = torchvision.datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=torchvision.transforms.ToTensor()
)
test_data = torchvision.datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=torchvision.transforms.ToTensor()
)

print(train_data.data.shape)
print(train_data.targets.shape)
print(test_data.targets.unique())

print(test_data.data.shape)
print(test_data.targets.shape)
print(train_data.targets.unique())

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for label, ax in enumerate(axes.flat):
    img = train_data.data[train_data.targets == label][0]
    ax.imshow(img)
    ax.set_title(classes[label])
```


## torch.utils.data.DataLoader
```python
class DataLoader(
    dataset: Dataset, # 数据集
    batch_size: int | None = 1, # 批次大小
    shuffle: bool | None = None, # 是否打乱数据
    sampler: Sampler | Iterable | None = None, # 样本抽样器
    batch_sampler: Sampler[List] | Iterable[List] | None = None, # 批次抽样器
    num_workers: int = 0 # 工作线程数
)

batch_size = 64
train_loader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_data, batch_size=batch_size, shuffle=False)

print(len(train_loader), len(test_loader))
print(train_loader.dataset.data.shape, test_loader.dataset.data.shape)
print(train_loader.dataset.targets.shape, test_loader.dataset.targets.shape)
```
