import urllib.request
from bs4 import BeautifulSoup as bs
import logging
flipkart_url = "https://www.flipkart.com/search?q=" + "tv"
res=urllib.request.urlopen(flipkart_url)
#res.urlopen()
html=res.read()
flipkart_html=bs(html,'html.parser')

flipkart_div=flipkart_html.find_all("div",{"class":"_1AtVbE col-12-12"})
#bigboxes=len(flipkart_div)
#print(bigboxes)
#type bigboxes
del flipkart_div[0:3]
anchor =flipkart_div[0].div.div.div.a['href']
url="https://www.flipkart.com"+ anchor
res=urllib.request.urlopen(url)
product_req = res.read()
product_html= bs(product_req,'html.parser')
product_div= product_html.find_all("div",{"class":"_27M-vq"})
#product_review=product_div[0].div.div.p
print(product_div)