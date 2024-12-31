### 导入库
`import matplotlib.pyplot as plt`



### plt.imread()
(function) def imread(
    fname: str | Path | BinaryIO,
    format: str | None = None
) -> ndarray



### plt.imshow()

```py
(function) def imshow(
    X: ArrayLike | Image,
    cmap: str | Colormap | None = None,
    norm: str | Normalize | None = None,
    *,
    aspect: float | Literal['equal', 'auto'] | None = None,
    interpolation: str | None = None,
    alpha: ArrayLike | None = None,
    vmin: float | None = None,
    vmax: float | None = None,
    origin: Literal['upper', 'lower'] | None = None,
    extent: tuple[float, float, float, float] | None = None,
    interpolation_stage: Literal['data', 'rgba'] | None = None,
    filternorm: bool = True,
    filterrad: float = 4,
    resample: bool | None = None,
    url: str | None = None,
    data: Any | None = None,
    **kwargs: Any
) -> AxesImage
```

| Para                | Func         |
| ------------------- | ------------ |
| X                   | 图像数据     |
| cmap                | 颜色映射     |
| norm                | 归一化方式   |
| aspect              | 图像长宽比   |
| interpolation       | 插值方法     |
| alpha               | 图像透明度   |
| vmin                | 颜色最小值   |
| vmax                | 颜色最大值   |
| origin              | 坐标原点位置 |
| extent              | 显示数据范围 |
| interpolation_stage | 插值阶段     |
| filternorm          | 是否过滤     |
| filterrad           | 过滤半径     |
| resample            | 重采样       |
| url                 | 图像链接     |

```python
from matplotlib import colormaps
list(colormaps)
```
| camp    | Func   |
| ------- | ------ |
| viridis | 翠绿色 |
| gray    | 灰度   |



### plt.subplots()
(function) def subplots(
    nrows: int = 1,
    ncols: int = 1,
    *,
    sharex: bool | Literal['none', 'all', 'row', 'col'] = False,
    sharey: bool | Literal['none', 'all', 'row', 'col'] = False,
    squeeze: bool = True,
    width_ratios: Sequence[float] | None = None,
    height_ratios: Sequence[float] | None = None,
    subplot_kw: dict[str, Any] | None = None,
    gridspec_kw: dict[str, Any] | None = None,
    **fig_kw: Any
) -> tuple[Figure, Any]

`fig, axes = plt.subplots(2, 5, figsize=(12, 5))`


```python
# 绘制带滚动条的正态分布函数
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def normal_distribution(x, mu, sigma):
    return (
        1
        / (sigma * np.sqrt(2 * np.pi))
        * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    )

# 初始参数
mu_initial = 0
sigma_initial = 1

x = np.linspace(-10, 10, 1000)
y = normal_distribution(x, mu_initial, sigma_initial)

# 创建画布
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# 绘制初始的正态分布曲线
(line,) = ax.plot(x, y)

# 添加均值滑动条
ax_mu = plt.axes([0.1, 0.1, 0.65, 0.03])
slider_mu = Slider(ax_mu, "Mu", -5, 5, valinit=mu_initial)

# 添加方差滑动条
ax_sigma = plt.axes([0.1, 0.05, 0.65, 0.03])
slider_sigma = Slider(ax_sigma, "Sigma", 0.1, 5, valinit=sigma_initial)


# 更新函数
def update(val):
    mu = slider_mu.val
    sigma = slider_sigma.val
    y = normal_distribution(x, mu, sigma)
    line.set_ydata(y)
    fig.canvas.draw_idle()


# 绑定更新函数
slider_mu.on_changed(update)
slider_sigma.on_changed(update)

plt.show()
```