from bs4 import BeautifulSoup
import requests


url = 'http://mignews.com/mobile'


page = requests.get(url)


print(page.status_code)


filteredNews = []
allNews = []


soup = BeautifulSoup(page.text, "html.parser")


#print(soup)
print('aaaaaaaaaaa')


allNews = soup.findAll('a', class_='lenta')


for data in allNews:
    if data.find('span', class_='time2 time3') is not None:
        filteredNews.append(data.text)



for data in filteredNews:
    print(data)



print('aaaaaaaaaaa')

##########

url = 'https://kk.polyanaski.ru/winter/'
page = requests.get(url)
print(page.status_code)
filteredNews = []
filteredAtr = []
filteredMap = {}
allNews = []
soup = BeautifulSoup(page.text, "html.parser")
#print(soup)
print('aaaaaaaaaaa')


allNews = soup.findAll('div', class_='left_panel_item summer')
print(allNews)


print('aaaaaaaaaaa')
print('aaaaaaaaaabbbbb')
for data in allNews:
    if data.find('div', class_='left_panel_item_road') is not None:
        filteredNews.append(data.text)
        filteredAtr.append(data)
        print('---')
        print('---')
        print(data.attrs)
        #print(data.name)
        #print(data.class)
        #print(data.data-disabled-id)


        soup2 = BeautifulSoup(data, "html.parser")

        allNews2 = soup2.findAll('div', class_='left_panel_item_road')
        for n in allNews2:
            print(n.attrs)
            filteredMap[n.attrs['data-disabled-id']] = 1 if 'disabled' not in n.attrs['class'] else 0

        print('+++')


print('aaaaaaaaaaa')
print(filteredMap)
print('aaaaaaaaaaa')


for data in filteredNews:
    print(data)


print('aaaaaaaaaaa')
print(filteredAtr)

import json
data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
order_data_dict = json.loads(data_string)

