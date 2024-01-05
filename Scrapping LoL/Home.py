import sqlite3
import streamlit as st
from functions import *

@st.cache_data
def load_data():
    return scraping_lol()

video_url = "https://www.leagueoflegends.com/static/hero-3e934348790824f4b800524f96a93020.mp4"
image_url = "https://www.leagueoflegends.com/static/logo-1200-04b3cefafba917c9c571f9244fd28a1e.png"


st.image(image_url, width=400, use_column_width=True, output_format='PNG', clamp=False, channels='RGB')
st.video(video_url)


champions_names = load_data()
# Afficher les champions dans une liste déroulante mutlitple
champions = st.multiselect('Select champions', champions_names)

# Utiliser un bouton pour lancer la recherche des informations de la liste déroulante
if st.button('Search'):
    for champion in champions:
        champion_info = scraping_champions_info(champion)
        col1, col2 = st.columns([1, 3])  
        with col1:
            st.image(champion_info['image_url'], width=170)
        with col2:
            st.write(champion_info['description_text'])

        st.write('---')








