import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

# 初始化 Dash 应用
app = dash.Dash(__name__)
app.title = "交互式指数分布绘图"

# 定义应用布局
app.layout = html.Div([
    html.H1("指数分布的交互式绘图", style={'textAlign': 'center'}),
    
    # 滑动条用于调整 λ 参数
    html.Div([
        html.Label("调整 λ 参数:"),
        dcc.Slider(
            id='lambda-slider',
            min=0.1,
            max=5.0,
            step=0.1,
            value=1.0,
            marks={i: f'{i}' for i in range(1, 6)}
        )
    ], style={'width': '80%', 'margin': 'auto'}),

    # 显示当前 λ 的值
    html.Div(id='lambda-output', style={'textAlign': 'center', 'marginTop': 20}),

    # 绘图区域
    dcc.Graph(
        id='exp-distribution-graph',
        style={'height': '600px'}
    )
])

# 定义回调函数，根据滑动条的值更新图表
@app.callback(
    [Output('exp-distribution-graph', 'figure'),
     Output('lambda-output', 'children')],
    [Input('lambda-slider', 'value')]
)
def update_graph(lambda_val):
    # 定义指数分布的范围
    x = np.linspace(0, 10, 500)
    y = lambda_val * np.exp(-lambda_val * x)

    # 创建 Plotly 图形对象
    trace = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name=f'λ = {lambda_val}'
    )

    layout = go.Layout(
        title='指数分布概率密度函数',
        xaxis=dict(title='x'),
        yaxis=dict(title='f(x)'),
        hovermode='closest'
    )

    figure = go.Figure(data=[trace], layout=layout)

    # 返回图形和当前 λ 的显示
    return figure, f"当前 λ 值: {lambda_val}"

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)
