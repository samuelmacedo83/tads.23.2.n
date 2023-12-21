import plotly.express as px
from data.download import download_data
def plot_line_i(ticker:str):
    """_summary_

    Args:
        ticker (str): _description_

    Returns:
        _plotly: A ticker plot
    """
    data=download_data(ticker)

    fig = px.line(
        data.reset_index(),
        x='Date', y='Close', title= ticker,
        labels={'Close': 'Fechamento', 'Date': 'Data'}
    )
    return fig 