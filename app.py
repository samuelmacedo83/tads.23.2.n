import streamlit as st
from plot. interactive import plot_line_i

sit.title('Stock Price App')

st. sidebar. header('User Input')
symbol = st.sidebar. text_input ('Escolha um ativo:', 'APPL')

plot

fig= plot_line_i(symbol)
st.plotly_char(fig)