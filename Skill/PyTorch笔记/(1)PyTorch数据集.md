[Datasets & DataLoaders](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)



## torch.utils.data.Dataset
自定义数据集, 需要实现`__len__`和`__getitem__`方法
```python
import os
import pandas as pd
from torchvision.io import read_image

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file) # 读取标签
        self.img_dir = img_dir # 获取图像目录
        self.transform = transform # 图像预处理
        self.target_transform = target_transform # 标签预处理

    def __len__(self):
        return len(self.img_labels) # 返回数据集大小

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0]) # 获取图像路径
        image = read_image(img_path) # 读取图像
        label = self.img_labels.iloc[idx, 1] # 获取标签
        if self.transform:
            image = self.transform(image) # 图像预处理
        if self.target_transform:
            label = self.target_transform(label) # 标签预处理
        return image, label
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


## torchvision.transforms.ToTensor
将PIL图像或numpy.ndarray转换为torch.Tensor
并且将图像的像素值缩放到[0., 1.]之间

## torchvision.transforms.Lambda
将自定义lambda函数应用于图像或标签
```python
# 将10维标签转换为one-hot编码
target_transform = Lambda(lambda y: torch.zeros(
    10, dtype=torch.float).scatter_(dim=0, index=torch.tensor(y), value=1))
```