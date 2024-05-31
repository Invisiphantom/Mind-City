


## optim.SGD
随机梯度下降优化器
```python
class SGD(
    params: ParamsT,
    lr: float = ...,
    momentum: float = ...,
    dampening: float = ...,
    weight_decay: float = ...,
    nesterov: bool = ...
)

optimizer = optim.Adam(params=model.parameters(), lr=lr)

for batch, (X, y) in enumerate(dataloader):
    pred = model(X)
    loss = loss_fn(pred, y)

    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
```
