from time import sleep
import time

def scraping_doctolib(n_page=5, time_sleep=1):
    # Start Project
    driver = Edge()
    driver.get("https://www.doctolib.fr/dentiste/paris")
    driver.find_element(By.ID, 'didomi-notice-agree-button').click()
    data_doctors = {}
    for n in range(1, n_page):
        driver.get(f'https://www.doctolib.fr/dentiste/paris?page={n}')
        sleep(time_sleep)
        doctors = driver.find_elements(By.CLASS_NAME, "dl-search-result-presentation")
        for doctor in doctors:
            data_doctors[doctor.find_element(By.TAG_NAME,'h3').text] = {
                'img' : doctor.find_element(By.TAG_NAME, 'img').get_attribute('src'),
                'adresse' : doctor.find_element(By.TAG_NAME,'span').text
            }
    driver.quit()
    return data_doctors


def scraping_les_echos(theme='IA', n_articles=10):

    driver = Chrome('./chromedriver')

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