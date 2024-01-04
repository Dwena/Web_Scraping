import streamlit as st 
from function import *

st.set_page_config(
    page_icon='Les Echos'
)

user_input = st.text_input("Sélectionner une thématique")
nb_articles = st.slider("Nombre d'article à collecter ?", 2, 50, 5)

if st.button("Lancer la collect"):
    data = scraping_les_echos(user_input, nb_articles)
    st.write(data)