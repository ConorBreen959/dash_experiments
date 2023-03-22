from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, assets_folder="~/Learnings/dash_experiments/data")

controls = dbc.Card([

    dbc.Form(
        [

            html.Label("Options"),

            dcc.RadioItems(
                id="display_figure",
                options=[
                    {
                        "label": "None",
                        "value": "None"
                    },
                    {
                        "label": "Figure 1",
                        "value": "Figure1"
                    },
                    {
                        "label": "Figure 2",
                        "value": "Figure2"
                    },
                    {
                        "label": "Figure 3",
                        "value": "Figure3"
                    }
                ],
                value="None",
                labelStyle={
                    "display": "inline-block",
                    "width": "10em",
                    "line-height": "0.5em"
                }
            )
        ]),
    ],
    body=True,
    style={"font-size": "large"}
)

app.layout = dbc.Container([

        html.H1('Button for predictions'),

        html.Hr(),

        dbc.Row([

            dbc.Col([controls], xs=4),

            dbc.Col([
                dbc.Row([
                    dbc.Col(html.Img(id='predictions')),
                ])

            ]),
        ]),

    ],

    fluid=True,

)

@app.callback(
    Output("predictions", "src"),
    [Input("display_figure", "value")]
)
def make_graph(display_figure):

    if 'Figure1' in display_figure:
        return app.get_asset_url('data/image_1.png')

    elif 'Figure2' in display_figure:
        return app.get_asset_url('data/image_2.png')

    elif 'Figure3' in display_figure:
        return app.get_asset_url('data/image_3.png')

    else:
        return None

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)