import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app=dash.Dash()
file = pd.read_csv("covidbydate.csv")
file =file.replace(0,np.nan)

app.layout = html.Div(children = [
    html.H1(children = 'Analysis of covid cases per day'), html.Hr(),
    dcc.Graph(
        id = 'covid',
        go.Figure = {
            'data' : [
                { 'x' : file['Date'], 'y':file['total confirmed cases'] , 'type': 'bar'}
                ]})
    ])

if __name__ == '__main__':
    app.run_server(debug=True)

