from bs4 import BeautifulSoup
import requests
import re
print("ALie-Express")

url = 'https://aliexpress.ru/item/1005003120035476.html?spm=a2g2w.home.0.1.75df501dZVtJ92&pdp_ext_f=%7B%22ship_from%22:%22RU%22,%22sku_id%22:%2212000024206607836%22%7D&&scm=1007.31960.266214.0&scm_id=1007.31960.266214.0&scm-url=1007.31960.266214.0&pvid=2fc93a94-b2e6-4746-8765-2b8ca04e1ff1&utparam=%257B%2522process_id%2522%253A%25221001%2522%252C%2522x_object_type%2522%253A%2522product%2522%252C%2522pvid%2522%253A%25222fc93a94-b2e6-4746-8765-2b8ca04e1ff1%2522%252C%2522belongs%2522%253A%255B%257B%2522id%2522%253A%2522477005%2522%252C%2522type%2522%253A%2522dataset%2522%257D%255D%252C%2522scm%2522%253A%25221007.31960.266214.0%2522%252C%2522tpp_buckets%2522%253A%252221669%25230%2523186385%252397_21669%25234190%252319167%2523916_21960%25230%2523266214%25230%2522%252C%2522x_object_id%2522%253A%25221005003120035476%2522%257D'
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
allPrice = soup.findAll('span', class_='ali-kit_Base__base__1odrub ali-kit_Base__default__1odrub ali-kit_Base__strong__1odrub price ali-kit_Price__size-xl__12ybyf Product_Price__current__1uqb8 product-price-current')
allPrice1 = soup.findAll('h1', class_='ali-kit_Base__base__1odrub ali-kit_Base__default__1odrub ali-kit_Heading__heading__1mk5o0 ali-kit_Heading__size-xxl__1mk5o0 Product_Name__productTitleText__hntp3')




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

#Hello
