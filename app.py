import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Output, Input
import plotly.express as px

data = {'Stock': ['F',  'NFLX',  'AMZN'], 'Number': [10, 15, 7]}
df = pd.DataFrame(data, columns=['Stock', 'Number'])
stock_options = df['Stock']

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Example Bar Chart'),
    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in stock_options],
            value='F',

         ),
        html.Div(dcc.Graph(id='graph')),
    ]),
])


@app.callback(
   Output(component_id='graph', component_property='figure'),
   Input(component_id='dropdown', component_property='value')
)
def update_graph(stock):
    msk = df.Stock.isin([stock])
    figure = px.bar(df[msk], x='Stock', y='Number', title=f"{stock} open price")

    return figure


if __name__ == '__main__':
    app.run_server(debug=True, port=5000)