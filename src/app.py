from dash import Dash, html, dcc

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal')
])

if __name__ == '__main__':
    app.run(debug=False)