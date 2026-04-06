import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv('daily_sales_formatted.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

fig = px.line(
    df,
    x='date',
    y='sales',
    color='region',
    title='Pink Morsel Sales: Pre and Post Price Increase'
)

fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Sales ($)')

fig.add_vline(
    x='2021-01-15',
    line_dash="dash",
    line_color="red"
)
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods: Pink Morsel Sales Visualizer',
        style={'textAlign': 'center', 'fontFamily': 'Arial, sans-serif'}
    ),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run(debug=True)