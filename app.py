# import requests
# import pandas as pd
# import plotly.express as px  # (version 4.7.0)
# import plotly.graph_objects as go
# from dash.dependencies import Input, Output, ALL, State, MATCH, ALLSMALLER
# import dash  # (version 1.12.0) pip install dash
# #import dash_core_components as dcc
# from dash import dcc
# #import dash_html_components as html
# from dash import html
# from dash.dependencies import Input, Output
# import numpy as np




# app = dash.Dash(__name__)
# server = app.server



# # --------------------------------------------------------------------------------------------------------- #





# # --------------------------------------------------------------------------------------------------------- #
# # # App layout



# df = pd.read_csv('csv_files/all_data.csv')
# # df = pd.read_csv('csv_files/backup.csv')


# # Found that all the indicators except for year are objects not ints. This could be the source of the random values along the axis problem
# print(df.info())


# # Trying to make the y axis ascend numerically
# # df = df.sort_values("Human Development Index").reset_index(drop=True)
# # df = df.sort_values("Life Expectancy").reset_index(drop=True)
# # df = df.sort_values("Education Index").reset_index(drop=True)
# # df = df.sort_values("Income Index").reset_index(drop=True)

# # df.reset_index(drop=True, inplace=True)




# # df17 = df7.sort_values("hdi_value").reset_index(drop=True)

# external_stylesheets = [
#     {
#         "href": "https://fonts.googleapis.com/css2?"
#                 "family=Lato:wght@400;700&display=swap",
#         "rel": "stylesheet",
#     },
# ]

# # --------------------------------------------------------------------------------------------------------- #

# df8 = df.copy()
# # df8 = df8['year','hdi_value','life_expectancy']

# df8 = df8[['Life Expectancy','year','Human Development Index','Education Index','Income Index']]
# # print(df8)

# available_indicators = df['Country_name'].unique()



# app.layout = html.Div([
#     html.Div(children=[
#         html.Button('Add Chart', id='add-chart', n_clicks=0),
#     ]),
#     html.Div(id='container', children=[]),

# ])


# @app.callback(
#     Output('container', 'children'),
#     [Input('add-chart', 'n_clicks')],
#     [State('container', 'children')]
# )
# def display_graphs(n_clicks, div_children):
#     new_child = html.Div(
#         style={'width': '45%', 'display': 'inline-block', 'outline': 'thin lightgrey solid', 'padding': 10},
#         children=[
#             dcc.Graph(
#                 id={
#                     'type': 'dynamic-graph',
#                     'index': n_clicks
#                 },
#                 figure={}
#             ),
#             # dcc.Slider(
#             #     df['year'].min(),
#             #     df['year'].max(),
#             #     step=None,
#             #     value=df['year'].min(),
#             #     marks={str(year): str(year) for year in df['year'].unique()},
#             #     id='year-slider'
#             # ),
#             dcc.RadioItems(
#                 id={
#                     'type': 'graph-choice',
#                     'index': n_clicks
#                 },
#                 options=[
#                          {'label': 'Line Chart', 'value': 'line'},
#                          {'label': 'Bar Chart', 'value': 'bar'},
#                          {'label': 'Pie Chart', 'value': 'pie'},
#                          {'label': 'Map', 'value': 'map'},
#                          {'label': 'Bubble Map', 'value': 'bubblemap'}],
                         
#                 value='line',
#             ),
#             dcc.Dropdown(
#                 id={
#                     'type': 'country-dropdown',
#                     'index': n_clicks
#                 },
#                 options=[{'label': s, 'value': s} for s in np.sort(df['Country_name'].unique())],
#                 multi=True,
#                 value=[],
#                 placeholder="Select a Country"
#             ),
#             html.H3("x-axis"),
#             dcc.Dropdown(
#                 id={
#                     'type': 'xaxis-dropdown',
#                     'index': n_clicks
#                 },
#                 options=[{'label': c, 'value': c} for c in ['Human Development Index', 'Life Expectancy', 'Country_name', 'year', 'Income Index']],
#                 # options=[{'label': c, 'value': c} for c in ['year']],
#                 value=[],
#                 clearable=False,
#                 placeholder="Select a value for the x-axis"
#                 # disabled=True
#             ),
#             html.H3("y-axis"),
#             dcc.Dropdown(
#                 id={
#                     'type': 'yaxis-dropdown',
#                     'index': n_clicks
#                 },
#                 # options=[{'label': n, 'value': n} for n in ['hdi_value', 'life_expectancy', 'Country_name', 'year']],
#                 options=[{'label': n, 'value': n} for n in ['Life Expectancy','Human Development Index','Education Index','Income Index']],
#                 value=[],
#                 clearable=False,
#                 placeholder="Select a value for the y-axis"
#             )
#         ]
#     )
#     div_children.append(new_child)
#     return div_children




# @app.callback(
#     Output({'type': 'dynamic-graph', 'index': MATCH}, 'figure'),
#     # Multiple inputs so it needs to be inside a list
#     [Input(component_id={'type': 'country-dropdown', 'index': MATCH}, component_property='value'),
#      Input(component_id={'type': 'xaxis-dropdown', 'index': MATCH}, component_property='value'),
#      Input(component_id={'type': 'yaxis-dropdown', 'index': MATCH}, component_property='value'),
#     #  Input('year-slider', 'value'),
#      Input({'type': 'graph-choice', 'index': MATCH}, 'value')]
# )


# # country-chosen = Countries selected from dropdown
# # ctg_value = Country_name
# # indicator_chosen_yaxis = year
# def update_graph(country_chosen, ctg_value, indicator_chosen_yaxis, chart_choice):
#     # Country from dropdown
#     print("country-chosen = ", country_chosen)
#     print("ctg_value = ", ctg_value)
#     print("indicator_chosen_yaxis = ", indicator_chosen_yaxis)
#     print("chart_choice = ", chart_choice)

#     dff = df[df.Country_name.isin(country_chosen)]
    
#     if chart_choice == 'bar':
#         # dff = dff.groupby([ctg_value], as_index=False)[['hdi_value', 'life_expectancy', 'Country_name', 'year']].sum()
#         fig = px.bar(dff, x='Country_name', y=indicator_chosen_yaxis, color='Country_name', hover_name="year", barmode='group', title="Bar Chart", 
#         labels={
#                      "Country_name": "Country name"
#                  },)
#         return fig
#     elif chart_choice == 'line':
#         # filtered_df = df[df.year == selected_year]
#         # fig = px.line(filtered_df, x='year', y=indicator_chosen_yaxis, color='Country_name', hover_name="year", title="Line Graph", 
#         fig = px.line(dff, x='year', y=indicator_chosen_yaxis, color='Country_name', hover_name="year", title="Line Graph", 
#         # fig = px.line(dff, x=ctg_value, y=indicator_chosen_yaxis, color='Country_name', hover_name="year", title="Line Graph", 
#         labels={
#                     "year": "Year"
#                 },)
#         fig.update_traces(mode='lines+markers')
#         return fig
#     elif chart_choice == 'pie':
#         dff = df[df['Country_name'].isin(country_chosen)]
#         # fig = px.pie(dff, names=ctg_value, values=indicator_chosen_yaxis, hover_name="Country_name")
#         fig = px.pie(dff, names="Country_name", values=indicator_chosen_yaxis, title="Pie Chart")
#         return fig
#     elif chart_choice == 'map':
#         # # dff = df[df['Country_name'].isin(country_chosen)]
#         fig = px.choropleth(dff, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", title="Map", 
#                     color_continuous_scale=px.colors.sequential.Plasma)
#         return fig
#     elif chart_choice == 'bubblemap':
#         fig = px.scatter_geo(dff, locations="Country_code", title="Bubble Map", hover_name="Country_name")
#         return fig



# if __name__ == '__main__':
#     app.run_server(debug=True)



import dash  # use Dash version 1.16.0 or higher for this app to work
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go



df = pd.read_csv('csv_files/all_data.csv')
# df = pd.read_csv('csv_files/backup.csv')

df8 = df.copy()
df8 = df8[['Life Expectancy','Human Development Index','Education Index','Income Index']]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(
        id='yaxis-dropdown',
        value=[],
        # multi=True,
        options=[{'label': n, 'value': n} for n in df8],
        clearable=False,
        placeholder="Select a value for the y-axis"
    ),
    dcc.Dropdown(id='country_dropdown',
                value=[],
                # value=['United States', 'Russian Federation'], 
                multi=True,
                clearable=True,
                options=[{'label': x, 'value': x} for x in df.Country_name.unique()], 
                placeholder="Select a Country"
    ),

    html.Div([
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
            config={
                'staticPlot': False,     # True, False
                'scrollZoom': False,      # True, False
                'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                'showTips': True,       # True, False
                'displayModeBar': 'hover',  # True, False, 'hover'
                'watermark': False,
                'modeBarButtonsToRemove': ['pan2d','select2d', 'lasso2d', 'autoScale2d', 'resetScale2d', 'zoom2d'],
                },
            className='six columns'
            ),
        dcc.Graph(id='pie-graph', figure={}, className='six columns',
            config={
                'modeBarButtonsToRemove': ['pan2d','select2d', 'lasso2d', 'autoScale2d', 'resetScale2d', 'zoom2d'],
            }),
        dcc.Graph(id='map-graph', figure={}, className='six columns',
            config={
                'modeBarButtonsToRemove': ['pan2d','select2d', 'lasso2d', 'autoScale2d', 'resetScale2d', 'zoom2d'],
            })
    ])
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='country_dropdown', component_property='value'),
    Input(component_id='yaxis-dropdown', component_property='value')
)
def update_graph(country_chosen, indicator_chosen_yaxis):
    dff = df[df.Country_name.isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y=indicator_chosen_yaxis, color='Country_name',
                  custom_data=['Country_name', 'Country_code', 'Life Expectancy', 'year'],
                  labels={
                    "year": "Year"
                })
    fig.update_traces(mode='lines+markers')
    return fig



# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='country_dropdown', component_property='value'),
    Input(component_id='yaxis-dropdown', component_property='value')
)
def update_pie_graph(hov_data, clk_data, slct_data, country_chosen, indicator_chosen_yaxis):
    if hov_data is None:
        dff2 = df[df.Country_name.isin(country_chosen)]
        dff2 = dff2[dff2.year == 2000]
        print(dff2)
        # fig2 = px.pie(data_frame=dff2, values='Country_name', names=indicator_chosen_yaxis,
        #               title=indicator_chosen_yaxis, color='Country_name')
        fig2 = px.pie(dff2, values=indicator_chosen_yaxis, names=country_chosen,
                      title=indicator_chosen_yaxis, color='Country_name')
        fig2.update_traces(textposition='inside', textinfo='percent+label+value')
        return fig2
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')

        dff2 = df[df.Country_name.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig2 = px.pie(data_frame=dff2, values=indicator_chosen_yaxis, names='Country_name', title=f'{indicator_chosen_yaxis} {hov_year}', color='Country_name')
        fig2.update_traces(textposition='inside', textinfo='percent+label+value')
        return fig2
        


@app.callback(
    Output(component_id='map-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='country_dropdown', component_property='value'),
    Input(component_id='yaxis-dropdown', component_property='value')
)
def update_map_graph(hov_data, clk_data, slct_data, country_chosen, indicator_chosen_yaxis):
    if hov_data is None:
        dff2 = df[df.Country_name.isin(country_chosen)]
        dff2 = dff2[dff2.year == 2000]
        print(dff2)
        fig3 = px.choropleth(dff2, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", title="Map", 
                    color_continuous_scale=px.colors.sequential.Plasma)   
        return fig3
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')

        dff2 = df[df.Country_name.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig3 = px.choropleth(dff2, color="Country_name", scope="world", locations="Country_code", hover_name="Country_name", title="Map", 
                    color_continuous_scale=px.colors.sequential.Plasma)        
        return fig3



if __name__ == '__main__':
    app.run_server(debug=True)

