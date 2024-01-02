import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scraping_bdm(keyword,url:str='https://www.blogdumoderateur.com/',pages = 5) -> dict:
    data = {}
    for page in range(1, pages + 1):
        url = f"{url}/page/{page}/?s={keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        articles = soup.find_all('article')

        for artilce in articles:
            try:image_link = artilce.find('img')['data-lazy-src'] # Image
            except:image_link = None
            
            title = artilce.h3.text                                 # Title

            try:link = artilce.find('a')['href']                    # Link
            except:link = artilce.parent['href']

            time = artilce.time['datetime'].split('T')[0]           # Time
        
            try:label = artilce.find('span', 'favtag color-b').text  # label
            except:
                try:label = artilce.parent.parent.parent.parent.h2.text
                except:label = None

            data[artilce['id']] = {
                'title' : title,
                'image' : image_link,
                'link'  : link,
                'label':  label,
                'time'  : time
            }
    return data
def main():
    st.title("Scraper pour Blog du Modérateur")

    keyword = st.text_input("Entrez les mots-clés pour les articles")

    if st.button("Lancer la collecte"):
        data = scraping_bdm(keyword)

        df = pd.DataFrame.from_dict(data, orient='index')

        st.write(df)

        st.download_button(
            label="Télécharger les données en CSV",
            data=df.to_csv().encode('utf-8'),
            file_name='articles.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    main()
