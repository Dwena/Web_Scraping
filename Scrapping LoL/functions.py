from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import sqlite3

def scraping_lol(url='https://www.leagueoflegends.com/fr-fr/champions/'):
    driver = Edge()
    driver.get(url)

    # Utiliser By.CSS_SELECTOR pour la compatibilité avec Selenium 4
    champions_elements = driver.find_elements(By.CSS_SELECTOR, '.style__Text-sc-n3ovyt-3.kThhiV')
    champions_names = [element.text for element in champions_elements]
    
    # Connexion à la base de données SQLite
    conn = sqlite3.connect('champions.db')
    c = conn.cursor()

    c.execute('''
          CREATE TABLE IF NOT EXISTS champions
          ([name] TEXT PRIMARY KEY)
          ''')

    # Insérer les noms des champions dans la base de données
    for name in champions_names:
        c.execute("INSERT OR IGNORE INTO champions (name) VALUES (?)", (name,))

    # Commit et fermeture de la connexion à la base de données
    conn.commit()

    driver.quit()
    conn.close()





