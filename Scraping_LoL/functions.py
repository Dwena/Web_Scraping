from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time
import csv
from io import StringIO

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

    image_url = driver.find_element(By.CSS_SELECTOR, 'img.style__Img-sc-g183su-1').get_attribute('src')

    try:driver.find_element(By.CSS_SELECTOR, 'div.style__Desc-sc-8gkpub-9 p button').click()
    except:pass

    try:driver.find_element(By.CSS_SELECTOR, 'div.style__Desc-sc-8gkpub-9.jheTpK p button').click()
    except:pass
    description_text = driver.find_element(By.CSS_SELECTOR, 'div.style__Desc-sc-8gkpub-9 p').text
    summary = driver.find_element(By.CSS_SELECTOR, "[data-testid='overview:subtitle']").text

    list_item = driver.find_element(By.CSS_SELECTOR, 'li.style__SpecsItem-sc-8gkpub-12')

    role_type_element = list_item.find_element(By.CSS_SELECTOR, "div[data-testid='overview:rolestring']")
    role_text = role_type_element.text

    role_value_element = list_item.find_element(By.CSS_SELECTOR, "div[data-testid='overview:role']")
    role_value_text = role_value_element.text

    return {
        "image_url": image_url,
        "description_text": description_text,
        "summary": summary,
        "role": role_text,
        "role_value": role_value_text,
    }

def convert_df_to_csv(results):
    output = StringIO()
    writer = csv.writer(output)

    header = results[0].keys()
    writer.writerow(header)

    for row in results:
        writer.writerow(row.values())

    return output.getvalue()
