import streamlit as st
from functions import *
from utils.Database import Database

st.set_page_config(
    page_title='League Of Legends Scraper',  
    page_icon='utils/favicon_io/favicon.ico',
    layout='wide',  
    initial_sidebar_state='expanded'  
)

@st.cache_data
def load_data():
    return scraping_lol()


video_url = "https://www.leagueoflegends.com/static/hero-3e934348790824f4b800524f96a93020.mp4"
image_url = "https://www.leagueoflegends.com/static/logo-1200-04b3cefafba917c9c571f9244fd28a1e.png"


st.sidebar.image(image_url, width=200, use_column_width=True, output_format='PNG', clamp=False, channels='RGB')
st.sidebar.write("On utilise selenium pour récupérer les données du site officiel de League Of Legends : https://www.leagueoflegends.com/fr-fr/champions/")
st.sidebar.title("ATIA Ali-Haïdar")


champions_names = load_data()
# Afficher les champions dans une liste déroulante mutlitple
champions = st.multiselect('Select champions', champions_names)

# Utiliser un bouton pour lancer la recherche des informations de la liste déroulante
if st.button('Search'):
    # Accumuler les informations de tous les champions recherchés
    all_champion_info = []

    for champion in champions:
        champion_info = scraping_champions_info(champion)

        # Afficher les informations du champion
        col1, col2,col3 = st.columns([1, 3, 1])  
        with col1:
            st.image(champion_info['image_url'], width=170)
        with col2:
            st.write(champion + ": " + champion_info['summary'])
            st.write(champion_info['description_text'])
        with col3:
            st.write(champion_info['role'] +" : ")
            st.write(champion_info['role_value'])
        

        st.write('---')

        # Ajouter les informations du champion à la liste de tous les résultats
        all_champion_info.append({
            "champion": champion,
            "summary": champion_info['summary'],
            "description": champion_info['description_text'],
            "image_url": champion_info['image_url'],
            "role": champion_info['role'],
            "role_value": champion_info['role_value'],
        })

    search_query = ', '.join(champions)
    Database.save_data(search_query, all_champion_info)

    csv_data = convert_df_to_csv(all_champion_info)

    # Bouton de téléchargement
    st.download_button(
        label="Télécharger les données en CSV",
        data=csv_data,
        file_name='results.csv',
        mime='text/csv',
    )

st.video(video_url)







