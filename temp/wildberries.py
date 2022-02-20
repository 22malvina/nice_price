from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.wildberries.ru/catalog/57483486/detail.aspx?targetUrl=BP'
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
allPrice = soup.findAll('span', class_='price-block__final-price')
name = soup.findAll('h1', class_='same-part-kt__header')

for one_price in allPrice:
    #print(data)
    print(one_price.text)
    #print(data.attrs)
    #print(data.name)
    #print(data.class)
    #print(data.data-disabled-id)
  

for one_price1 in name:
    #print(data)
    print(one_price1.text)
    #print(data.attrs)
    #print(data.name)
    #print(data.class)
    #print(data.data-disabled-id)
   

#Hello world!
