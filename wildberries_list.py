from bs4 import BeautifulSoup
import requests
import re

#url = 'https://www.wildberries.ru/catalog/35797682/detail.aspx?targetUrl=MI'
url1 = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page=1'
url2 = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page=2'
url3 = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page=3'
url4 = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page=4'
url5 = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page=5'


url = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page='
count_element_on_page = 25 * 4 #= 100
count_all_element = 1342
count_page = count_all_element // count_element_on_page
print('count_page = ', count_page)

def list_number_pages(count_page):
    numbers = []
    i = 1
    while i <= count_page:
        numbers.append(i)
        i = i + 1
    return numbers

numners = list_number_pages(count_page)

print('numners = ')
print(numbers)

def list_urls_final(nembers, url):
    list_urls = []
    for n in numbers:
        url_page = url + str(n) # dddd + ffff
        list_urls.append(url_page)
    return list_urls

list_urls = list_urls_final(numbers, url)



for url_new in list_urls:
    page = requests.get(url_new)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    allPrice = soup.findAll('ins', class_='lower-price')

    prices = []

    #print(allPrice)
    for one_price in allPrice:
        #print(data)
        #print(one_price.text)
        prices.append(one_price.text)

        #result = re.findall(r'\d+', one_price.text)
        #print(result)

        #print(result[0] + result[1])
        #print('__'.join(result))
        #print(''.join(result))

        #price_str = result[0] + result[1]
        #print(price_str)
        #print(type(price_str))
        #
        #price_int = int(price_str)
        #print(price_int)
        #print(type(price_int))


    allPrice1 = soup.findAll('span', class_='lower-price')
    for one_price in allPrice:
        #print(one_price.text)

        prices.append(one_price.text)

    print(len(prices))

    #prices.sort()
    #print(prices)


#####





#url = 'https://www.wildberries.ru/catalog/35797682/detail.aspx?targetUrl=MI'
#page = requests.get(url)
#print(page.status_code)
#soup = BeautifulSoup(page.text, "html.parser")
#allPrice = soup.findAll('span', class_='price-block__final-price')
#print(allPrice)
#
#for one_price in allPrice:
#    #print(data)
#    print(one_price.text)
#    #print(data.attrs)
#    #print(data.name)
#    #print(data.class)
#    #print(data.data-disabled-id)
#
#    result = re.findall(r'\d+', one_price.text)
#    print(result)
#
#    print(result[0] + result[1])
#    print('__'.join(result))
#    print(''.join(result))
#
#    price_str = result[0] + result[1]
#    print(price_str)
#    print(type(price_str))
#    
#    price_int = int(price_str)
#    print(price_int)
#    print(type(price_int))
#
##    if data.find('div', class_='left_panel_item_road') is not None:
##
##        soup2 = BeautifulSoup(data, "html.parser")
##        allNews2 = soup2.findAll('div', class_='left_panel_item_road')
##        for n in allNews2:
##            print(n.attrs)
##            filteredMap[n.attrs['data-disabled-id']] = 1 if 'disabled' not in n.attrs['class'] else 0
