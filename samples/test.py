import pandas as pd
import plotly.express as px
import streamlit as st

# Teste do pandas
df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40]
})

# Teste do plotly
fig = px.line(df, x='col1', y='col2', title='Test Plotly Line Chart')

# Teste do streamlit
st.write('Teste do Streamlit')
st.dataframe(df)
st.plotly_chart(fig)
