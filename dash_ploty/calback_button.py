from dash import Dash, dcc, html, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

app = Dash(__name__)

N = 3

tipos = ['Normal', 'Fire', 'Water']


def make_figure0(n):
    return "evento o"


app.layout = html.Div(
    [
        html.Div([html.Div(dbc.Button(f"{tipo}", id=f"btn-{tipo}")) for tipo in tipos]),
        html.P(id="graph"),
    ]
)


@app.callback(
    Output("graph", "children"), [Input(f"btn-{tipo}", "n_clicks") for tipo in tipos]
)
def update_graph(*_):
    ctx = callback_context
    print('ctx.inputs', ctx.inputs)
    print('ctx.triggered_id', ctx.triggered_id)
    print('ctx.triggered', ctx.triggered[0]['value'])
    print('=======================')
    if not ctx.triggered:
        raise PreventUpdate
    else:
        n = ctx.triggered[0]["prop_id"].split(".")[0].split("-")[1]
    if n == "0":
        return make_figure0(n)


if __name__ == "__main__":
    app.run_server(debug=True)
