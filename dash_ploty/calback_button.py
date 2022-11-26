from dash import Dash, dcc, html, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from enumcor import Cor

app = Dash(__name__)

N = 3

tipos = ['Normal', 'Fire', 'Water']


def make_figure0(n):
    return "evento o"


app.layout = html.Div(
    [
        html.Div([html.Div(dbc.Button(f"{cor.name}", id=f"btn-{cor.name}")) for cor in Cor]),
        html.P(id="graph"),
    ]
)


@app.callback(
    Output("graph", "children"), [Input(f"btn-{cor.name}", "n_clicks")for cor in Cor]
)
def update_graph(*_):
    ctx = callback_context
    print('ctx.inputs', ctx.inputs)
    print('ctx.triggered_id', ctx.triggered_id)
    print('ctx.triggered', ctx.triggered[0]['value'])
    print('=======================')

    return ctx.triggered[0]['value']


if __name__ == "__main__":
    app.run_server(debug=True)
