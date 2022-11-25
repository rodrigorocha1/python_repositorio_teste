from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id="input_text", placeholder="Type something...", type="text"),
    dbc.Button(
        "Click me", id="example_button", className="me-2", n_clicks=0
    ),
    dcc.Tabs(
        id="tabs-with-classes-2",
        value='tab-2',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Tab one',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab two',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab three, multiline',
                value='tab-3', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Tab four',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
        ]),
    html.Div(id='tabs-content-classes-2')
])


# @app.callback(Output('tabs-content-classes-2', 'children'),
#               [Input('tabs-with-classes-2', 'value'),
#                [Input('input_text', 'value')]],
#
#               )
# def render_content(tab, value):
#     print(tab)
#     if tab == 'tab-1':
#         return html.Div([
#             html.H3(f'Tab content 1 {value, type(value)}'),
#         ])
#     elif tab == 'tab-2':
#         return html.Div([
#             html.H3(f'Tab content 2 {value, type(value)}'),
#         ])
#     elif tab == 'tab-3':
#         return html.Div([
#             html.H3(f'Tab content 3{value, type(value)}'),
#         ])
#     elif tab == 'tab-4':
#         return html.Div([
#             html.H3(f'Tab content 4 {value, type(value)}'),
#         ])


@app.callback(Output('tabs-content-classes-2', 'children'),
              [Input('tabs-with-classes-2', 'value'),
               [Input('example_button', 'n_clicks')]],
              State('input_text', 'value')

              )
def render_content(tab, n_clicks, input_text):
    print(tab)
    if tab == 'tab-1':
        return html.Div([
            html.H3(f'Tab content 1 {input_text, type(input_text)}'),
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3(f'Tab content 2 {input_text, type(input_text)}'),
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3(f'Tab content 3{input_text, type(input_text)}'),
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3(f'Tab content 4 {input_text, type(input_text)}'),
        ])


if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
