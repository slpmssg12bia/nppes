#!/usr/bin/python

import subprocess
import re
from bs4 import BeautifulSoup
import requests
import wget

def get_urls(soup):
    urls = []
    for a in soup.find_all('a', href=True):
        ul = a.find_all(text=re.compile('NPPES Data Dissemination'))
        if ul != []:
            urls.append(a)
            break
    print('done scraping the url...!')
    return urls

def download_and_extract(urls):
    for texts in urls:
        text = str(texts)
        file = text[50:142]
        print('zip file :', file)
        zip_link = texts['href']
        print('Downloading %s :' %zip_link)
        slashurl = zip_link.split('/')
        print(slashurl)
        wget.download("https://download.cms.gov/nppes/"+ slashurl[1])
        print("file downloaded....!!!")
        subprocess.run(["mv", slashurl[1], "db.zip"])
        subprocess.run(["unzip", "db.zip"])
        print("uploading the latest dump to s3")
        subprocess.run(["bash", "/home/ubuntu/nppes/nppes_dump_to_s3.sh"])
        subprocess.run(["bash", "/home/ubuntu/nppes/nppes_clean.sh"])
        return

r = requests.get('https://download.cms.gov/nppes/NPI_Files.html')
soup = BeautifulSoup(r.content, 'html.parser')
urls = get_urls(soup)
download_and_extract(urls)
