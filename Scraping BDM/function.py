import requests
import random
import time

import streamlit as st

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def scraping_bdm(url:str='https://www.blogdumoderateur.com/', data={}) -> dict:
    response_bdm = requests.get(url)
    soup_bdm = BeautifulSoup(response_bdm.text)
    artilces = soup_bdm.find_all('article')


    for artilce in artilces:
        
        try:image_link = artilce.find('img')['src'] # Image
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


def scraping_les_echos(theme='IA', n_articles=10):

    try:driver = Chrome()
    except:driver = Chrome('./chromedriver')

    driver.get('https://www.lesechos.fr/')
    # Cookies consent
    driver.find_element(By.ID, 'didomi-notice-agree-button').click()

    driver.find_element(By.CLASS_NAME, 'sc-14kwckt-16.sc-16o6ckw-0.WiTvs.bvLlpL.sc-ctlfsq-0.lnDWGz').click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'sc-14kwckt-28 sc-ywv8p0-0 sc-166k8it-1 wwuyu jCZKki cQRcWN'.replace(' ', '.')).send_keys(theme+Keys.ENTER)
    time.sleep(2)
    data_les_echos = {}
    articles = driver.find_elements(By.TAG_NAME, 'article')
    for n_article in range(1, n_articles):
        time.sleep(2)
        title = articles[n_article].find_element(By.TAG_NAME, 'h3').text                            #Tire
        link = articles[n_article].find_element(By.TAG_NAME, 'a').get_attribute('href')             #Lien
        
        try:img = articles[n_article].find_element(By.TAG_NAME, 'img').get_attribute('src')             # Image
        except:img = None

        driver.get(link)
        time.sleep(2)

        try:author = driver.find_element(By.CLASS_NAME, 'sc-kla0ai-0.hEKJIU').text                      # Autor
        except: author = None

        try:date = driver.find_element(By.CLASS_NAME, 'sc-17ifq26-0.eJxzlO').text                       # Date de publication
        except: date=None
        driver.back()
        time.sleep(2)
        
        articles = driver.find_elements(By.TAG_NAME, 'article')
        data_les_echos[str(random.randint(10000, 1000000))] ={
            'title':title,
            'link':link,
            'img':img,
            'date':date,
            'author':author,
        }
    driver.quit()
    return data_les_echos