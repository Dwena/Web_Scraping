import sqlite3
import streamlit as st
from functions import *

st.title('Home')
st.write('Welcome to the League of Legends champions database !')
st.write('You can find here all the champions of the game, their stats, their lore, and more !')
st.write('You can also find the items of the game, their stats, their recipes, and more !')

# Connexion à la base de données SQLite
conn = sqlite3.connect('champions.db')
c = conn.cursor()
scraping_lol()
# Afficher les champions dans un tableau
c.execute("SELECT * FROM champions")
champions = c.fetchall()
st.write('Champions :')
st.table(champions)
# Fermeture de la connexion à la base de données
conn.close()