import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
from datetime import datetime

df = pd.read_csv('daily_sales_formatted.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

app = dash.Dash(__name__)

colors = {
    'background': '#E2E8F0',
    'text': '#1E293B',
    'card': '#FFFFFF',
    'pink_morsel': '#E36E8B'
}

app.layout = html.Div(style={'backgroundColor': colors['background'], 'padding': '40px', 'fontFamily': 'Arial, sans-serif', 'minHeight': '100vh'}, children=[
    html.Div(style={'backgroundColor': colors['card'], 'padding': '30px', 'borderRadius': '12px', 'boxShadow': '0 4px 6px rgba(0,0,0,0.1)', 'maxWidth': '1200px', 'margin': '0 auto'}, children=[
        html.H1(
            children='Soul Foods: Pink Morsel Sales',
            style={'textAlign': 'center', 'color': colors['text'], 'marginBottom': '30px'}
        ),
        html.Div([
            html.Label('Filter by Region: ', style={'fontWeight': 'bold', 'marginRight': '15px', 'fontSize': '18px'}),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': ' All Regions', 'value': 'all'},
                    {'label': ' North', 'value': 'north'},
                    {'label': ' South', 'value': 'south'},
                    {'label': ' East', 'value': 'east'},
                    {'label': ' West', 'value': 'west'}
                ],
                value='all',
                inline=True,
                style={'display': 'inline-block', 'fontSize': '16px'},
                inputStyle={'margin-left': '15px', 'margin-right': '5px'}
            )
        ], style={'textAlign': 'center', 'margin': '0 auto 30px auto', 'padding': '15px', 'backgroundColor': '#F8FAFC', 'borderRadius': '8px', 'border': '1px solid #E2E8F0', 'width': 'fit-content'}),
        dcc.Graph(id='sales-line-chart')
    ])
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        color='region' if selected_region == 'all' else None,
        title=f'Sales Data: {selected_region.capitalize()} Region(s)'
    )

    if selected_region != 'all':
        fig.update_traces(line_color=colors['pink_morsel'])

    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Sales ($)')
    fig.update_layout(plot_bgcolor='#FFFFFF', paper_bgcolor='#FFFFFF')

    vline_date = datetime(2021, 1, 15).timestamp() * 1000
    fig.add_vline(
        x=vline_date,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increased to $3.00",
        annotation_position="top left"
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)