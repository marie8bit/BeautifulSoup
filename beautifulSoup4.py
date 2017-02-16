from bs4 import BeautifulSoup
import requests
from datetime import *
import sys
url = 'http://tagmeth.livejournal.com/64243.html'
response = requests.get(url)
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')
title = (soup.title.string)
dateTime = (datetime.now())
dt = dateTime.date()
dat= str(dt)
f = open (dat, 'w')
f.write(str(dateTime)='\n')
f.write(title)
#print (soup.find_all('h2'))
#print (soup.prettify())
