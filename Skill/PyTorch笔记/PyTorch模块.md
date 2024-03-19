torch.nn.Module
```python
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))


```

(method) def to(
    device: DeviceLikeType | None = ...,
    dtype: dtype | str | None = ...,
    non_blocking: bool = ...
) -> NeuralNetwork

(method) def state_dict(
    *,
    prefix: str = ...,
    keep_vars: bool = ...
) -> Dict[str, Any]




torch.nn.Flatten
class Flatten(
    start_dim: int = 1,
    end_dim: int = -1
)


torch.nn.Sequential
class Sequential(*args: Module)

torch.nn.Linear
class Linear(
    in_features: int,
    out_features: int,
    bias: bool = True,
    device: Any | None = None,
    dtype: Any | None = None
)

torch.nn.ReLU
class ReLU(inplace: bool = False)

