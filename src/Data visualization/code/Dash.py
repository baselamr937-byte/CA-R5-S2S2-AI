import html

import Dash
from dash import Dash,html,dcc
from dash.dependencies import Input,Output
app=Dash(__name__)
app.layout=html.Div([
    html.Button('Submit',id='number')
    dcc.Input(placeholder="Enter a valid number")])

app.run(debug=True)