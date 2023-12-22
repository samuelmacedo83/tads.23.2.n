import streamlit as st
from plot.interactive import plot_line_i

st.title('Stock Price App')

# Sidebar
symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL')

# Plot
fig = plot_line_i(symbol)
st.plotly_chart(fig)