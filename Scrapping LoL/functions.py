from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import sqlite3
import time

def scraping_lol(url='https://www.leagueoflegends.com/fr-fr/champions/'):
    driver = Edge()
    driver.get(url)

    # Utiliser By.CSS_SELECTOR pour la compatibilité avec Selenium 4
    champions_elements = driver.find_elements(By.CSS_SELECTOR, '.style__Text-sc-n3ovyt-3.kThhiV')
    champions_names = [element.text for element in champions_elements]
    
    # Connexion à la base de données SQLite
    return champions_names

def scraping_champions_info(champion_name ,base_url="https://www.leagueoflegends.com/fr-fr/champions/"):
    if champion_name.find(' ') != -1:
        champion_name = champion_name.replace(' ', '-')
    url = base_url + champion_name.lower()
    driver = Edge()
    driver.get(url)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".osano-cm-accept-all.osano-cm-buttons__button.osano-cm-button.osano-cm-button--type_accept").click()

    image_element = driver.find_element(By.CSS_SELECTOR, 'img.style__Img-sc-g183su-1')
    image_url = image_element.get_attribute('src')

    try:driver.find_element(By.CSS_SELECTOR, 'div.style__Desc-sc-8gkpub-9 p button').click()
    except:pass

    try:driver.find_element(By.CSS_SELECTOR, 'div.style__Desc-sc-8gkpub-9.jheTpK p button').click()
    except:pass
    description_element = driver.find_element(By.CSS_SELECTOR, 'div.style__Desc-sc-8gkpub-9 p')
    description_text = description_element.text

    return {
        "image_url": image_url,
        "description_text": description_text
    }




