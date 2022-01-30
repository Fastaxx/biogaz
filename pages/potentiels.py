import streamlit as st
import pandas as pd

def app():
	df = pd.read_csv('potentiels-methanisation.csv', sep=';', index_col=1)
	st.header('Potentiel de méthanisation (GWh/an)')

	data = df['Potentiel total de méthanisation (GWh/an)']
	st.write(data)
	st.bar_chart(data)
