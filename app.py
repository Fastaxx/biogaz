import streamlit as st
import pandas as pd
from multipage import Multipage
from pages import informations, potentiels

#Création de l'instance app
app = Multipage()

# Titre Page général
st.title('Projet Biogaz')

# Ajouter toutes les pages
app.add_page('Potentiels méthanisation', potentiels.app)
app.add_page('Informations', informations.app)

# Lancement App
app.run()