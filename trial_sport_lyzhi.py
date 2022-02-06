from bs4 import BeautifulSoup
import requests
import re

url = 'https://trial-sport.ru/goods/51533/2174331.html'
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
allPrice = soup.findAll('div', class_='price price_disc')
print(allPrice)

for one_price in allPrice:
    #print(data)
    print(one_price.text)
    #print(data.attrs)
    #print(data.name)
    #print(data.class)
    #print(data.data-disabled-id)

    result = re.findall(r'\d+', one_price.text)
    print(result)

    print(result[0] + result[1])
    print('__'.join(result))
    print(''.join(result))

    price_str = result[0] + result[1]
    print(price_str)
    print(type(price_str))
    
    price_int = int(price_str)
    print(price_int)
    print(type(price_int))

#    if data.find('div', class_='left_panel_item_road') is not None:
#
#        soup2 = BeautifulSoup(data, "html.parser")
#        allNews2 = soup2.findAll('div', class_='left_panel_item_road')
#        for n in allNews2:
#            print(n.attrs)
#            filteredMap[n.attrs['data-disabled-id']] = 1 if 'disabled' not in n.attrs['class'] else 0
