import dash
from dash import dcc, html
import dash_table
import pandas as pd

# Load CSV file into a DataFrame
csv_file_path = r'C:\Users\Akshat\Desktop\google-maps-reviews-scraper\output\wyzmindz-solutions-pvt-ltd-bengaluru-karnataka\csv\detailed-reviews-of-wyzmindz-solutions-pvt-ltd-bengaluru-karnataka.csv'
df = pd.read_csv(csv_file_path)

# Create Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_data_conditional=[
            {
                'if': {'column_id': 'review_text'},
                'height': 'auto'  # Set the height of the review_text cell to auto
            }
        ],
        style_cell={
            'whiteSpace': 'normal',
            'height': 'auto',
            'textAlign': 'left'
        },
        style_cell_conditional=[
            {
                'if': {'column_id': 'review_text'},
                'width': '500px',  # Set the width of the review_text cell to 500px
            }
        ],
        css=[{
            'selector': '.dash-cell div.dash-cell-value',
            'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
        }],
        style_table={
            'overflowX': 'auto'
        },
        sort_action='native',
        sort_mode='single',
        sort_by=[]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
