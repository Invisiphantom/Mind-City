
## 训练函数
```python
def train(
    dataloader: DataLoader,
    model: nn.Module,
    loss_fn: nn.Module,
    optimizer: optim.Optimizer,
):
    model.train()
    losses = []
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        pred = model(X)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            losses.append(loss.item())
    return losses
```

## 测试函数
```python
def test(dataloader: DataLoader, model: nn.Module):
model.eval()
correct_num = 0
with torch.no_grad():
    for X, y in dataloader:
        X, y = X.to(device), y.to(device)
        pred = model(X)
        correct_num += (pred.argmax(1) == y).sum().item()
correct_rate = correct_num / len(dataloader.dataset)
return [correct_rate]
```


## 迭代循环
```python
lr = 1e-3
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(params=model.parameters(), lr=lr)

epochs = 5
train_losses = []
test_accuracy = []
for t in range(epochs):
    print(f"Epoch {t+1} Start")
    train_losses += train(train_loader, model, loss_fn, optimizer)
    test_accuracy += test(test_loader, model)

plt.plot(train_losses, label="train_loss")
print(test_accuracy)
```