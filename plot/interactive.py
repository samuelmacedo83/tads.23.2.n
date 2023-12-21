import plotly.express as px 
from data.download import download_data

def plot_line_i(ticker:str):
    data = download_data('BBAS3.SA')

    fig = px.line(
        data.reset_index(),
        x='Date', y='Close', title='BBAS3',
        labels={'Close': 'Fechamento', 'Date':'Data'}
    )
    return fig