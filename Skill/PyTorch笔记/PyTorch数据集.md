
| Dataset      | Name                                                             | Desc             |
| ------------ | ---------------------------------------------------------------- | ---------------- |
| MNIST        | Modified National Institute of Standards and Technology database | 手写数字数据集   |
| QMNIST       | Extended-MNIST                                                   | 扩展MNIST数据集  |
| EMNIST       | Extended-MNIST                                                   | 扩展MNIST数据集  |
| FashionMNIST | Fashion-MNIST                                                    | 时尚服饰数据集   |
| KMNIST       | Kuzushiji-MNIST                                                  | 日本平假名数据集 |





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