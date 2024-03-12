### 导入库
`import matplotlib.pyplot as plt`

### plt.imshow()
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

### 图像窗口
`plt.show()`