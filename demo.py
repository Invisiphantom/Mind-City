from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Slider, ColumnDataSource
from bokeh.plotting import figure
import numpy as np

# 初始参数
a = 0
b = 1

# 创建数据源
source = ColumnDataSource(data=dict(x=[], y=[]))

# 创建图形
p = figure(title="均匀分布", x_axis_label="x", y_axis_label="概率密度", width=600, height=400)

# 更新函数
def update_plot():
    a_value = a_slider.value
    b_value = b_slider.value
    X = np.linspace(a_value, b_value, 100)
    Y = np.ones_like(X) / (b_value - a_value)
    source.data = dict(x=X, y=Y)
    p.line("x", "y", source=source)

# 创建滑块
a_slider = Slider(start=0, end=3, value=a, step=0.01, title="a")
b_slider = Slider(start=1, end=5, value=b, step=0.01, title="b")

# 关联回调
a_slider.on_change('value', lambda attr, old, new: update_plot())
b_slider.on_change('value', lambda attr, old, new: update_plot())

# 布局
layout = column(a_slider, b_slider, p)

# 将布局添加到当前文档
curdoc().add_root(layout)

# 初始更新图形
update_plot()