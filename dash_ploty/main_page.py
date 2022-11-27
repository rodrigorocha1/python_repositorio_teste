import dash
from dash.dependencies import Input, Output, MATCH, State
import dash_bootstrap_components as dbc
import dash_html_components as html
from teste_modal import modal

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = modal()

@app.callback(
    Output({'index': MATCH, 'role': 'modal'}, "is_open"),
    [Input({'index': MATCH, 'role': 'open'}, "n_clicks"), Input({'index': MATCH, 'role': 'close'}, "n_clicks")],
    [State({'index': MATCH, 'role': 'modal'}, "is_open")])
def toggle_modal(n1, n2, is_open):
    print(n1, n2, is_open)
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
