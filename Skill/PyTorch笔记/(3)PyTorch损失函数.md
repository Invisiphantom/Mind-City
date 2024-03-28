

## nn.CrossEntropyLoss
交叉熵损失函数
```python
class CrossEntropyLoss(
    weight: Tensor | None = None,
    size_average: Any | None = None,
    ignore_index: int = -100,
    reduce: Any | None = None,
    reduction: str = 'mean',
    label_smoothing: float = 0
)

loss_fn = nn.CrossEntropyLoss()

losses = []
for batch, (X, y) in enumerate(dataloader):
    pred = model(X)
    loss = loss_fn(pred, y)
    losses.append(loss.item())
```