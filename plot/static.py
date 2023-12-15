from data.download import download_data
from plotnine import (
    ggplot, aes,
    geom_line,
    ggtitle,
    xlab, ylab
)

def plot_line(ticker:str) -> ggplot:
    """ Plot a static plot using plotnine.

    Args:
        ticker (str): The ticker of financial asset.

    Returns:
        ggplot: A ticker plot.
    """

    data = download_data(ticker)

    fig = ggplot(
        data = data.reset_index(),
        mapping = aes(x = 'Date', y  = 'Close')
    ) + \
        geom_line() + \
        ggtitle(f'Dados Históricos do {ticker}') + \
        xlab('Data') + \
        ylab('Fechamento')

    return fig