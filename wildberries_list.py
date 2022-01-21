from bs4 import BeautifulSoup
import requests
import re

def list_number_pages(count_page):
    numbers = []
    i = 1
    while i <= count_page:
        numbers.append(i)
        i = i + 1
    return numbers

def list_urls_final(nembers, url):
    list_urls = []
    for n in numbers:
        url_page = url + str(n) # dddd + ffff
        list_urls.append(url_page)
    return list_urls

def get_prices_from_page(url_new):
    page = requests.get(url_new)
    print(page.status_code)
    prices = []
    soup = BeautifulSoup(page.text, "html.parser")

    allPrice = soup.findAll('ins', class_='lower-price')
    for one_price in allPrice:
        prices.append(one_price.text)

    allPrice1 = soup.findAll('span', class_='lower-price')
    for one_price in allPrice:
        prices.append(one_price.text)

    return prices

url = 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort=priceup&page='
count_element_on_page = 25 * 4 #= 100
count_all_element = 1342
count_page = count_all_element // count_element_on_page
print('count_page = ', count_page)

numbers = list_number_pages(count_page)

print('numners = ')
print(numbers)

list_urls = list_urls_final(numbers, url)

for url_k in list_urls:
    prices = get_prices_from_page(url_k)
    print(len(prices))
    #prices.sort()
    #print(prices)
