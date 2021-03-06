import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from formulaml_dash import app
from driver_json import team_json as tj
import flask
from dash.dependencies import Input, Output, State
from markupsafe import escape
import plotly.express as px
import pandas as pd
from .GraphScripts import PlotlyGraphScripts as gs

data=tj()
name = 'alfaromeo'
team = data[name]["graph_team"]
lineup = data[name]["team_lineup"]

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

awards = data[name]["awards_won"]
drivers = data[name]["top_drivers"]
history = data[name]["team_history"]

teams_dd = dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Red Bull Racing", href="/team/red_bull/"),
                dbc.DropdownMenuItem("Mercedes AMG", href="/team/mercedes/"),
                dbc.DropdownMenuItem("Scuderia Ferrari", href="/team/ferrari/"),
                dbc.DropdownMenuItem("Renault Sport", href="/team/renault/"),
                dbc.DropdownMenuItem("McLaren F1 Team", href="/team/mclaren/"),
                dbc.DropdownMenuItem("Racing Point F1 Team", href="/team/racingpoint/"),
                dbc.DropdownMenuItem("AlphaTauri", href="/team/alphatauri/"),
                dbc.DropdownMenuItem("Alfa Romeo Racing", href="/team/alfaromeo/"),
                dbc.DropdownMenuItem("Haas F1 Team", href="/team/haas/"),
                dbc.DropdownMenuItem("Williams Racing", href="/team/williams/"),
            ],
            nav=True,
            in_navbar=True,
            label="Teams",
            style={
                "padding-top":"7px",
            }
                )

predictor_dd = dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Predictor", href="/predictor/"),
                dbc.DropdownMenuItem("Predictor Information", href="/predictor_info/"),
            ],
            nav=True,
            in_navbar=True,
            label="Predictor",
            style={
                "padding-top":"7px",
            }
                )
            
layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(
    [
        dbc.Navbar(
            [
                dbc.Nav([dbc.NavLink(dbc.NavLink("Home", href="/", active="exact")), predictor_dd, teams_dd, dbc.DropdownMenu(
                    children=[
                dbc.DropdownMenuItem("Max Verstappen", href="/driver/verstappen/"),
                dbc.DropdownMenuItem("Daniel Ricciardo", href="/driver/ricciardo/"),
                dbc.DropdownMenuItem("Lewis Hamilton", href="/driver/hamilton/"),
                dbc.DropdownMenuItem("Kimi Raikkonen", href="/driver/raikkonen/"),
                dbc.DropdownMenuItem("Sebastian Vettel", href="/driver/vettel/"),
                dbc.DropdownMenuItem("Lando Norris", href="/driver/norris/"),
                dbc.DropdownMenuItem("George Russell", href="/driver/russell/"),
                dbc.DropdownMenuItem("Alex Albon", href="/driver/albon/"),
                dbc.DropdownMenuItem("Sergio Perez", href="/driver/perez/"),
                dbc.DropdownMenuItem("Esteban Ocon", href="/driver/ocon/"),
                dbc.DropdownMenuItem("Lance Stroll", href="/driver/stroll/"),
                dbc.DropdownMenuItem("Nicolas Latifi", href="/driver/latifi/"),
                dbc.DropdownMenuItem("Kevin Magnussen", href="/driver/magnussen/"),
                dbc.DropdownMenuItem("Romain Grosjean", href="/driver/grosjean/"),
                dbc.DropdownMenuItem("Carlos Sainz Jr.", href="/driver/sainz/"),
                dbc.DropdownMenuItem("Charles Leclerc", href="/driver/leclerc/"),
                dbc.DropdownMenuItem("Valtteri Bottas", href="/driver/bottas/"),
                dbc.DropdownMenuItem("Antonio Giovinazzi", href="/driver/giovinazzi/"),
                dbc.DropdownMenuItem("Pierre Gasly", href="/driver/gasly/"),
                dbc.DropdownMenuItem("Daniil Kvyat", href="/driver/kvyat/"),
            ],
            nav=True,
            in_navbar=True,
            label="Drivers",
            style={
                "padding-top":"7px",
            }
                )]),
            ],
            sticky="top",
            style={"font-size":"25px",
                    "height":"65px",
                    "background-color":"#F8EAE8",}
        ),
    ]
),
    #header
    html.Div(id='driver_dropdown'),
    html.Div([
    html.H1(data[name]["name"], style={'text-indent':'100px', 
                                        'line-height':'100%', 
                                        'clear':'both',
                                        'display':'inline-block',
                                        'padding-top':'1%'}),

    html.Img(src=data[name]["flag"], style={'width':'45px',
                                            'height':'45px',
                                            'display':'inline-block',
                                            'clear':'both'}),
    
    html.Img(src=data[name]["team_logo"], style={'width':'25%',
                                            'float':'right',
                                            'margin-top':'3%',
                                            'margin-bottom':'3%',
                                            'margin-right':'3%',
                                            'padding-left':'2%',
                                            'display':'inline-block'}),

    html.H2(data[name]["pairing"], style={'text-indent':'100px',
                                        'vertical-align':'text-top',
                                        'line-height':'100%'}),
    #left
    html.Div([
        html.P("Base: " + data[name]["base"]),
        html.P("Entries: " + data[name]["entries"]),
        html.P("Driver's Titles: " + data[name]["driver_titles"]),
        html.P("Constructor's Titles: " + data[name]["team_titles"]),
    ],id='left', style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'50%',
                            'display':'inline-block'}),
    #right
    html.Div([
        html.P('Wins: ' + data[name]["wins"]),
        html.P('Podiums: ' + data[name]["podiums"]),
         html.P('Poles: ' + data[name]["poles"]),
        html.P('First Start: ' + data[name]["first_start"]),
        html.P('First Win: ' + data[name]["first_win"]),
    ],id='right',style={'text-indent':'100px',
                            'vertical-align':'text-top',
                            'line-height':'50%',
                            'display':'inline-block'}),
    ],id='header', style={'background-color':data[name]["background-color"],
                            'height':'300px', 
                            'padding-top':'10px', 
                            'padding-bottom':'70px', 
                            'font-size':'35px',
                            'color':'black',
                            'margin-bottom': '50px'}),
    html.Div([
        html.Div([
            html.H3('Team Summary'),
            html.P("Alfa Romeo is an iconic name in F1, winning the first two drivers titles in 1950 and 1951 with Juan Manuel Fangio and Nino Farina they wrote their names into F1 legend. They left the sport after these victories, returning in 1979 for a 6 year spell where they never recaptured that glory. This new run for the team after taking over the Sauber team temporarily so far has not gone to plan either. After a strong 2019 campaign scoring 57 points, they endured a rough 2020 only managing 8 points."),
        ],id='points', style={'padding-left':'6%',
                                'padding-top':'2%',
                                'width':'40%',
                                'float':'left',
                                'clear':'both'}),
        dcc.Graph(
            id='example-graph', figure=gs.get_TeamCareerPoints(team), style={'height':'10%', 
                                    'width':'40%', 
                                    'margin-right':'3%', 
                                    'margin-left':'15%', 
                                    'display':'inline-block',
                                    'border-radius': '10px',
                                    'border-top':'solid 10px' + data[name]["background-color"],
                                    'border-right':'solid 10px' + data[name]["background-color"],
                                    'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ]),
    
    html.Div([
        dcc.Graph(
            id='example-graph', figure=gs.get_ConstructorChampionship(team), style={'height':'20%', 'width':'40%', 
                                    'display':'inline-block',
                                    'margin-right': '15%', 
                                    'margin-left':'3%',
                                    'margin-top':'3%',
                                    'border-radius': '10px',
                                    'border-top':'solid 10px' + data[name]["background-color"],
                                    'border-left':'solid 10px' + data[name]["background-color"],
                                    'border-bottom':'solid 10px' + data[name]["background-color"]}),
        html.Div([
            html.H3('Awards Won:'),
            html.Ul(children=[html.Li(i) for i in awards]),
        ],id='awards', style={'float':'right',
                                'clear':'both',
                                'width':'40%',
                                'padding-right':'6%',
                                'padding-top':'2%'}),
    ],style={}),
    #teamHistory
    html.Div([
        html.Div([
            html.H3('2020 Season'),
            html.P("Alfa Romeo endured an incredibly difficult season with very little to smile about, especially compared to their previous campaign. Raikkonen picked up his 4 points through two 9th placed finishes and Giovinazzi finished 9th once and 10th twice. In general both finished in the higher half of the non-scoring drivers however there are no points no matter how well you do if you're not 10th or above."),
        ],id='teamHistory', style={'padding-left':'6%',
                                'padding-top':'2%',
                                'width':'40%',
                                'float':'left',
                                'clear':'both'}),
        dcc.Graph(
            id='example-graph', figure=gs.get_SeasonChampionship(team),  style={'height':'10%', 
                                    'width':'40%', 
                                    'margin-right':'3%', 
                                    'margin-left':'15%', 
                                    'display':'inline-block',
                                    'border-radius': '10px',
                                    'border-top':'solid 10px' + data[name]["background-color"],
                                    'border-right':'solid 10px' + data[name]["background-color"],
                                    'border-bottom':'solid 10px' + data[name]["background-color"]}),
        ]),
    html.Div([
        dcc.Graph(
            id='example-graph', figure=gs.get_TeamLineup(lineup), style={'height':'20%', 
                                    'width':'40%', 
                                    'margin-left':'3%', 
                                    'display':'inline-block',
                                    'border-radius': '10px',
                                    'border-top':'solid 10px' + data[name]["background-color"],
                                    'border-left':'solid 10px' + data[name]["background-color"],
                                    'border-bottom':'solid 10px' + data[name]["background-color"]}),
        
        html.Div([
            html.H3('Top Drivers:'),
            html.Ul(children=[html.Li(i) for i in drivers]),
        ],id='points', style={'float':'right',
                                'padding-right':'6%',
                                'padding-top':'4%',
                                'width':'40%',
                                'clear':'both'}),
    ]),

    html.Div([
        html.Div([
            html.H3('Previous Teams Under this entry'),
            html.Ul(children=[html.Li(i) for i in history]),
        ],id='qualifying', style={'float':'left',
                                'padding-left':'6%',
                                'padding-top':'4%',
                                'width':'40%',
                                'clear':'both'}),
        
        dcc.Graph(
            id='example-graph', figure=gs.get_TeamFinishesScatter(team), style={'height':'10%', 
                                    'width':'40%', 
                                    'margin-right':'3%', 
                                    'margin-left':'15%', 
                                    'display':'inline-block',
                                    'border-radius': '10px',
                                    'border-top':'solid 10px' + data[name]["background-color"],
                                    'border-right':'solid 10px' + data[name]["background-color"],
                                    'border-bottom':'solid 10px' + data[name]["background-color"]}),
    ]),

    ], style={'font-family':'Yu Gothic UI', 'margin':'0', 'padding':'0', 'height':'100%','width':'100%', 'font-size':'25px', 'background-color': '#cccccc'}),

if __name__ == '__main__':
    app.run_server(debug=True)
