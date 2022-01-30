import streamlit as st
import pandas as pd
import altair as alt

st.title('Projet Biogaz')
df = pd.read_csv('potentiels-methanisation.csv', sep=';', index_col=1)
st.header('Potentiel de méthanisation (GWh/an)')

st.write(df)
st.bar_chart(df['Potentiel total de méthanisation (GWh/an)'])