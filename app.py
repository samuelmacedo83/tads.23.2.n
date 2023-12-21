import streamlit as st
#import yfinance as yf
import pandas as pd
from data.download import download_data
from plot.static import plot_line
from plotnine import *

st.title('Stock Price App')

# Sidebar
st.sidebar.header('User Input')
symbol = st.sidebar.text_input('Enter stock symbol (e.g., AAPL):', 'AAPL')

stock_data = download_data(symbol)

st.subheader(f'Stock Data for {symbol}')
st.write(stock_data)

# fig = ggplot(
#     data = stock_data.reset_index(),
#     mapping = aes(x = 'Date', y  = 'Close')
# ) + \
#     geom_line() + \
#     ggtitle(f'Dados Históricos do {symbol}') + \
#     xlab('Data') + \
#     ylab('Fechamento')
stock_data = pd.DataFrame(stock_data)
fig = plot_line(stock_data)
#st.subheader('Stock Price Chart')
st.pyplot(fig)