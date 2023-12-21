import plotly.express as px
from data.download import download_data

data=download_data('BBAS3.SA')

px.line(
    data.reset_index(),
    x='Date', y='Close', title='BBAS3',
    labels={'Close': 'Fechamento', 'Date': 'Data'}
)
from plot.interactive import plot_line_i
plot_line_i('BBAS3')