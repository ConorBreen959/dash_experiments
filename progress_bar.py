from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

app = Dash()

app.layout = html.Div([
    html.H1(
        children="Updating Status Message with Dash",
        style={
            "textAlign": "center",
            "color": "#7FDBFF"
        }
    ),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag&Drop or ',
            html.A('Select csv files')
        ]),
        multiple=True,
    ),
    dbc.Alert(id="upload-alert"),
],
    style={
        "backgroundColor": "#111111"
    }
)


@app.callback(Output('upload-alert', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def process_data(contents, names):
    if names is not None:
        #change alert text to validating data
        for f in names:
            if not f.endswith('.csv'):
              return "data is not okay"
            return "data is in required format"
         # change alert text to data format is okay, validating data
         # validate_data()
         # change alert text to data is okay / return not okay
         # save_data()
         # return alert text - success


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)