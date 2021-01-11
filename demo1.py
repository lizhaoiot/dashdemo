import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc                  # 交互式组件
import dash_html_components as html                 # 代码转html

app = dash.Dash(__name__)
app.layout = html.Div(
    children = [
        html.H1('你好，Dash'),
        html.Div('''Dash: Python网络应用框架'''),
        dcc.Graph(
            id='example-graph',
            figure = dict(
                data = [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': '北京'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': '上海'}],
                layout = dict(title = 'Dash数据可视化')
            )
        )
    ]
)

if __name__ == '__main__':
    app.run_server()