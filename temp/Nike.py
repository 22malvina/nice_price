from bs4 import BeautifulSoup
import requests
import re
print("Nike")

url='https://www.nike.com/ru/t/%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8-air-force-1-07-TjhXcv/DR0143-101'
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
allPrice = soup.findAll('div', class_='product-price css-11s12ax is--current-price css-tpaepq')
allPrice1 = soup.findAll('h1', class_='headline-2 css-zis9ta')
#hello



for one_price in allPrice:
    #print(data)
    print(one_price.text)
    #print(data.attrs)
    #print(data.name)
    #print(data.class)
    #print(data.data-disabled-id)

for one_price1 in allPrice1:
    #print(data)
    print(one_price1.text)
    #print(data.attrs)
    #print(data.name)
    #print(data.class)
    #print(data.data-disabled-id)

