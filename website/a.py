import urllib.request
import socket
from bs4 import BeautifulSoup
import json
from selenium import webdriver
def insert_into_file(filename,l):
    with open(filename,'a') as f:
        for item in l:
            f.write(item + '\n')
def get_url():
    #url = "https://www.pravega.org/events"
    client = webdriver.Firefox()
    client.get("https://allevents.in/bangalore/hackathon#")
    sub ="hackathon"
    #sub1 = "competitive"
    sub2 = "mailto"
    links =set()
    soup = BeautifulSoup(client.page_source,'html.parser')
    for anchor in soup.find_all('a'):
        l=anchor.get('href','/')
        if sub in l  :
            if sub2 in l:
                pass
            else:    
        #        l = url + l
                print(l)
                links.add(l)
    insert_into_file('links2.csv',links)
def get_url1():
    url = "https://www.pravega.org/events/ibm-hackathon/"
    client = webdriver.Firefox()   
    sub ="hackathon"
    #sub1 = "competitive"
    #sub2 = "mailto"
    links =set()
    soup = BeautifulSoup(client.page_source,'html.parser')
    for anchor in soup.find_all('a'):
        l=anchor.get('href','/')
        if sub in l  :
            if sub2 in l:
                pass
            else:
        #        l = url + l
                print(l)
                links.add(l)
    insert_into_file('links2.csv',links)
def get_url2():
    #url = "https://www.pravega.org/events"
    client = webdriver.Firefox()
    client.get("https://www.hackerearth.com/challenges")
    sub ="hackathon"
    sub1 = "competitive"
    sub2 = "hackerearth"
    links =set()
    soup = BeautifulSoup(client.page_source,'html.parser')
    for anchor in soup.find_all('a'):
        l=anchor.get('href','/')
        if sub and sub1 and not sub2 in l  :
            if sub2 in l:
                pass
            else:
                #l = url + l
                print(l)
                links.add(l)
    insert_into_file('links2.csv',links)
def get_url3():
    #url = "https://www.pravega.org/events"
    client = webdriver.Firefox()
    client.get("https://dare2compete.com")
    sub ="hackathon"
    #sub1 = "competitive"
    #sub2 = "hackerearth"
    links =set()
    soup = BeautifulSoup(client.page_source,'html.parser')
    for anchor in soup.find_all('a'):
        l=anchor.get('href','/')
        if sub in l  :
                l = url + l
                print(l)
                links.add(l)
    insert_into_file('links2.csv',links)
def get_url4():
    #url = "https://www.pravega.org/events"
    client = webdriver.Firefox()
    client.get("https://www.hackathon.com")
    sub ="events"    
    links =set()
    soup = BeautifulSoup(client.page_source,'html.parser')
    for anchor in soup.find_all('a'):
        l=anchor.get('href','/')
        if sub and sub1 and not sub2 in l  :                
            #l = url + l
            print(l)
            links.add(l)
    insert_into_file('links2.csv',links)
get_url()
get_url1()
get_url2()
get_url3()
get_url4()
#def parsing_pages(link):
'''html = urllib.request.urlopen('https://dare2compete.com/e/hackathons/latest')
soup = BeautifulSoup(html,'html.parser')
for anchor in soup.find_all('a'):
    anchor.get('href','/')
    
def validate_url(url):
    ip = socket.gethostbyname('sit.ac.in')
    api = 'http://geoip-db.com/jsonp/'+ ip
    link1= urllib.request.urlopen("https://geoip-db.com/json")
    data = json.loads(link1.read().decode())
    return data['country_name']
    '''