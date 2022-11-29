#!/usr/bin/python

import subprocess
import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import wget

# postgres_data.dmp
def get_urls(soup):
    urls = []
    for a in soup.find_all('a', href=True):
        ul = a.find_all(text=re.compile("Weekly Update"))
        if ul != []:
            urls.append(a)
    print('done scraping the url......!!!!')
    return urls

def download_and_extract(urls):
    for texts in urls:
        text = str(texts)
        file = text[11:56]
        print('zip file :', file)
        date = file[32:38]
        print(date)
        fileDate = datetime.strptime(date, '%m%d%y').date()
        print('file date :', fileDate)
        zip_link = texts['href']
        print('Downloading %s :' %zip_link)
        slashurl = zip_link.split('/')
        print(slashurl)
        wget.download("https://download.cms.gov/nppes/"+ slashurl[1])
        print("file downloaded....!!!")
        subprocess.run(["mv", slashurl[1], "db.zip"])
        subprocess.run(["unzip", "db.zip"])
        print("uploading the latest dump to s3")
        subprocess.run(["bash", "nppes_dump_to_s3.sh"])
        subprocess.run(["bash", "nppes_clean.sh"])
        return

r = requests.get('https://download.cms.gov/nppes/NPI_Files.html')
soup = BeautifulSoup(r.content, 'html.parser')
urls = get_urls(soup)
download_and_extract(urls)
