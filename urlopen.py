import urllib.request
from bs4 import BeautifulSoup as bs
import logging
flipkart_url = "https://www.flipkart.com/search?q=" + "tv"
res=urllib.request.urlopen(flipkart_url)
res.urlopen()
html=res.read()
print(html)