import urllib.request
import socket
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json
from selenium import webdriver
def insert_into_file(filename,l):
    with open(filename,'a') as f:
        for item in l:
            f.write(item + '\n')

def get_domain_name(url):
   try:
       results = get_sub_domain_name(url).split('.')
       return results[-2] + '.' + results[-1]
   except:
       return ''



def get_sub_domain_name(url):
   try:
       return urlparse(url).netloc
   except:
       return ''
def get_url():
    complete_url_set=['https://hackathon.guide/','https://www.hackathon.com/','https://www.eventbrite.com/d/india--bangalore/hackathon/','https://hackinout.co/','https://www.meraevents.com/search?keyword=hackathon','https://www.eventshigh.com/detail/bangalore/618dc9fdb169679ec22319080a9eee94-inclusive-stem-hackathon-2019','https://www.townscript.com/india/hackathon']
    #url = "https://;skillenza.com"
    url_set=[]
    for i in complete_url_set:
        s = get_domain_name(i)
        url_set.append(s)
    client = webdriver.Firefox()
    for i in complete_url_set:
        client.get(i)
        sub ="hack"
        links = []
        soup = BeautifulSoup(client.page_source,'html.parser')
        for anchor in soup.find_all('a'):
            l = anchor.get('href','/')
            if sub in l :
                l = i + l
                links.append(l)
                insert_into_file('links.csv',links)
get_url()
