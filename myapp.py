# Standard Imports
import numpy as np, pandas as pd, random, json, time, os

# Plotly Imports
import plotly.graph_objects as go
import plotly.express as px

# Dash Imports
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Additional Imports
# import STUFF

# Load CSS sheet for style information
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Define the Web-App Object and set to variable "server"
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Suppres some output
app.config.suppress_callback_exceptions = True


#################################################
################# Layout ########################
#################################################

app.layout = html.Div([

    html.H1(children='Super Simple Dash App!'),
    html.H2(children='This is an example of a dash app with an interactive dashboard.'),
    
    html.H6("Change below to make a new figure:"),
    
    html.Div([
           "     Number of points, N=: ",
           dcc.Input(id='my-input', value=10, type='number', debounce = True)
    ], style={'width':600}),

    html.Div([
		"     Size of Noise, s=: ",
		dcc.Input(id='my-input2', value=1, type='number', debounce = True)
	]),
    
    
    html.Br(),
    
    
    html.Div([
        html.Div([
            dcc.Graph(id='figure-output')], 
            style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),

        html.Div([dcc.Graph(id='figure-output2')], 
            style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'})
    ]),

])

#####################
# Plot one          #
#####################
@app.callback(
    Output('figure-output2', 'figure'),
    Input('my-input', 'value'))    
def make_plot(N):
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(N), y=3*np.random.rand(N),
                    mode='lines',
                    name='MORE RANDOM DATA'))
                    
    fig.update_layout(title="Model Output")
    
    return fig  
    




#####################
# Plot two          #
#####################
@app.callback(
    Output('figure-output', 'figure'),
    Input('my-input', 'value'),
    Input('my-input2', 'value'))    
def make_plot(N,s=1):
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(N), y=s*np.random.rand(N),
                    mode='lines',
                    name='Random Data'))
                    
    fig.update_layout(title="Model Output")
    
    return fig    




    
# -------------------------- MAIN ---------------------------- #


# This is the code that gets run when we call this file from the terminal
# The port number can be changed to fit your particular needs
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
