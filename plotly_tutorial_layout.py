from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

agri_exports = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

life_exp = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(life_exp, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

colors = {
    'text': '#1d9aab'
}


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__, assets_folder="static/css")

app.layout = html.Div([
    html.H1(
        children="Hello Dash",
        style={
            "textAlign": "center",
            "color": colors["text"]
        }
    ),
    html.Div(
        children="Dash is a web application framework; see below for data",
        style={
            "textAlign": "center"
        }
    ),
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(agri_exports),
])

if __name__ == '__main__':
    app.run_server(debug=True)