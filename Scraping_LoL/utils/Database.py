import sqlite3
from datetime import datetime

class Database:
    def save_data(search_query, results):
        conn = sqlite3.connect('search_history.db')
        c = conn.cursor()
        c.execute("INSERT INTO search_history (timestamp, search_query, results) VALUES (?, ?, ?)",
                (datetime.now(), search_query, str(results)))
        conn.commit()
        conn.close()

    def connect_database():
        # Connexion à la base de données (elle sera créée si elle n'existe pas)
        conn = sqlite3.connect('search_history.db')
        c = conn.cursor()

        # Créer la table de l'historique des recherches
        c.execute('''
                CREATE TABLE IF NOT EXISTS search_history
                (timestamp DATETIME, search_query TEXT, results TEXT)
                ''')
        conn.commit()
        conn.close()
