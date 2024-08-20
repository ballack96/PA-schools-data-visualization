import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import requests
import plotly.express as px


# Fetch the data
url = "https://data.pa.gov/resource/dtvt-jb9p.json"
response = requests.get(url)
if response.status_code == 200:
    data = pd.DataFrame(response.json())
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    data = pd.DataFrame()  # Create an empty DataFrame if the request fails

# Initialize the Dash app
app = dash.Dash(__name__)


# Define the app layout
app.layout = html.Div([
    html.H1("PA Data Visualization"),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': col, 'value': col} for col in data.columns],
        value=data.columns[0]  # Default value
    ),
    dcc.Graph(id='line-chart')
])

# Define the callback to update the graph based on the selected dropdown value
@app.callback(
    Output('line-chart', 'figure'),
    [Input('dropdown', 'value')]
)
def update_chart(selected_column):
    fig = px.line(data, x=data.index, y=selected_column, title=f'Line Chart of {selected_column}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)