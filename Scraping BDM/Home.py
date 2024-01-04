import streamlit as st
from function import *
import json

# Input User
user_input = st.text_input("Choisissez une thématique ")

# Slider
n_pages = st.slider("Sélectionez le nombre de page : ",1,50)


# Buton
if st.button('Lancer la recherche'):
    data = {}
    user_input = user_input.replace(' ', '+')
    
    for page in range(1, n_pages):
        search_url= f'https://www.blogdumoderateur.com/page/{page}/?s=' + user_input
        data = scraping_bdm(search_url, data)

    with open('utiles/'+user_input.replace('+', '_')+'.json','w') as f:
        json.dump(data, f)

    st.write(data)