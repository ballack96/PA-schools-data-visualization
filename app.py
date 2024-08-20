import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import requests
import plotly.express as px


# Initialize the Dash app
app = dash.Dash(__name__)

# Import the dataset
file_name = 'pa-school-direcotory.csv'
data = pd.read_csv(file_name)


# Define the layout
app.layout = html.Div([
    html.H1("Schools in PA"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': cat, 'value': cat} for cat in data['category'].unique()],
        placeholder="Select Category"
    ),
    dcc.Dropdown(
        id='county-dropdown',
        placeholder="Select County"
    ),
    dcc.Graph(id='map')
])

# Callback to update county dropdown based on category
@app.callback(
    Output('county-dropdown', 'options'),
    Input('category-dropdown', 'value')
)
def set_county_options(selected_category):
    filtered_data = data[data['category'] == selected_category]
    return [{'label': county, 'value': county} for county in filtered_data['county'].unique()]

# Callback to update map based on selected filters
@app.callback(
    Output('map', 'figure'),
    [Input('category-dropdown', 'value'),
     Input('county-dropdown', 'value')]
)
def update_map(selected_category, selected_county):
    filtered_data = data.copy()
    if selected_category:
        filtered_data = filtered_data[filtered_data['category'] == selected_category]
    if selected_county:
        filtered_data = filtered_data[filtered_data['county'] == selected_county]

    fig = px.scatter_mapbox(filtered_data,
                            lat="latitude", lon="longitude",
                            hover_name="institution_name",
                            hover_data=["city", "county"],
                            zoom=6, height=750)

    fig.update_layout(mapbox_style="open-street-map")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)