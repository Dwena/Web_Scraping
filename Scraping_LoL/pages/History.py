import streamlit as st
import sqlite3

# Afficher l'historique des recherches
def show_history():
    # Connexion à la base de données
    conn = sqlite3.connect('search_history.db')
    c = conn.cursor()
    
    # Récupérer l'historique des recherches
    c.execute("SELECT * FROM search_history")
    history = c.fetchall()
    
    # Afficher l'historique
    for entry in history:
        with st.expander(f"{entry[1]} : {entry[0]}"):
            results = eval(entry[2])

            for result in results:
                col1, col2,col3 = st.columns([1, 3, 1])  
                with col1:
                    st.image(result['image_url'], width=170)
                with col2:
                    st.write(result["champion"] + ": " + result['summary'])
                    st.write(result['description'])
                with col3:
                    st.write(result['role'] +" : ")
                    st.write(result['role_value'])
                st.write('---')

    
    conn.close()

show_history()
